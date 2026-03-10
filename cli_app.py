from storage import load_tasks, save_tasks
from models import Task
from utils import timer, validate_priority

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(t.id for t in tasks) + 1

@validate_priority
def add_task(title, description='', priority='medium'):
    tasks = load_tasks()
    task = Task(get_next_id(tasks), title, description, priority)
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: [{task.id}] {task.title}")

def list_tasks(filter_priority=None, filter_status=None):
    tasks = load_tasks()
    if filter_priority:
        tasks = [t for t in tasks if t.priority == filter_priority]
    if filter_status:
        tasks = [t for t in tasks if t.status == filter_status]
    if not tasks:
        print("No tasks found.")
        return
    print(f"\n{'ID':<5} {'Title':<25} {'Priority':<10} {'Status'}")
    print("-" * 55)
    for t in tasks:
        print(f"{t.id:<5} {t.title:<25} {t.priority:<10} {t.status}")

def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task.id == task_id:
            task.complete()
            save_tasks(tasks)
            print(f"✅ Task {task_id} marked complete.")
            return
    print(f"❌ Task {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    original_count = len(tasks)
    tasks = [t for t in tasks if t.id != task_id]
    if len(tasks) == original_count:
        print(f"❌ Task {task_id} not found.")
        return
    save_tasks(tasks)
    print(f"🗑 Task {task_id} deleted.")

def search_tasks(keyword):
    tasks = load_tasks()
    keyword = keyword.lower()
    results = [t for t in tasks if keyword in t.title.lower()
               or keyword in t.description.lower()]
    if not results:
        print(f"No tasks found for '{keyword}'")
        return
    for t in results:
        print(f"[{t.id}] {t.title} — {t.priority} — {t.status}")

def show_summary():
    tasks = load_tasks()
    total     = len(tasks)
    completed = len([t for t in tasks if t.status == 'completed'])
    pending   = len([t for t in tasks if t.status == 'pending'])
    high      = len([t for t in tasks if t.priority == 'high'])

    print(f"\n📊 SUMMARY")
    print(f"   Total tasks   : {total}")
    print(f"   Completed     : {completed}")
    print(f"   Pending       : {pending}")
    print(f"   High priority : {high}")

def update_task(task_id, new_title=None, new_description=None, new_priority=None):
    tasks = load_tasks()
    for task in tasks:
        if task.id == task_id:
            if new_title:
                task.title = new_title
            if new_description:
                task.description = new_description
            if new_priority and new_priority in ['low', 'medium', 'high']:
                task.priority = new_priority
            save_tasks(tasks)
            print(f"✅ Task {task_id} updated.")
            return
    print(f"❌ Task {task_id} not found.")

def show_menu():
    print("\n" + "="*40)
    print("       TASK MANAGER")
    print("="*40)
    print("1. Add task")
    print("2. List all tasks")
    print("3. List by priority")
    print("4. List pending only")
    print("5. Complete a task")
    print("6. Delete a task")
    print("7. Search tasks")
    print("8. Show Summary")
    print("0. Exit")
    print("="*40)

def main():
    print("Welcome to Task Manager!")
    while True:
        show_menu()
        choice = input("Choose option: ").strip()

        if choice == '1':
            title = input("Title: ").strip()
            desc = input("Description (optional): ").strip()
            priority = input("Priority (low/medium/high) [medium]: ").strip() or 'medium'
            add_task(title, desc, priority)

        elif choice == '2':
            list_tasks()

        elif choice == '3':
            priority = input("Priority (low/medium/high): ").strip()
            list_tasks(filter_priority=priority)

        elif choice == '4':
            list_tasks(filter_status='pending')

        elif choice == '5':
            list_tasks()
            try:
                task_id = int(input("Enter task ID to complete: "))
                complete_task(task_id)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == '6':
            list_tasks()
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == '7':
            keyword = input("Search keyword: ").strip()
            search_tasks(keyword)

        elif choice == '8': 
            show_summary()

        elif choice == '9':
            list_tasks()
            try:
                task_id = int(input("Task ID to update: "))
                print("Press Enter to skip a field.")
                new_title    = input("New title: ").strip() or None
                new_desc     = input("New description: ").strip() or None
                new_priority = input("New priority (low/medium/high): ").strip() or None
                update_task(task_id, new_title, new_desc, new_priority)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == '0':
            print("Goodbye! 👋")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()