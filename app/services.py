import json
from typing import List

from models import Task
from utils import IDGenerator, is_valid_future_date


class TaskManager:
    """Менеджер задач"""
    def __init__(self, storage_file: str = "tasks.json"):
        self.storage_file = storage_file
        self.tasks: List[Task] = self.load_tasks()
        IDGenerator.current_id = self.search_max_id()

    def search_max_id(self) -> int:
        max_id = 0
        if self.tasks:
            for task in self.tasks:
                if task.id > max_id:
                    max_id = task.id
        return max_id

    def load_tasks(self) -> List[Task]:
        """Автоматическая загрузка задач из файла"""
        try:
            with open(self.storage_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Task.from_dict(task) for task in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        """Сохранение задач в файл"""
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, ensure_ascii=False, indent=4)

    def add_task(self, task: Task):
        """Создание задачи"""
        if task.title and task.description and task.category and task.due_date and task.priority:
            if is_valid_future_date(task.due_date):
                self.tasks.append(task)
                self.save_tasks()
                print(f"Задача {task.title} успешно добавлена")
            else:
                print(f"Введите корректную дату")
        else:
            print(f"Необходимо заполнить все поля")

    def list_tasks(self, category: str = None):
        """Вывод или всех задач, или по указанной категории"""
        tasks = [task for task in self.tasks if category is None or task.category == category]
        if tasks:
            print(f"Найдено задач - {len(tasks)}:")
            for task in tasks:
                print(f"{task.id} - {task.title} [{task.category}] "
                      f"(Приоритет: {task.priority}, Выполнить до: {task.due_date}) - {task.status}")
        elif category:
            print(f"Задач с категорией {category} не найдено")
        else:
            print(f"Список задач пуст")

    def delete_task(self, task_id: str):
        """Удаление задачи"""
        if task_id.isdigit():
            for index, task in enumerate(self.tasks):
                if task.id == int(task_id):
                    self.tasks.pop(index)
                    print(f"Задача с id {task_id} успешно удалена")
                    self.save_tasks()
                    break
            else:
                print(f"Задачи с указанным id нет")
        else:
            print(f"Переданный id не является целым числом")

    def edit_task(self, task_id: str, **kwargs):
        """Редактирование задачи"""
        if not task_id.isdigit():
            print(f"Переданный id не является целым числом")
            return -1
        try:
            if kwargs["due_date"]:
                if not is_valid_future_date(kwargs["due_date"]):
                    print(f"Введите корректную дату")
                    return -1
        except KeyError:
            pass

        for task in self.tasks:
            if task.id == int(task_id):
                for key, value in kwargs.items():
                    if hasattr(task, key) and value:
                        setattr(task, key, value)
                self.save_tasks()
                print(f"Задача с id {task_id} успешно изменена")
                break
        else:
            print(f"Задачи с указанным id нет")

    def search_tasks(self, keyword: str):
        """Поиск задачи по ключевому слову"""
        tasks = [task for task in self.tasks
                 if task.category == keyword
                 or task.status == keyword
                 or task.title == keyword]
        if tasks:
            print(f"Найдено задач - {len(tasks)}:")
            for task in tasks:
                print(f"{task.id} - {task.title} [{task.category}] "
                      f"(Приоритет: {task.priority}, Выполнить до: {task.due_date}) - {task.status}")
        else:
            print(f"Не найдено совпадений по слову {keyword}")

    def change_status(self, task_id: str):
        """Изменение статуса задачи"""
        if task_id.isdigit():
            for task in self.tasks:
                if task.id == int(task_id):
                    task.status = "выполнена"
                    self.save_tasks()
                    print(f"Задача с id {task_id} выполнена")
                    break
            else:
                print(f"Задачи с указанным id нет")
        else:
            print(f"Переданный id не является целым числом")
