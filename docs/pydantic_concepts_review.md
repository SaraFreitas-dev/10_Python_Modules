# Pydantic v2 - Core Concepts Review

This document explains the main Pydantic concepts used in the exercises from the *Cosmic Data* module (nº9).

---

# What is Pydantic?

Pydantic is a Python library used for:

- Data validation
- Automatic type conversion
- Parsing external data
- Safer and cleaner models

It allows developers to define strict data structures using Python type hints.

---

# BaseModel

`BaseModel` is the foundation of every Pydantic model.

When a class inherits from `BaseModel`, Pydantic automatically validates the data.

## Example

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

## Creating an object

```python
user = User(name="Sara", age=20)
```

---

# Automatic Type Conversion

Pydantic automatically converts compatible types.

## Example

```python
user = User(name="Sara", age="20")
```

Even though `"20"` is a string, Pydantic converts it into an integer.

---

# ValidationError

If invalid data is provided, Pydantic raises a `ValidationError`.

## Example

```python
User(name="Sara", age="abc")
```

Output:

```python
ValidationError
```

Because `"abc"` cannot be converted into an integer.

---

# Field

`Field()` is used to add validation constraints and metadata to attributes.

---

# Numeric Constraints

## Example

```python
from pydantic import Field

age: int = Field(ge=18, le=80)
```

### Meaning

- `ge` = greater or equal
- `le` = less or equal

This means age must be between 18 and 80.

---

# String Constraints

## Example

```python
name: str = Field(min_length=3, max_length=50)
```

The string:
- must contain at least 3 characters
- cannot exceed 50 characters

---

# Float Constraints

## Example

```python
power_level: float = Field(ge=0.0, le=100.0)
```

Useful for percentages and ranges.

---

# Default Values

Pydantic supports default values.

## Example

```python
is_active: bool = True
```

If no value is provided, the field automatically becomes `True`.

---

# Optional Fields

Optional fields may contain a value or `None`.

## Example

```python
from typing import Optional

notes: Optional[str]
```

Equivalent to:

```python
str | None
```

---

# Enum

Enums restrict a field to predefined values.

---

# Example

```python
from enum import Enum

class Rank(str, Enum):
    CAPTAIN = "captain"
    COMMANDER = "commander"
```

---

# Why use Enum?

Enums prevent invalid values.

## Valid

```python
rank="captain"
```

## Invalid

```python
rank="banana"
```

This would raise a validation error.

---

# model_validator

`@model_validator` is used for custom validation logic.

It is useful when validation depends on multiple fields.

---

# Pydantic v2 Syntax

```python
from pydantic import model_validator

@model_validator(mode='after')
```

---

# mode='after'

This means:

1. Pydantic validates all fields first
2. Then your custom validation logic runs

---

# Example

```python
@model_validator(mode='after')
def validate_contact(self):

    if self.contact_type == "physical" and not self.is_verified:
        raise ValueError("Physical contacts must be verified")

    return self
```

This type of validation cannot be done with `Field()` alone.

---

# return self

Inside a model validator, `return self` is required.

It returns the validated model instance.

---

# Nested Models

Nested models are models inside other models.

---

# Example

```python
class CrewMember(BaseModel):
    name: str

class SpaceMission(BaseModel):
    crew: list[CrewMember]
```

---

# What happens automatically?

Pydantic:
- validates the list
- validates every CrewMember
- converts data automatically

---

# Dictionary Unpacking (`**data`)

`**data` converts a dictionary into keyword arguments.

---

# Example

```python
data = {
    "name": "Sara",
    "age": 20
}

User(**data)
```

Equivalent to:

```python
User(name="Sara", age=20)
```

---

# Datetime Validation

Pydantic automatically parses datetime values.

## Example

```python
from datetime import datetime

created_at: datetime
```

It can convert:
- datetime objects
- valid datetime strings
- timestamps

---

# Field vs model_validator

## Field

Used for single-field validation.

### Example

```python
age: int = Field(ge=18)
```

Validates only the `age` field.

---

## model_validator

Used for validation involving multiple fields.

### Example

```python
if duration_days > 365 and crew_size < 5:
    raise ValueError("Long missions require larger crews")
```

This depends on multiple attributes.

---

# Main Advantages of Pydantic

- Cleaner code
- Automatic validation
- Better error messages
- Automatic type conversion
- Easier API and data handling
- Strong typing support

---

# Summary

| Concept | Purpose |
|---|---|
| BaseModel | Creates validated models |
| Field | Adds constraints to fields |
| Enum | Restricts possible values |
| ValidationError | Raised when validation fails |
| model_validator | Custom validation logic |
| Optional | Allows `None` values |
| Nested Models | Models inside other models |
| datetime | Automatic datetime parsing |

---
