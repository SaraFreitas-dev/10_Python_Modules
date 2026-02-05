# 🎮 Python Module 03 — Data Quest: Mastering Python Collections

This project is part of the **42 School Common Core** and focuses on
**Python collections and data processing patterns** commonly used in
**data engineering and analytics systems**.

This module introduces the core Python data structures and shows how to
use them efficiently in **real-world, command-line–driven scenarios**.

Using the **Data Quest / Pixel Dimension** theme, this module simulates
a **game analytics platform** where large volumes of player data must be
processed, analyzed, and transformed using the right data structures.

The goal of this module is to understand and apply:
- command-line argument processing (`sys.argv`)
- lists for sequential data analytics
- tuples for immutable structured data
- sets for unique collections and comparisons
- dictionaries for structured and nested data
- generators for memory-efficient data streams
- comprehensions for elegant data transformation
- defensive programming with graceful error handling

---

## 📁 Project Structure

Each exercise is placed in its own directory (`ex0` to `ex6`) and contains
only the files requested by the subject.

Additional **testing and helper tools provided by 42** are located in
the `data_quest_tools/` directory.

## 📌 Exercises Overview

### **Exercise 0 — Command Quest**
Introduces command-line communication.
- Reads and analyzes `sys.argv`
- Handles cases with no input

**Concepts:** `sys.argv`, `len()`, command-line parsing

---

### **Exercise 1 — Score Cruncher**
Processes player scores using lists.
- Stores scores in lists
- Computes total, average, min, max, and range
- Handles invalid input gracefully

**Concepts:** lists, numeric aggregation, `try/except`

---

### **Exercise 2 — Position Tracker**
Works with immutable 3D coordinates.
- Stores positions as tuples `(x, y, z)`
- Calculates Euclidean distance
- Demonstrates tuple unpacking
- Handles parsing errors safely

**Concepts:** tuples, immutability, unpacking, math operations

---

### **Exercise 3 — Achievement Hunter**
Tracks unique achievements using sets.
- Ensures uniqueness
- Compares achievements between players
- Uses set operations for analytics

**Concepts:** sets, `union`, `intersection`, `difference`

---

### **Exercise 4 — Inventory Master**
Builds a structured inventory system.
- Stores data in dictionaries
- Uses nested structures
- Generates statistics and reports

**Concepts:** dictionaries, key-value mapping, nested data

---

### **Exercise 5 — Stream Wizard**
Introduces memory-efficient data processing.
- Implements generators with `yield`
- Processes large data streams
- Demonstrates constant memory usage

**Concepts:** generators, iteration, streaming data

---

### **Exercise 6 — Data Alchemist**
Combines all data structures using comprehensions.
- List, dict, and set comprehensions
- Produces a final analytics dashboard

**Concepts:** comprehensions, data transformation, integration

---

## 🛠️ Testing & Helper Tools (Provided by 42)

The `data_quest_tools/` directory contains official helper scripts:
- **`data_generator.py`** — Generates test data for all exercises
- **`exercise_0_help.py`** — `sys.argv` usage examples
- **`exercise_1_helper.py`** — Realistic score datasets
- **`advanced_data_helper.py`** — Complex test scenarios

---

## ✅ Notes

- Python **3.10+**
- **flake8** compliant
- Follows **42 conventions**
- Authorized functions only
- Outputs match subject examples
- Programs never crash on errors

---

## 🚀 Final Thoughts

This module shifts the focus from *learning Python* to
*thinking like a data engineer*.

By mastering collections, generators, and comprehensions, you learn to
process data efficiently and write clean, expressive code.

