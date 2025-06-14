import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().with_name('tasks.json')


def load_tasks():
    if DATA_FILE.exists():
        with open(DATA_FILE) as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)


def add_task(description):
    tasks = load_tasks()
    tasks.append({'description': description, 'done': False})
    save_tasks(tasks)


def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks, 1):
        status = '✓' if task['done'] else ' '
        print(f"{i}. [{status}] {task['description']}")


def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        save_tasks(tasks)
