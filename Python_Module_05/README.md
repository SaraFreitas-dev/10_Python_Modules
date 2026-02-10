# 🌐 Python Module 05 — Nexus: Polymorphic Enterprise Pipelines

This project is part of the **42 School Common Core** and focuses on
**polymorphism, abstraction, and scalable system architecture** in Python.

Building on the typing, OOP, and data-processing foundations from previous
modules, this module introduces how to design **enterprise-grade systems**
where multiple components interact through **shared interfaces** rather than
hard-coded dependencies.

Using the **Nexus Pipeline System** theme, this module simulates a real-world
data processing platform capable of handling **multiple data formats** through
a unified and extensible architecture.

The goal of this module is to understand and apply:
- polymorphism and interface-driven design
- abstract base classes (`ABC`)
- structural subtyping with `Protocol`
- type-safe pipelines with full annotations
- separation of concerns via processing stages
- scalable and extensible system design
- clean orchestration of heterogeneous components

Each exercise incrementally builds toward a complete **multi-pipeline
enterprise system**.

---

## 📁 Project Structure

Each exercise is placed in its own directory (`ex0` to `ex2`) and contains
only the files requested by the subject.

The repository **also includes the official `main` test files provided by the
subject**, allowing direct validation against the expected behavior.

```bash
ex0/ → Data Processor Foundation
ex1/ → Polymorphic Streams
ex2/ → Nexus Integration (Enterprise Pipeline System)

main.py → Official subject test file (included for validation)
```

## 📌 Exercises Overview

### **Exercise 0 — Data Processor Foundation**

Introduces the core abstract structures used throughout the module.

- Defines base processors using abstract classes  
- Establishes a common processing interface  
- Demonstrates basic inheritance and method overriding  

**Concepts:** `ABC`, abstract methods, base class design

---

### **Exercise 1 — Polymorphic Streams**

Explores true polymorphic behavior across multiple data streams.

- Implements different stream types sharing the same interface  
- Processes heterogeneous data uniformly  
- Demonstrates runtime polymorphism in action  

**Concepts:** polymorphism, inheritance, shared interfaces

---

### **Exercise 2 — Nexus Integration**

Integrates all concepts into a full enterprise-style system.

- Builds configurable processing pipelines  
- Uses staged processing (Input → Transform → Output)  
- Orchestrates multiple pipelines through a central manager  
- Supports different data formats (JSON, CSV, Streams)  
- Demonstrates pipeline chaining and error recovery  

**Concepts:**  
polymorphism at scale, `Protocol`, complex inheritance,  
enterprise architecture, system orchestration

---

## ✅ Notes

- Written for **Python 3.10+**
- Fully type-annotated (**100% typing coverage**)
- Compliant with **flake8**
- Follows **42 naming conventions**
- Uses only authorized libraries
- Outputs match the subject examples
- Includes the **official subject `main` tests** for validation
- Designed to be extensible without modifying existing code

---

## 🌐 Final Thoughts

This module focuses on a core software engineering principle:  
**designing systems that grow without breaking**.

Rather than coupling components tightly, the Nexus system relies on  
**abstraction, contracts, and polymorphism** to allow new pipelines,  
new data formats, and new behaviors to be added safely.

By the end of this module, the Nexus Pipeline System demonstrates how  
clean architecture, strong typing, and polymorphism combine to produce  
**robust, scalable, and maintainable Python systems**.
