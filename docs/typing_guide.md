# Python Typing Guide

A beginner-friendly guide to Python type hints and typing concepts commonly used in modern Python projects.

This document focuses on the typing features frequently used in 42 Python modules and real-world applications.

---

# Why Use Typing?

Type hints improve:

- Code readability
- Error detection
- IDE autocompletion
- Project maintainability
- Static analysis with `mypy`

Typing makes code easier to understand and safer to maintain.

---

# Basic Type Hints

## Example

```python
name: str = "Sara"
age: int = 20
height: float = 1.70
is_active: bool = True
```

---

# Function Type Hints

## Example

```python
def add(a: int, b: int) -> int:
    return a + b
```

### Explanation

- `a: int` → parameter must be an integer
- `-> int` → function returns an integer

---

# list[str]

Used for lists containing only strings.

## Example

```python
names: list[str] = ["Sara", "John", "Alice"]
```

---

# dict[str, int]

Dictionary where:
- keys are strings
- values are integers

## Example

```python
student_scores: dict[str, int] = {
    "Sara": 18,
    "John": 15
}
```

---

# tuple[int, int]

Tuple with two integers.

Very common in:
- game development
- coordinates
- maze projects
- pathfinding systems

## Example

```python
position: tuple[int, int] = (5, 10)
```

---

# Optional

`Optional` means a value can be:
- a specific type
- or `None`

## Example

```python
from typing import Optional

nickname: Optional[str] = None
```

Equivalent to:

```python
nickname: str | None = None
```

---

# Union

`Union` allows multiple possible types.

## Example

```python
from typing import Union

value: Union[int, str]
```

Equivalent to:

```python
value: int | str
```

---

# Any

`Any` disables type checking for a variable.

## Example

```python
from typing import Any

data: Any
```

---

# Callable

`Callable` describes functions as types.

## Example

```python
from collections.abc import Callable

operation: Callable[[int, int], int]
```

Meaning:
- accepts two integers
- returns one integer

---

# Callable Function Example

```python
from collections.abc import Callable

def calculate(
    a: int,
    b: int,
    operation: Callable[[int, int], int]
) -> int:

    return operation(a, b)
```

---

# Nested Typing

Typing structures can be combined.

## Example

```python
maze: list[list[int]]
```

A list containing lists of integers.

---

# Complex Example

```python
player_positions: dict[str, tuple[int, int]]
```

Dictionary:
- key → player name
- value → `(x, y)` coordinates

---

# Common 42 Examples

## Maze coordinates

```python
position: tuple[int, int]
```

---

## BFS queue

```python
queue: list[tuple[int, int]]
```

---

## Graph structure

```python
graph: dict[str, list[str]]
```

---

# Type Aliases

Useful for improving readability.

## Example

```python
Position = tuple[int, int]

player_position: Position
enemy_position: Position
```

---

# Static Type Checking with mypy

`mypy` checks typing without running the code.

## Run mypy

```bash
mypy .
```

---

# Common mypy Errors

## Missing return statement

```python
def get_value() -> int:
    pass
```

---

## Incompatible types

```python
age: int = "hello"
```

---

# Best Practices

- Avoid unnecessary `Any`
- Use precise types
- Use `Optional` when needed
- Keep function return types explicit
- Prefer readable typing over overly complex typing

---

# Summary Table

| Typing Feature | Purpose |
|---|---|
| list[str] | List of strings |
| dict[str, int] | Dictionary with string keys and integer values |
| tuple[int, int] | Tuple with two integers |
| Optional[T] | Type or None |
| Union[A, B] | Multiple possible types |
| Any | Disables type checking |
| Callable | Function as a type |

---

# Final Notes

Typing is not only about satisfying `mypy`.

Good typing:
- documents code
- improves maintainability
- helps teamwork
- reduces bugs
- makes large projects easier to manage

---
