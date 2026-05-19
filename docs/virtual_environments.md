# Python Virtual Environments Guide

A beginner-friendly guide to Python virtual environments and package management.

This document explains:
- venv
- activation
- pip
- requirements.txt
- Poetry
- PEP 668
- common problems in 42 School environments

Virtual environments are essential for modern Python development.

---

# What is a Virtual Environment?

A virtual environment is an isolated Python environment.

It allows each project to:
- have its own packages
- use different library versions
- avoid conflicts with system Python

Without virtual environments:
- projects may break each other
- package versions may conflict
- system Python can become unstable

---

# Why Use Virtual Environments?

Virtual environments help:
- isolate dependencies
- create reproducible projects
- avoid permission issues
- protect system Python
- simplify collaboration

---

# Creating a Virtual Environment

Python includes `venv` by default.

---

# Create venv

```bash
python3 -m venv venv
```

This creates a folder called:

```text
venv/
```

Containing:
- Python executable
- pip
- installed packages
- activation scripts

---

# Common Naming

Most projects use:

```text
venv/
```

Other common names:
- `.venv`
- `env`

---

# Activating the Virtual Environment

The environment must be activated before installing packages.

---

# Linux / macOS

```bash
source venv/bin/activate
```

---

# Windows CMD

```cmd
venv\Scripts\activate.bat
```

---

# Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

---

# Successful Activation

The terminal usually changes.

Example:

```text
(venv) user@computer:~/project$
```

This means the environment is active.

---

# Checking the Python Path

Use:

```bash
which python3
```

Example output:

```text
/home/user/project/venv/bin/python3
```

If it shows:

```text
/usr/bin/python3
```

then the venv is probably NOT activated.

---

# Deactivating the Environment

```bash
deactivate
```

This returns to the system Python.

---

# pip

`pip` is Python's package manager.

Used for:
- installing packages
- updating packages
- removing packages

---

# Installing Packages

```bash
pip install pydantic
```

---

# Installing Specific Versions

```bash
pip install "pydantic>=2"
```

---

# Installing Multiple Packages

```bash
pip install flake8 mypy requests
```

---

# Viewing Installed Packages

```bash
pip list
```

---

# requirements.txt

`requirements.txt` stores project dependencies.

Useful for:
- reproducibility
- collaboration
- deployment

---

# Creating requirements.txt

```bash
pip freeze > requirements.txt
```

---

# Example requirements.txt

```text
pydantic==2.11.0
mypy==1.15.0
flake8==7.2.0
```

---

# Installing from requirements.txt

```bash
pip install -r requirements.txt
```

---

# Why requirements.txt Matters

Without it:
- other users may install wrong versions
- projects may stop working
- environments become inconsistent

---

# Poetry

Poetry is a more advanced Python dependency manager.

It replaces:
- pip
- requirements.txt
- manual dependency handling

---

# Poetry Features

Poetry:
- manages dependencies
- creates virtual environments
- handles package versions
- simplifies project management

---

# Installing Poetry

Linux/macOS:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

---

# Creating a Poetry Project

```bash
poetry init
```

---

# Installing Dependencies

```bash
poetry add pydantic
```

---

# Activating Poetry Environment

```bash
poetry shell
```

---

# Installing from pyproject.toml

```bash
poetry install
```

---

# pyproject.toml

Poetry stores dependencies in:

```text
pyproject.toml
```

Instead of:
- requirements.txt

---

# Example pyproject.toml

```toml
[tool.poetry.dependencies]
python = "^3.10"
pydantic = "^2.11"
```

---

# PEP 668

PEP 668 protects system Python environments.

Modern Linux distributions may block:

```bash
pip install package
```

outside virtual environments.

---

# Common Error

```text
externally-managed-environment
```

This is extremely common on:
- Ubuntu
- Debian
- 42 machines

---

# Why This Happens

The operating system wants to protect:
- system Python
- system packages
- package manager integrity

---

# Recommended Solution

Use virtual environments:

```bash
python3 -m venv venv
source venv/bin/activate
```

Then install packages normally.

---

# Alternative Solution

Sometimes users install locally:

```bash
pip install --user package
```

But virtual environments are cleaner.

---

# Common Problems in 42 School

42 environments often have:
- limited permissions
- restricted system access
- outdated packages
- disk quota issues

---

# Common Problem: No Permission

Example:

```text
Permission denied
```

Usually solved by:
- using venv
- avoiding sudo

---

# Common Problem: PEP 668

Example:

```text
externally-managed-environment
```

Solution:
- create a venv

---

# Common Problem: No Space Left on Device

Example:

```text
OSError: [Errno 28] No space left on device
```

Very common in:
- `/tmp`
- home directories
- cached pip files

---

# Possible Solutions

Clean pip cache:

```bash
pip cache purge
```

Remove unused venvs:

```bash
rm -rf venv
```

---

# Common Problem: Wrong Python Version

Check version:

```bash
python3 --version
```

---

# Common Problem: Missing Packages

Example:

```text
ModuleNotFoundError: No module named 'pydantic'
```

Usually means:
- venv not activated
- package not installed

---

# Common Problem: which python3

If this returns:

```text
/usr/bin/python3
```

the venv is probably inactive.

---

# Common Problem: Broken venv

Sometimes virtual environments break.

Fix:

```bash
rm -rf venv
python3 -m venv venv
```

---

# Good Project Workflow

---

# Step 1

Create project folder:

```bash
mkdir my_project
cd my_project
```

---

# Step 2

Create virtual environment:

```bash
python3 -m venv venv
```

---

# Step 3

Activate environment:

```bash
source venv/bin/activate
```

---

# Step 4

Install dependencies:

```bash
pip install pydantic mypy flake8
```

---

# Step 5

Save dependencies:

```bash
pip freeze > requirements.txt
```

---

# Recommended .gitignore

Do NOT upload virtual environments to GitHub.

Example:

```gitignore
venv/
__pycache__/
*.pyc
```

---

# Best Practices

- Always use virtual environments
- Never commit venv folders
- Keep requirements.txt updated
- Prefer precise package versions
- Activate venv before working
- Avoid using sudo pip install

---

# Summary Table

| Tool / Concept | Purpose |
|---|---|
| venv | Isolated Python environment |
| pip | Package manager |
| requirements.txt | Stores dependencies |
| Poetry | Advanced dependency manager |
| PEP 668 | Protects system Python |
| activate | Enables virtual environment |

---

# Final Notes

Virtual environments are one of the most important parts of modern Python development.

Understanding them helps avoid:
- dependency conflicts
- broken projects
- permission issues
- package problems

This becomes especially important in:
- 42 projects
- team environments
- APIs
- large Python applications
- deployment systems

---
