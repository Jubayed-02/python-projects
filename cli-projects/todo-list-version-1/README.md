# Personal Todo App Version-1

A simple, interactive command-line **todo-list application** written in pure Python. It lets a user create, mark, delete, and view tasks from the terminal. No external libraries or dependencies are required.

> Note: the list will not be saved on local machine. it will store data while the code is running.

## Overview

This is a beginner-friendly Python project that simulates a **personal todo-list** in the terminal. The user interacts with the program via a numbered menu, and all tasks are held in an in-memory dictionary for the duration of the session.

## Features

- **Create a task** (code `1`)
- **Mark a task as completed** (code `2`)
- **Delete a task** (code `3`)
- **View the list** (code `4`)
- **Exit the app** (code `0`)
- Clean terminal formatting with separator lines
- Graceful handling of invalid input and `Ctrl+C` (`KeyboardInterrupt`)
- Automatic re-indexing of tasks after deletion

---

## Requirements

- **Python 3.x**
- No third-party packages

---

## How to Run

Save the script as `todo_app.py` and run:

```bash
python todo_app.py
```
