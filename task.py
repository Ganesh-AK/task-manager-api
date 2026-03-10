class Task:
    def __init__(self, title, status="pending"):
        self.title = title
        self.status = status

    def __repr__(self):
        return f"Task(title='{self.title}', status='{self.status}')"

t = Task("Buy groceries")
print(t)
