# 💊 Python Module 08 — The Matrix: Data Engineering Foundations

This project is part of the **42 School Common Core** and focuses on  
**real-world Python development practices used in data engineering**.

Building on previous modules, this project introduces essential tools for  
**environment isolation, dependency management, and configuration handling**.

The goal of this module is to understand and apply:
- virtual environments (`venv`)
- dependency management (`pip` vs `Poetry`)
- external libraries (pandas, numpy, matplotlib, requests)
- dynamic imports and dependency checks
- environment variables and `.env` configuration
- secure handling of sensitive data
- real-world project structure

Each exercise simulates a real-world scenario, resulting in a  
basic but complete **data pipeline system**.

---

## 📚 Table of Contents

## 📚 Table of Contents

- 🧱 [Exercise 0 - Entering the Matrix](#exercise-0--entering-the-matrix)  
  *Understanding virtual environments and Python runtime isolation*

- 📦 [Exercise 1 - Loading Programs](#exercise-1--loading-programs)  
  *Managing dependencies and building a basic data analysis pipeline*

- 🔐 [Exercise 2 - Accessing the Mainframe](#exercise-2--accessing-the-mainframe)  
  *Secure configuration using environment variables and .env files*

---

## 📁 Project Structure


```bash

ex0/
└── construct.py

ex1/
├── loading.py
├── requirements.txt
└── pyproject.toml

ex2/
├── oracle.py
├── .env.example
└── .gitignore

```


---

## 📌 Exercises Overview

### **Exercise 0 — Entering the Matrix**
Introduces virtual environments.

- Detects if running inside a virtual environment
- Displays Python environment information
- Shows differences between global and isolated environments
- Provides instructions to create a `venv`

**Concepts:** environment isolation, system paths, Python runtime  
👉 Based on detecting `VIRTUAL_ENV` and system paths :contentReference[oaicite:0]{index=0}

---

### **Exercise 1 — Loading Programs**
Focuses on dependency management and data processing.

- Checks installed dependencies dynamically
- Supports both `pip` and `Poetry`
- Uses:
  - `numpy` → data generation
  - `pandas` → data manipulation
  - `matplotlib` → visualization
  - `requests` (optional)
- Generates a dataset and saves a graph (`matrix_analysis.png`)

**Concepts:** package management, dynamic imports, data pipelines  
👉 Dependency checking implemented via `importlib` 
👉 Requirements defined in `requirements.txt`

---

### **Exercise 2 — Accessing the Mainframe**
Introduces environment configuration and security.

- Loads variables from `.env`
- Uses `python-dotenv`
- Handles:
  - `MATRIX_MODE`
  - `DATABASE_URL`
  - `API_KEY`
  - `LOG_LEVEL`
  - `ZION_ENDPOINT`
- Demonstrates dev vs production behavior
- Ensures secrets are not hardcoded

**Concepts:** environment variables, secure config, system design  
👉 Configuration loading handled safely with fallback and validation

---

## ⚙️ Key Learning Points

- Virtual environments isolate your projects from global Python
- Dependency management is critical in real-world applications
- `pip` and `Poetry` solve the same problem differently
- External libraries must be handled safely (missing deps, versions)
- `.env` files prevent exposing sensitive data
- Environment variables override local configuration
- Clean configuration = secure and scalable systems

---

## 🔐 Security & Best Practices

- Never commit `.env` files - use `.gitignore` (this project includes a .env.example for practice purposes only)
- Always validate required environment variables
- Avoid hardcoding secrets in your code
- Provide fallback behavior for missing dependencies
- Separate development and production configurations

---

## ✅ Notes

- Written for **Python 3.10+**
- Uses **type hints** and follows **flake8**
- Designed to work **with and without dependencies installed**
- Handles errors gracefully (missing packages / config)
- Focus is on **real-world practices, not algorithm complexity**
- Outputs match the subject expectations