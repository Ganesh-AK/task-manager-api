import json
import os
from models import Task

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        data = json.load(f)
    return [Task.from_dict(d) for d in data]

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)
    print("Tasks saved.")