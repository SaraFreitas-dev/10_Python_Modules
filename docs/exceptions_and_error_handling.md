# Exceptions and Error Handling in Python

A beginner-friendly guide to Python exceptions and error handling.

This document explains:
- try
- except
- finally
- custom exceptions
- common exceptions
- good practices

Error handling is extremely important in:
- parsing projects
- APIs
- file management
- game systems
- user input validation
- large applications

---

# What is an Exception?

An exception is an error that happens while the program is running.

If exceptions are not handled:
- the program crashes

---

# Example of an Exception

```python
number = int("hello")
```

Output:

```text
ValueError
```

Because `"hello"` cannot be converted into an integer.

---

# try / except

`try` allows Python to test code that may fail.

`except` catches the error and prevents the program from crashing.

---

# Basic Example

```python
try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid number")
```

---

# Flow Explanation

1. Python enters the `try` block
2. If no error happens:
   - code continues normally
3. If an error happens:
   - execution jumps to `except`

---

# Catching Multiple Exceptions

---

# Example

```python
try:
    value = numbers[10]
    number = int("hello")

except IndexError:
    print("Invalid index")

except ValueError:
    print("Invalid conversion")
```

---

# Catching Multiple Errors Together

```python
try:
    ...
except (ValueError, TypeError):
    print("Invalid data")
```

---

# Accessing the Exception Object

Use `as e` to inspect the error.

---

# Example

```python
try:
    number = int("hello")

except ValueError as e:
    print(e)
```

Output:

```text
invalid literal for int()
```

---

# finally

`finally` always executes.

Even if:
- an exception happens
- the function returns early

---

# Example

```python
try:
    file = open("data.txt")

except FileNotFoundError:
    print("File not found")

finally:
    print("Closing program")
```

---

# Why Use finally?

Useful for cleanup operations:
- closing files
- freeing resources
- disconnecting sockets
- stopping systems

---

# else

`else` runs only if no exception happens.

---

# Example

```python
try:
    number = int("42")

except ValueError:
    print("Invalid number")

else:
    print("Conversion successful")
```

---

# Common Python Exceptions

| Exception | Meaning |
|---|---|
| ValueError | Invalid value |
| TypeError | Invalid type |
| IndexError | Invalid list index |
| KeyError | Missing dictionary key |
| FileNotFoundError | File does not exist |
| ZeroDivisionError | Division by zero |
| AttributeError | Object missing attribute |

---

# Custom Exceptions

Custom exceptions allow developers to create meaningful project-specific errors.

Very useful in:
- parsers
- validation systems
- game engines
- APIs

---

# Basic Custom Exception

```python
class ParserError(Exception):
    pass
```

---

# Raising Exceptions

Use `raise` to trigger an exception.

---

# Example

```python
if not config_file.endswith(".txt"):
    raise ParserError("Invalid config file")
```

---

# Catching Custom Exceptions

```python
try:
    parse_config()

except ParserError as e:
    print(e)
```

---

# Real Parsing Example

```python
class ConfigError(Exception):
    pass


def parse_width(value: str) -> int:

    if not value.isdigit():
        raise ConfigError("WIDTH must be numeric")

    return int(value)
```

---

# Why Custom Exceptions Matter

Custom exceptions:
- improve debugging
- create cleaner code
- provide meaningful errors
- separate project logic from Python internal errors

---

# Re-raising Exceptions

Sometimes you want to:
- log the error
- then raise it again

---

# Example

```python
try:
    parse_file()

except ValueError as e:
    print("Logging error...")
    raise
```

---

# Avoid Bare except

Bad practice:

```python
except:
    print("Something failed")
```

Why bad?
- hides unexpected errors
- makes debugging difficult

---

# Better Practice

```python
except ValueError:
    print("Invalid value")
```

Catch only expected exceptions.

---

# Good Error Messages

Bad:

```python
raise ValueError("Error")
```

Better:

```python
raise ValueError("WIDTH must be greater than 0")
```

Clear messages improve debugging.

---

# Error Handling in Parsing Projects

Parsing systems must:
- validate input
- detect invalid formats
- avoid crashes
- provide meaningful messages

---

# Example Config Parser

```python
def parse_line(line: str) -> tuple[str, str]:

    if "=" not in line:
        raise ValueError("Missing '=' separator")

    key, value = line.split("=")

    return key, value
```

---

# Nested try / except

Python supports nested error handling.

---

# Example

```python
try:

    try:
        number = int("hello")

    except ValueError:
        print("Inner error")

except Exception:
    print("Outer error")
```

---

# Exception Hierarchy

All exceptions inherit from:

```python
Exception
```

Custom exceptions usually inherit from:
- `Exception`

---

# Common 42 Examples

## Parsing

```python
raise ConfigError("Duplicate key")
```

---

## Maze Validation

```python
raise MazeError("Path could not be found")
```

---

## File Handling

```python
raise FileNotFoundError("Map file missing")
```

---

# Best Practices

- Catch only expected exceptions
- Use meaningful error messages
- Prefer custom exceptions for project logic
- Avoid giant try blocks
- Keep error handling readable
- Never silently ignore exceptions

---

# Bad Practice Example

```python
try:
    ...
except:
    pass
```

This hides bugs and should usually be avoided.

---

# Good Practice Example

```python
try:
    config = load_config()

except FileNotFoundError:
    print("Config file missing")

except ConfigError as e:
    print(e)
```

---

# Summary Table

| Keyword | Purpose |
|---|---|
| try | Executes risky code |
| except | Catches exceptions |
| finally | Always executes |
| else | Executes if no error happens |
| raise | Triggers an exception |
| Exception | Base exception class |

---

# Final Notes

Good error handling is one of the most important parts of software development.

Strong exception handling:
- prevents crashes
- improves debugging
- creates safer applications
- improves user experience
- makes projects easier to maintain

Error handling becomes especially important in:
- parsers
- games
- APIs
- networking
- file systems
- large applications

---
