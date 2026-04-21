# 🧪 Python Module 09 — The Observatory: Data Validation Systems

This project is part of the **42 School Common Core** and focuses on  
**data validation, structured modeling, and business rule enforcement** using Python.

Building on previous modules, this project introduces advanced concepts such as  
**data validation frameworks, schema enforcement, and real-world data integrity rules**.

The goal of this module is to understand and apply:

- data modeling with `pydantic`
- field validation using constraints (`Field`)
- advanced validation using `@model_validator`
- handling complex data relationships (nested models)
- enum usage for controlled values
- error handling and validation feedback
- clean architecture for data pipelines

Each exercise simulates a real-world system where **data must be validated before use**,  
resulting in a robust **data validation pipeline**.

---

## 📚 Table of Contents

- 🛰️ [Exercise 0 - Space Station Validation](#exercise-0--space-station-validation)  
  *Basic data validation with constraints*

- 👽 [Exercise 1 - Alien Contact Protocol](#exercise-1--alien-contact-protocol)  
  *Advanced validation rules and conditional logic*

- 🚀 [Exercise 2 - Space Mission Control](#exercise-2--space-mission-control)  
  *Complex nested validation and business rules*

---

## 📁 Project Structure

```bash
ex0/
└── space_station.py

ex1/
└── alien_contact.py

ex2/
└── space_crew.py
```

## 📌 Exercises Overview

### **Exercise 0 — Space Station Validation**

Introduces structured data validation using `Pydantic` models.

- Defines a `SpaceStation` model
- Validates fields using:
  - string length constraints
  - numeric ranges (`ge`, `le`)
- Uses default values and optional fields
- Handles validation errors safely

**Concepts:** data validation, schema definition, field constraints  
👉 Built using `BaseModel` and `Field`

---

### **Exercise 1 — Alien Contact Protocol**

Focuses on advanced validation logic and conditional rules.

- Introduces `Enum` for controlled values (`ContactType`)
- Implements complex validation using `@model_validator`
- Applies rules such as:
  - ID format enforcement
  - conditional validation based on contact type
  - cross-field dependency validation

**Concepts:** business logic validation, enums, conditional constraints  
👉 Uses `@model_validator(mode="after")` for full-object validation

---

### **Exercise 2 — Space Mission Control**

Implements nested models and complex validation scenarios.

- Defines multiple models:
  - `CrewMember`
  - `SpaceMission`
- Uses nested data structures (`list[CrewMember]`)
- Validates:
  - crew composition (roles required)
  - experience distribution
  - mission constraints based on duration
  - active status of crew members

**Concepts:** nested validation, aggregation rules, system integrity  
👉 Demonstrates real-world data validation pipelines

---

## ⚙️ Key Learning Points

- `pydantic` simplifies robust data validation
- Data integrity must be enforced at model level
- Validation can go beyond fields into full object logic
- Enums prevent invalid categorical data
- Nested models reflect real-world structured data
- Clean validation logic improves maintainability

---

## 🔐 Best Practices

- Always validate external or user-provided data
- Use clear and explicit constraints (`Field`)
- Keep validation logic readable and separated
- Avoid side effects (like `print`) in validation functions
- Prefer returning validated objects instead of raw data
- Handle validation errors gracefully

---

## ✅ Notes

- Written for **Python 3.10+**
- Uses **type hints** and follows **flake8**
- Focuses on **data integrity and validation patterns**
- Designed to simulate **real-world backend/data engineering scenarios**
- Outputs match the subject expectations