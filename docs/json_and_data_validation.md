# JSON and Data Validation Guide

A beginner-friendly guide to JSON, serialization, schemas, and data validation in Python.

This document explains:
- JSON
- serialization
- deserialization
- validation
- schemas
- common validation techniques

These concepts are heavily used in:
- APIs
- web development
- configuration files
- parsers
- databases
- game systems
- data engineering

---

# What is JSON?

JSON stands for:

```text
JavaScript Object Notation
```

It is a lightweight format used to store and exchange data.

JSON is one of the most common data formats in the world.

---

# Why JSON is Popular

JSON is:
- human readable
- easy to parse
- language independent
- lightweight
- widely supported

---

# Basic JSON Example

```json
{
    "name": "Sara",
    "age": 20,
    "is_active": true
}
```

---

# JSON Data Types

| JSON Type | Python Equivalent |
|---|---|
| string | str |
| number | int / float |
| boolean | bool |
| object | dict |
| array | list |
| null | None |

---

# JSON Objects

JSON objects are similar to Python dictionaries.

---

# Example

```json
{
    "username": "Sara",
    "score": 100
}
```

Equivalent Python dictionary:

```python
{
    "username": "Sara",
    "score": 100
}
```

---

# JSON Arrays

Arrays are similar to Python lists.

---

# Example

```json
[
    "apple",
    "banana",
    "orange"
]
```

Equivalent Python list:

```python
["apple", "banana", "orange"]
```

---

# Serialization

Serialization means converting Python objects into JSON.

---

# Why Serialization Matters

Serialization is used when:
- sending API responses
- saving files
- storing data
- sending network messages

---

# Python Serialization Example

```python
import json

data = {
    "name": "Sara",
    "age": 20
}

json_text = json.dumps(data)

print(json_text)
```

---

# json.dumps()

`dumps` means:

```text
dump string
```

It converts Python data into a JSON string.

---

# Example Output

```json
{"name": "Sara", "age": 20}
```

---

# Pretty JSON Formatting

```python
json.dumps(data, indent=4)
```

Produces readable JSON.

---

# Deserialization

Deserialization means converting JSON into Python objects.

---

# Example

```python
import json

text = '{"name": "Sara", "age": 20}'

data = json.loads(text)

print(data["name"])
```

---

# json.loads()

`loads` means:

```text
load string
```

It converts JSON text into Python objects.

---

# Working with JSON Files

---

# Writing JSON Files

```python
import json

data = {
    "name": "Sara",
    "score": 42
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
```

---

# Reading JSON Files

```python
import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data)
```

---

# dump vs dumps

| Function | Purpose |
|---|---|
| json.dump | Writes JSON to file |
| json.dumps | Returns JSON string |
| json.load | Reads JSON from file |
| json.loads | Reads JSON from string |

---

# What is Validation?

Validation checks if data is:
- correct
- complete
- safe
- expected

Validation prevents:
- crashes
- invalid data
- corrupted systems

---

# Example Without Validation

```python
age = int(user_input)
```

If input is:

```text
hello
```

the program crashes.

---

# Example With Validation

```python
if user_input.isdigit():
    age = int(user_input)
else:
    print("Invalid age")
```

---

# Why Data Validation Matters

Validation is critical in:
- APIs
- config parsers
- user input
- databases
- file systems

Bad data can:
- crash applications
- create security problems
- corrupt files
- break systems

---

# Schemas

A schema defines:
- the structure of data
- required fields
- data types
- validation rules

Schemas describe what valid data looks like.

---

# Example Schema Concept

```text
User:
- name -> string
- age -> integer
- email -> string
```

---

# Validation Using Pydantic

Pydantic validates data using schemas defined as Python classes.

---

# Example

```python
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
```

---

# Valid Data

```python
User(name="Sara", age=20)
```

---

# Invalid Data

```python
User(name="Sara", age="hello")
```

This raises:

```text
ValidationError
```

---

# Field Validation

Pydantic supports extra validation using `Field`.

---

# Example

```python
from pydantic import BaseModel, Field


class User(BaseModel):
    age: int = Field(ge=18, le=99)
```

---

# Validation Rules

This means:
- age must be >= 18
- age must be <= 99

---

# Optional Fields

```python
from typing import Optional

nickname: Optional[str]
```

Allows:
- string
- or None

---

# Nested Validation

Schemas can contain other schemas.

---

# Example

```python
class Address(BaseModel):
    city: str


class User(BaseModel):
    address: Address
```

Pydantic validates nested objects automatically.

---

# Custom Validation

Sometimes validation depends on multiple fields.

---

# Example

```python
if duration_days > 365 and crew_size < 5:
    raise ValueError("Crew too small")
```

---

# Common Validation Techniques

| Validation Type | Example |
|---|---|
| Type validation | int, str, bool |
| Range validation | age >= 18 |
| Length validation | min_length=3 |
| Format validation | email structure |
| Required fields | missing keys |
| Business rules | custom logic |

---

# Common JSON Problems

---

# Invalid Syntax

Bad JSON:

```json
{
    "name": "Sara",
}
```

Trailing commas are invalid.

---

# Wrong Types

```json
{
    "age": "hello"
}
```

Expected integer:
- received string

---

# Missing Fields

```json
{
    "name": "Sara"
}
```

Missing required fields may break validation.

---

# Security Considerations

Never trust external JSON blindly.

Always validate:
- API data
- uploaded files
- config files
- network messages

---

# Real 42 Examples

## Config Parser

```json
{
    "width": 20,
    "height": 15
}
```

---

## Game Save Data

```json
{
    "player": "Sara",
    "level": 5,
    "position": [10, 20]
}
```

---

## API Response

```json
{
    "status": "ok",
    "data": {}
}
```

---

# Best Practices

- Always validate external data
- Use schemas for structure
- Keep JSON readable
- Use meaningful field names
- Validate before processing
- Handle invalid data safely

---

# Summary Table

| Concept | Purpose |
|---|---|
| JSON | Data exchange format |
| Serialization | Python -> JSON |
| Deserialization | JSON -> Python |
| Validation | Checks correctness |
| Schema | Defines data structure |
| Pydantic | Validation library |

---

# Final Notes

JSON and validation are fundamental concepts in modern software development.

Understanding them is essential for:
- APIs
- game systems
- parsers
- databases
- backend systems
- configuration management

Good validation creates:
- safer applications
- cleaner code
- fewer crashes
- better debugging
- more reliable systems

---
