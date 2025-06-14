# Programacion-

This repository contains a small Python project: a simple command line task manager.

## Usage

The project provides a `main.py` script with the following commands:

- `add <description>`: Add a new task with the given description.
- `list`: List all tasks.
- `done <index>`: Mark a task as done (1-based index).

Example:

```bash
python3 main.py add "Buy milk"
python3 main.py list
python3 main.py done 1
```

Tasks are stored in `task_manager/tasks.json` and will persist between runs.
