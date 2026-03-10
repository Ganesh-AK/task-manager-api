from datetime import datetime

class Task:
    def __init__(self, id: int, title: str,
                 description: str = '', priority: str = 'medium'):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority    # low / medium / high
        self.status = 'pending'     # pending / completed
        self.created_at = datetime.now().isoformat()

    def complete(self):
        self.status = 'completed'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'status': self.status,
            'created_at': self.created_at
        }

    def __repr__(self):
        return f"Task({self.id}: {self.title} [{self.status}])"
    
    def update_priority(self, new_priority):
        self.priority = new_priority
        print(f"Priority updated to: {new_priority}")

    def is_high_priority(self):
        return self.priority == 'high'
    
    