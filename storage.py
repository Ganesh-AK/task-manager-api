import json
import os
from dotenv import load_dotenv
from models import Task

load_dotenv()  # reads .env into environment variables

TASKS_FILE = os.getenv('TASKS_FILE', 'tasks.json')

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []  # normal on first run
    try:
        with open(TASKS_FILE, 'r') as f:
            data = json.load(f)
        return [Task.from_dict(d) for d in data]
    except json.JSONDecodeError:
        print("⚠️  Warning: tasks file is corrupted. Starting fresh.")
        return []
    except Exception as e:
        print(f"⚠️  Unexpected error loading tasks: {e}")
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)
    print("Tasks saved.")