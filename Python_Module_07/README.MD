# Module 07 - DataDeck

## Table of Contents

- [Exercise 0 - Creature Factory](#exercise-0---creature-factory)
- [Exercise 1 - Capabilities](#exercise-1---capabilities)
- [Exercise 2 - Abstract Strategy](#exercise-2---abstract-strategy)


# Exercise 0 - Creature Factory

## Directory Structure

- `ex0/` - Creature system package (abstract factory pattern)
- `ex0/creature.py` - Defines the abstract `Creature` base class
- `ex0/flame_creatures.py` - Contains Flame family creatures (`Flameling`, `Pyrodon`)
- `ex0/aqua_creatures.py` - Contains Aqua family creatures (`Aquabub`, `Torragon`)
- `ex0/factories.py` - Implements `CreatureFactory` and concrete factories (`FlameFactory`, `AquaFactory`)
- `ex0/__init__.py` - Exposes only factory classes (encapsulation)
- `battle.py` - Test script to validate factories and simulate battles

---

## Description

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

## Directory Structure

- `ex1/` - Capability system package (composition with abstract classes)
- `ex1/capabilities.py` - Defines capability interfaces (`HealCapability`, `TransformCapability`)
- `ex1/healing_creatures.py` - Contains healing family creatures (`Sproutling`, `Bloomelle`)
- `ex1/transform_creatures.py` - Contains transform family creatures (`Shiftling`, `Morphagon`)
- `ex1/factories.py` - Implements capability-based factories (`HealingCreatureFactory`, `TransformCreatureFactory`)
- `ex1/__init__.py` - Exposes only factory classes
- `capacitor.py` - Test script demonstrating creature capabilities

---

## Description

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

# Exercise 1 - Capabilities

## Directory Structure

- `ex1/` - Capability system package (composition with abstract classes)
- `ex1/capabilities.py` - Defines capability interfaces (`HealCapability`, `TransformCapability`)
- `ex1/healing_creatures.py` - Contains healing family creatures (`Sproutling`, `Bloomelle`)
- `ex1/transform_creatures.py` - Contains transform family creatures (`Shiftling`, `Morphagon`)
- `ex1/factories.py` - Implements capability-based factories (`HealingCreatureFactory`, `TransformCreatureFactory`)
- `ex1/__init__.py` - Exposes only factory classes
- `capacitor.py` - Test script demonstrating creature capabilities

---

## Description

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