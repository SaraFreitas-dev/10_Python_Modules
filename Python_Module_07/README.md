# 🎴 Module 07 - DataDeck

## 📖 Overview

This project is part of the 42 curriculum and focuses on advanced object-oriented programming concepts in Python.

The program simulates the creation and interaction of different creature types, allowing them to perform actions such as attacking, healing, transforming, and adapting their behavior during battles.

The goal is to build a flexible and extensible architecture, promoting clean design, separation of concerns, and dynamic behavior management.

## 📚 Table of Contents

- 🏭 [Exercise 0 - Creature Factory](#exercise-0---creature-factory)  
  *Creation of creature families using the Abstract Factory pattern*

- ⚙️ [Exercise 1 - Capabilities](#exercise-1---capabilities)  
  *Extending creatures with reusable behaviors through abstract capabilities*

- 🧠 [Exercise 2 - Abstract Strategy](#exercise-2---abstract-strategy)  
  *Dynamic battle behavior using the Strategy pattern*

---

# Exercise 0 - Creature Factory

## 📁 Directory Structure

```bash
ex0/
├── Creature.py          # Abstract Creature base class
├── CreatureFactory.py   # Abstract factory interface
├── FlameFactory.py      # Factory for Flame creatures
├── AquaFactory.py       # Factory for Aqua creatures
├── Flameling.py         # Base Flame creature
├── Pyrodon.py           # Evolved Flame creature
├── Aquabub.py           # Base Aqua creature
├── Torragon.py          # Evolved Aqua creature
└── __init__.py          # Exposes factory classes

battle.py                # Test script for creature creation & battles
```

---

## 📌 Description

This exercise introduces the **Abstract Factory design pattern** to create families of creatures.

### Creature (Abstract Class)
- Defines common attributes (`name`, `type`)
- Provides a concrete `describe()` method
- Declares an abstract `attack()` method

### Concrete Creatures
- `Flameling` / `Pyrodon` (Flame family)
- `Aquabub` / `Torragon` (Aqua family)
- Each implements its own attack behavior

### CreatureFactory (Abstract Class)
- Defines methods to create:
  - base creature
  - evolved creature

### Concrete Factories
- `FlameFactory` → creates `Flameling` and `Pyrodon`
- `AquaFactory` → creates `Aquabub` and `Torragon`

### battle.py
- Tests factory creation
- Demonstrates polymorphism (`describe()` + `attack()`)
- Simulates a simple battle between creatures

---

## Notes

- The `ex0` package does **not expose concrete Creature classes directly**
- Only factory classes are exposed to ensure proper **encapsulation**
- This design allows easy extension with new creature families without modifying existing code

# Exercise 1 - Capabilities

## 📁 Directory Structure

```bash
ex1/
├── HealCapability.py            # Heal capability interface
├── TransformCapability.py       # Transform capability interface
├── Sproutling.py                # Base healing creature
├── Bloomelle.py                 # Evolved healing creature
├── Shiftling.py                 # Base transform creature
├── Morphagon.py                 # Evolved transform creature
├── HealingCreatureFactory.py    # Factory for healing creatures
├── TransformCreatureFactory.py  # Factory for transform creatures
└── __init__.py                  # Exposes factory classes

capacitor.py                     # Test script demonstrating capabilities
```

---

## 📌 Description

This exercise extends the creature system by introducing **capabilities** using abstract classes.

Instead of modifying the base `Creature`, new behaviors are added through **separate capability classes**, promoting flexibility and reuse.

### Capabilities

#### HealCapability
- Defines the `heal()` abstract method
- Implemented by healing creatures
- Returns a string describing the healing action

#### TransformCapability
- Defines:
  - `transform()`
  - `revert()`
- Uses an internal state to modify behavior dynamically
- Impacts how `attack()` behaves

---

### Healing Creatures

- `Sproutling` (base)
  - Basic attack
  - Heals itself for a small amount

- `Bloomelle` (evolved)
  - Stronger attack
  - Heals itself and others for a large amount

---

### Transform Creatures

- `Shiftling` (base)
  - Normal attack by default
  - Can transform to enhance attack
  - Reverts to original state

- `Morphagon` (evolved)
  - More powerful transformed attack
  - Uses the same transform/revert cycle with stronger effects

---

### Factories

#### HealingCreatureFactory
- Creates:
  - `Sproutling` (base)
  - `Bloomelle` (evolved)

#### TransformCreatureFactory
- Creates:
  - `Shiftling` (base)
  - `Morphagon` (evolved)

---

### capacitor.py

- Tests healing creatures:
  - describe → attack → heal

- Tests transform creatures:
  - describe → attack → transform → attack → revert

- Demonstrates dynamic behavior based on capabilities

---

## Notes

- Capabilities are implemented as **independent abstract classes**
- They do **not inherit from Creature**, enabling composition
- Behavior is extended without modifying the base class
- Output must strictly match the subject requirements

---

# Exercise 2 - Abstract Strategy

## 📁 Directory Structure

```bash
ex2/
├── BattleStrategy.py       # Abstract BattleStrategy interface
├── NormalStrategy.py       # Strategy for basic attack behavior
├── DefensiveStrategy.py    # Strategy for attack + heal behavior
├── AggressiveStrategy.py   # Strategy for transform + attack + revert behavior
└── __init__.py             # Exposes strategy classes

tournament.py               # Test script simulating battles with strategies
```

---

## 📌 Description

This exercise introduces the **Strategy design pattern** to control how creatures behave during battles.

Instead of hardcoding behavior inside the creatures, actions are delegated to **strategy objects**, allowing dynamic behavior selection at runtime.

---

### BattleStrategy (Abstract Class)

- Defines two methods:
  - `is_valid(creature) -> bool`
  - `act(creature) -> str or None`

- `is_valid` ensures the strategy is compatible with the creature  
- `act` defines how the creature behaves in battle

---

### Concrete Strategies

#### NormalStrategy
- Valid for all creatures
- Behavior:
  - Performs a standard `attack()`

---

#### AggressiveStrategy
- Valid only for creatures with transform capability
- Behavior:
  - `transform()` → `attack()` → `revert()`

---

#### DefensiveStrategy
- Valid only for creatures with healing capability
- Behavior:
  - `attack()` → `heal()`

---

### Exception Handling

- If a strategy is used with an incompatible creature:
  - `is_valid()` returns `False`
  - Calling `act()` raises a custom exception

---

### tournament.py

- Creates multiple creatures using factories (from ex0 and ex1)
- Assigns a strategy to each creature
- Simulates a tournament:
  - Each creature fights all others
  - Strategy determines behavior during combat
- Handles invalid strategy-creature combinations safely

---

## Notes

- The Strategy pattern allows behavior to change **without modifying creature classes**
- Eliminates conditional logic (`if transform`, `if heal`, etc.)
- Promotes flexibility and scalability
- Works together with:
  - Factory pattern (object creation)
  - Capability pattern (behavior composition)

- Output and error handling must strictly match the subject requirements