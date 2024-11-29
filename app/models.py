from utils import IDGenerator


class Task:
    """Модель задачи"""
    def __init__(self, title: str, description: str, category: str, due_date: str, priority: str):
        self.id = IDGenerator.get_next_id()
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = "не выполнена"

    def to_dict(self):
        return vars(self)

    @staticmethod
    def from_dict(data: dict):
        task = Task(
            title=data["title"],
            description=data["description"],
            category=data["category"],
            due_date=data["due_date"],
            priority=data["priority"]
        )
        task.id = data["id"]
        task.status = data["status"]
        return task
