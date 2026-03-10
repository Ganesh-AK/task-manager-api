from models import Task

# Create tasks
t1 = Task(1, 'Learn FastAPI', 'Build REST API', 'high')
t2 = Task(2, 'Learn Docker', priority='medium')
t3 = Task(3, 'Buy groceries', priority='low')

# Test to_dict
print(t1.to_dict())

# Test complete()
t1.complete()
print('Status:', t1.status)  # should print: completed

# Test __repr__
print(t2)  # should print: Task(2: Learn Docker [pending])

# List of tasks
tasks = [t1, t2, t3]

# Filter high priority
high = [t for t in tasks if t.priority == 'high']
print('High priority:', high)

# Filter pending only
pending = [t for t in tasks if t.status == 'pending']
print('Pending:', pending)

# Test update_priority
t2.update_priority('high')
print(t2.priority)          # should print: high

# Test is_high_priority
print(t1.is_high_priority())   # True
print(t3.is_high_priority())   # False