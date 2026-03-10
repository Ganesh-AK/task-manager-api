# Task Manager CLI

A command-line task management application built with Python.
Demonstrates OOP, file persistence, decorators, and error handling.

## Tech Stack
- Python 3.12
- JSON file storage
- Virtual environment

## Features
- Add tasks with title, description, and priority
- List all tasks with filters (priority, status)
- Complete and delete tasks
- Search tasks by keyword
- Update existing tasks
- View summary statistics
- Input validation with custom decorators
- Error handling for corrupted files

## Project Structure
task-manager-api/
├── models.py       # Task class with OOP
├── storage.py      # JSON file read/write
├── cli_app.py      # Main app with menu
├── utils.py        # Decorators and helpers
├── requirements.txt
└── README.md

## How to Run

# 1. Clone the repo
git clone https://github.com/Ganesh-AK/task-manager-api.git
cd task-manager-api

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python cli_app.py

## Example Usage
Choose option: 1
Title: Learn FastAPI
Description: Build REST API
Priority: high
✅ Task added: [1] Learn FastAPI

## What I Learned
- Object-Oriented Programming with Python classes
- File I/O and JSON persistence
- Python decorators for input validation
- Error handling with try/except
- Git version control and GitHub

## Author
Your Name — github.com/Ganesh-AK