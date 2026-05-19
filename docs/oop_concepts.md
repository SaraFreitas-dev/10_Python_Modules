# Object-Oriented Programming (OOP) Concepts

A beginner-friendly guide to the main Object-Oriented Programming concepts used in Python.

This document explains:
- Classes
- Objects
- Inheritance
- Encapsulation
- Polymorphism
- Abstraction
- Composition vs Inheritance

These concepts are heavily used in:
- game development
- APIs
- large Python applications
- design patterns
- 42 Python modules

---

# What is OOP?

Object-Oriented Programming (OOP) is a programming style based on objects.

Objects:
- store data
- contain behavior
- interact with each other

OOP helps organize large projects into reusable and maintainable structures.

---

# Classes

A class is a blueprint for creating objects.

---

# Example

```python
class Duck:

    def quack(self) -> None:
        print("Quack!")
```

---

# Creating an Object

```python
duck = Duck()

duck.quack()
```

Output:

```text
Quack!
```

---

# Attributes

Attributes store data inside objects.

---

# Example

```python
class Player:

    def __init__(self, name: str) -> None:
        self.name = name
```

---

# __init__()

`__init__()` is called automatically when an object is created.

It initializes the object attributes.

---

# Creating the Object

```python
player = Player("Sara")
```

---

# Accessing Attributes

```python
print(player.name)
```

Output:

```text
Sara
```

---

# Methods

Methods are functions inside classes.

---

# Example

```python
class Enemy:

    def attack(self) -> None:
        print("Enemy attacks!")
```

---

# Inheritance

Inheritance allows one class to reuse another class.

A child class inherits:
- attributes
- methods
- behavior

from a parent class.

---

# Example

```python
class Animal:

    def speak(self) -> None:
        print("Some sound")


class Dog(Animal):

    def bark(self) -> None:
        print("Woof!")
```

---

# Using Inheritance

```python
dog = Dog()

dog.speak()
dog.bark()
```

Output:

```text
Some sound
Woof!
```

---

# Why Use Inheritance?

Inheritance:
- reduces duplicated code
- improves organization
- allows shared behavior

---

# Overriding Methods

Child classes can replace parent behavior.

---

# Example

```python
class Animal:

    def speak(self) -> None:
        print("Animal sound")


class Cat(Animal):

    def speak(self) -> None:
        print("Meow")
```

---

# Result

```python
cat = Cat()

cat.speak()
```

Output:

```text
Meow
```

This is called method overriding.

---

# Polymorphism

Polymorphism means:
- different objects
- same method name
- different behavior

---

# Example

```python
class Dog:

    def speak(self) -> None:
        print("Woof")


class Cat:

    def speak(self) -> None:
        print("Meow")
```

---

# Using Polymorphism

```python
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

Output:

```text
Woof
Meow
```

Same method:
- different implementations

---

# Encapsulation

Encapsulation means protecting internal object data.

Objects should control access to their own state.

---

# Protected Attributes

Convention:
- `_name`

Means:
- "internal use"
- should not be modified directly

---

# Private Attributes

Convention:
- `__name`

Makes direct access harder.

---

# Example

```python
class BankAccount:

    def __init__(self) -> None:
        self.__balance = 0
```

---

# Access Problem

```python
account = BankAccount()

print(account.__balance)
```

This raises an error.

---

# Controlled Access

Use methods instead.

---

# Example

```python
class BankAccount:

    def __init__(self) -> None:
        self.__balance = 0

    def deposit(self, amount: int) -> None:
        self.__balance += amount

    def get_balance(self) -> int:
        return self.__balance
```

---

# Abstraction

Abstraction hides implementation details.

The user interacts with:
- simple interfaces
- not internal complexity

---

# Example

```python
class CoffeeMachine:

    def make_coffee(self) -> None:
        print("Making coffee...")
```

The user:
- presses a button
- does not care about internal machine logic

---

# Abstract Classes

Python supports abstract classes using `ABC`.

---

# Example

```python
from abc import ABC, abstractmethod


class Creature(ABC):

    @abstractmethod
    def attack(self) -> None:
        pass
```

---

# Child Implementation

```python
class Dragon(Creature):

    def attack(self) -> None:
        print("Fire breath!")
```

---

# Why Use Abstraction?

Abstraction:
- forces structure
- improves consistency
- defines required behavior

Very useful in:
- game systems
- factories
- APIs
- strategy patterns

---

# Composition

Composition means:
- objects contain other objects

Instead of inheriting behavior.

---

# Example

```python
class Engine:

    def start(self) -> None:
        print("Engine started")


class Car:

    def __init__(self) -> None:
        self.engine = Engine()
```

---

# Using Composition

```python
car = Car()

car.engine.start()
```

---

# Composition vs Inheritance

## Inheritance

Represents:
- "is-a" relationship

Example:

```text
Dog is an Animal
```

---

## Composition

Represents:
- "has-a" relationship

Example:

```text
Car has an Engine
```

---

# Which is Better?

Composition is often safer and more flexible.

Inheritance is useful when:
- behavior is truly shared

Composition is useful when:
- objects collaborate together

---

# Real 42 Examples

## Inheritance

```python
class Enemy(GameObject):
```

---

## Composition

```python
class Game:
    self.player = Player()
```

---

## Polymorphism

```python
enemy.attack()
boss.attack()
```

Different enemies:
- same method
- different behavior

---

# Common OOP Benefits

- Better code organization
- Reusability
- Easier maintenance
- Cleaner architecture
- Scalability for large projects

---

# Common OOP Problems

Bad OOP design may cause:
- overly deep inheritance trees
- tightly coupled systems
- hard debugging
- unnecessary complexity

---

# Best Practices

- Prefer composition over excessive inheritance
- Keep classes focused on one responsibility
- Use meaningful class names
- Avoid giant classes
- Encapsulate sensitive data
- Use abstraction for shared interfaces

---

# Summary Table

| Concept | Meaning |
|---|---|
| Class | Blueprint for objects |
| Object | Instance of a class |
| Inheritance | Reuse behavior from another class |
| Encapsulation | Protect internal data |
| Polymorphism | Same method, different behavior |
| Abstraction | Hide implementation details |
| Composition | Objects containing objects |

---

# Final Notes

OOP is one of the most important programming paradigms in Python.

Understanding these concepts helps when building:
- games
- MLX projects
- APIs
- parsers
- large applications
- design pattern systems

Strong OOP foundations make code:
- cleaner
- safer
- easier to scale

---
