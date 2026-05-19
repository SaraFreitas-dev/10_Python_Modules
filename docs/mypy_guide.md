# mypy and flake8 Guide

A beginner-friendly guide to static analysis tools commonly used in Python projects.

This document explains:
- mypy
- flake8
- line too long
- unused imports
- indentation problems
- naming conventions
- common errors in 42 projects

These tools help improve:
- code quality
- readability
- maintainability
- type safety

---

# What is mypy?

`mypy` is a static type checker for Python.

It checks:
- type hints
- return types
- Optional issues
- invalid assignments
- typing consistency

mypy analyzes code WITHOUT running it.

---

# Example

```python
def add(a: int, b: int) -> int:
    return a + b
```

Correct typing:
- parameters are integers
- return value is integer

---

# Example Error

```python
age: int = "hello"
```

mypy error:

```text
Incompatible types in assignment
```

---

# Running mypy

```bash
mypy .
```

---

# Common mypy Errors

---

# Missing Return Statement

## Example

```python
def get_name() -> str:
    print("Sara")
```

Problem:
- function says it returns `str`
- but returns nothing

---

# Fix

```python
def get_name() -> str:
    return "Sara"
```

---

# Optional Problems

## Example

```python
from typing import Optional

name: Optional[str] = None

print(name.upper())
```

Possible problem:
- `name` may be `None`

---

# Fix

```python
if name is not None:
    print(name.upper())
```

---

# Incompatible Types

## Example

```python
numbers: list[int] = ["hello"]
```

mypy error:
- expected integer
- received string

---

# What is flake8?

`flake8` is a style and linting tool.

It checks:
- formatting
- style problems
- unused imports
- indentation
- naming conventions

flake8 improves readability and consistency.

---

# Running flake8

```bash
flake8 .
```

---

# line too long

One of the most common flake8 errors.

---

# Example Error

```text
E501 line too long
```

---

# Problem Example

```python
print("This is an extremely long line that exceeds the maximum allowed line length in flake8")
```

---

# Why This Matters

Long lines:
- reduce readability
- are harder to review
- look bad in terminals

---

# Fix

Split the line.

---

# Example Fix

```python
print(
    "This is an extremely long line "
    "that was split correctly"
)
```

---

# unused imports

Very common error.

---

# Example Error

```text
F401 'os' imported but unused
```

---

# Problem Example

```python
import os
```

If `os` is never used:
- flake8 complains

---

# Fix

Remove the import.

```python
# removed unused import
```

---

# Why This Matters

Unused imports:
- create clutter
- confuse developers
- slow large projects slightly

---

# indentation

Python depends on indentation.

Bad indentation causes:
- syntax errors
- readability problems

---

# Example Problem

```python
def hello():
print("Hello")
```

---

# Correct Version

```python
def hello():
    print("Hello")
```

---

# Recommended Indentation

PEP8 recommends:
- 4 spaces

Avoid:
- tabs mixed with spaces

---

# naming conventions

Python follows naming standards called:
- PEP8 naming conventions

---

# Variables and Functions

Use:

```python
snake_case
```

---

# Good Example

```python
player_name = "Sara"

def calculate_score():
    pass
```

---

# Bad Example

```python
PlayerName = "Sara"

def CalculateScore():
    pass
```

---

# Classes

Use:

```python
PascalCase
```

---

# Good Example

```python
class SpaceStation:
    pass
```

---

# Constants

Use:

```python
UPPER_CASE
```

---

# Example

```python
WINDOW_WIDTH = 1920
```

---

# Why Naming Matters

Good naming:
- improves readability
- explains intent
- helps teamwork
- simplifies debugging

---

# Common 42 flake8 Problems

| Error | Meaning |
|---|---|
| E501 | line too long |
| F401 | unused import |
| E302 | expected blank lines |
| E305 | expected blank line after function |
| W293 | blank line contains whitespace |

---

# Example: Blank Line Error

Problem:

```python
def hello():
    print("Hi")
def bye():
    print("Bye")
```

---

# Fix

```python
def hello():
    print("Hi")


def bye():
    print("Bye")
```

---

# Strict mypy Mode

Many projects use:

```bash
mypy . --strict
```

This enables:
- stricter checks
- stronger typing rules

---

# Common Strict Errors

- missing annotations
- missing return types
- Any usage
- Optional problems

---

# Example

```python
def add(a, b):
    return a + b
```

Strict mode complains because:
- parameters are untyped

---

# Fix

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

# Good Workflow

Run both tools regularly:

```bash
flake8 .
mypy .
```

---

# Why Use Both?

## flake8

Focuses on:
- style
- formatting
- readability

---

## mypy

Focuses on:
- typing
- logic consistency
- type safety

---

# Recommended 42 Workflow

1. Write code
2. Run program
3. Run flake8
4. Run mypy
5. Fix warnings immediately

---

# Best Practices

- Keep lines short
- Remove unused imports
- Use meaningful names
- Type all functions
- Avoid unnecessary Any
- Keep formatting consistent
- Run tools frequently

---

# Summary Table

| Tool | Purpose |
|---|---|
| mypy | Static type checking |
| flake8 | Style and linting |
| E501 | Line too long |
| F401 | Unused import |
| snake_case | Variable/function naming |
| PascalCase | Class naming |

---

# Final Notes

mypy and flake8 are extremely important in professional Python development.

These tools help create:
- cleaner code
- safer projects
- better teamwork
- easier debugging
- more maintainable applications

They are especially valuable in:
- 42 projects
- large Python applications
- APIs
- parsers
- game engines
- backend systems

---
