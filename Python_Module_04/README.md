# 🛡️ Python Module 04 — Cyber Archives: Secure File Systems

This project is part of the **42 School Common Core** and focuses on
**secure file handling, permissions, and crisis response** in Python.

This module introduces the concepts required to safely interact with 
the file system while anticipating and responding to failure scenarios.

Using the **Cyber Archives** theme, this module simulates real-world
high-security data vaults, where archives may be missing, restricted,
corrupted, or fully accessible — and must always be handled safely.

The goal of this module is to understand and apply:
- file opening modes and safe file access
- context managers (`with`) for automatic resource handling
- file system exceptions (`FileNotFoundError`, `PermissionError`)
- secure read and write operations
- system-level error detection and response
- defensive programming for file-based systems
- resilient crisis response design

Each exercise incrementally builds on the previous one, culminating in a
complete **crisis response system** that handles multiple failure scenarios
without crashing.

---

## 📁 Project Structure

Each exercise is placed in its own directory (`ex0` to `ex4`) and contains
only the files requested by the subject.

```bash
ex0/ → Ancient Archive Recovery
ex1/ → Archive Creation & Preservation
ex2/ → Stream Communication System
ex3/ → Secure Vault Operations
ex4/ → Crisis Response System
```
---

## 📌 Exercises Overview

### **Exercise 0 — Ancient Archive Recovery**
Introduces safe file reading.
- Opens and reads archive files
- Handles missing files gracefully
- Ensures proper file closure

**Concepts:** `open`, `with`, `FileNotFoundError`

---

### **Exercise 1 — Archive Creation & Preservation**
Focuses on controlled file writing.
- Creates new archive files
- Writes structured data safely
- Prevents accidental data loss

**Concepts:** write modes, safe file writing, data preservation

---

### **Exercise 2 — Stream Communication System**
Explores standard input and output streams.
- Reads user input from stdin
- Writes system messages to stdout and stderr
- Simulates multi-channel communication

**Concepts:** `input`, `sys.stdout`, `sys.stderr`, streams

---

### **Exercise 3 — Secure Vault Operations**
Demonstrates secure access to classified data.
- Reads protected archive content
- Appends new classified entries
- Confirms successful preservation

**Concepts:** context managers, append mode, secure file access

---

### **Exercise 4 — Crisis Response System**
Integrates all previous concepts into a resilient system.
- Detects missing, restricted, and valid archives
- Handles file system exceptions correctly
- Responds to crises without crashing

**Concepts:** exception dispatching, system recovery

---

## 🧪 Test Files

Test and simulation files are provided in the 
***data-generator-tools folder*** to validate file access,
permissions, and crisis response behavior.

These files are used exclusively for testing and are not part of the
core application logic.

---

## ✅ Notes

- Written for **Python 3.10+**
- Fully compliant with **flake8**
- Follows **42 naming conventions**
- Uses only authorized functions
- Outputs match the subject examples
- Programs never crash, even during crisis scenarios

---

## 🔐 Final Thoughts

This module focuses on a critical real-world skill:
**interacting safely with the file system under failure conditions**.

Rather than assuming files are always accessible, the goal is to
**anticipate errors, respond securely, and maintain system stability**.

