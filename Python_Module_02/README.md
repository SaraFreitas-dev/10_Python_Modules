# 🌿 Python Module 02 — Garden Guardian: Error Handling Systems

This project is part of the **42 School Common Core** and focuses on
**exception handling and defensive programming** in Python.

Building on the object-oriented foundations from **Module 01**, this module
introduces the concepts required to build **robust and resilient systems**
that can handle errors gracefully without crashing.

Using the **Garden Guardian** theme, this module simulates real-world
agricultural data systems where failures are expected — and must be handled
correctly.

The goal of this module is to understand and apply:
- Python exception handling (`try`, `except`, `finally`, `raise`)
- built-in exception types
- custom exception classes
- error categorization and recovery
- defensive programming principles
- clean resource management
- resilient system design

Each exercise incrementally builds on the previous one, culminating in a
complete **garden management system** that integrates all concepts.

---

## 📁 Project Structure

Each exercise is placed in its own directory (`ex0` to `ex5`) and contains
only the files requested by the subject.

```bash
ex0/ → Agricultural Data Validation Pipeline
ex1/ → Different Types of Problems
ex2/ → Custom Error Types
ex3/ → Finally Block & Resource Cleanup
ex4/ → Raising Your Own Errors
ex5/ → Garden Management System
```


---

## 📌 Exercises Overview

### **Exercise 0 — Agricultural Data Validation Pipeline**
Introduces basic exception handling.
- Converts string input to numbers
- Validates temperature ranges
- Handles invalid and extreme inputs

**Concepts:** `try/except`, `ValueError`, input validation

---

### **Exercise 1 — Different Types of Problems**
Explores common built-in Python exceptions.
- Demonstrates multiple error types
- Handles each error appropriately
- Shows program continuation after failures

**Concepts:** multiple exception types, grouped exception handling

---

### **Exercise 2 — Making Your Own Error Types**
Introduces custom exception classes.
- Creates garden-specific error types
- Uses inheritance to group related errors
- Demonstrates catching parent exceptions

**Concepts:** custom exceptions, inheritance, error hierarchy

---

### **Exercise 3 — Finally Block: Always Clean Up**
Focuses on guaranteed cleanup logic.
- Simulates a watering system
- Ensures cleanup happens even on errors
- Demonstrates `finally` behavior

**Concepts:** `finally`, resource management, defensive cleanup

---

### **Exercise 4 — Raising Your Own Errors**
Introduces proactive error signaling.
- Validates plant health parameters
- Raises appropriate errors when invalid
- Handles raised errors gracefully

**Concepts:** `raise`, validation logic, meaningful error messages

---

### **Exercise 5 — Garden Management System**
Integrates all previous concepts into one system.
- Manages plants and watering operations
- Uses custom garden exceptions
- Handles errors without crashing
- Demonstrates system recovery

**Concepts:** system integration, fault tolerance, resilient design

---

## ✅ Notes

- Written for **Python 3.10+**
- Fully compliant with **flake8**
- Follows **42 naming conventions**
- Uses only authorized functions
- Outputs match the subject examples
- Programs never crash, even on errors

---

## 🌱 Final Thoughts

This module focuses on a core professional skill:
**writing code that survives failure**.

Rather than avoiding errors, the goal is to **anticipate, handle, and recover** from them — a critical mindset for building reliable real-world systems.

By the end of this module, the Garden Guardian system demonstrates how exception handling techniques work together to create robust,
maintainable, and fault-tolerant programs.
