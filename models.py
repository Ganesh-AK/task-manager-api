from datetime import datetime
from datetime import date

class Task:
    def __init__(self, id: int, title: str,
                 description: str = '', priority: str = 'medium',due_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority    # low / medium / high
        self.status = 'pending'     # pending / completed
        self.created_at = datetime.now().isoformat()
        self.due_date = due_date 
    
    def is_overdue(self):
        if not self.due_date:
            return False
        due = date.fromisoformat(self.due_date)
        return date.today() > due

    def complete(self):
        self.status = 'completed'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'status': self.status,
            'created_at': self.created_at,
            'due_date': self.due_date
        }

    def __repr__(self):
        return f"Task({self.id}: {self.title} [{self.status}])"
    
    @classmethod
    def from_dict(cls, data: dict):
        task = cls(
            id=data['id'],
            title=data['title'],
            description=data.get('description', ''),
            priority=data.get('priority', 'medium'),
            due_date=data.get('due_date', None)
        )
        task.status = data.get('status', 'pending')
        task.created_at = data.get('created_at', '')
        return task
    
    def update_priority(self, new_priority):
        if new_priority not in ['low', 'medium', 'high']:
            print("Invalid priority!")
            return
        self.priority = new_priority
        print(f"Priority updated to: {new_priority}")

    def is_high_priority(self):
        return self.priority == 'high'
    
    
