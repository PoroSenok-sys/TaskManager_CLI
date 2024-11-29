from models import Task
from services import TaskManager


def main():
    manager = TaskManager()

    while True:
        print("\nМенеджер задач")
        print("1. Добавить задачу")
        print("2. Просмотреть задачи")
        print("3. Редактировать задачу")
        print("4. Удалить задачу")
        print("5. Поиск задачи")
        print("6. Изменение статуса задачи")
        print("7. Выход")

        choice = input("Выберите действие: ")
        if choice == "1":
            title = input("Название задачи: ")
            description = input("Описание: ")
            category = input("Категория: ")
            due_date = input("Срок выполнения (YYYY-MM-DD): ")
            priority = input("Приоритет (низкий, средний, высокий): ")
            manager.add_task(Task(title=title, description=description, category=category,
                                  due_date=due_date, priority=priority))
        elif choice == "2":
            category = input("Категория (оставьте пустым для всех задач): ")
            manager.list_tasks(category if category else None)
        elif choice == "3":
            task_id = input("ID задачи для редактирования: ")
            title = input("Новое название (оставьте пустым для пропуска): ")
            description = input("Новое описание (оставьте пустым для пропуска): ")
            category = input("Новая категория (оставьте пустым для пропуска): ")
            due_date = input("Новый срок выполнения (оставьте пустым для пропуска): ")
            priority = input("Новый приоритет (оставьте пустым для пропуска): ")
            manager.edit_task(task_id, title=title, description=description, category=category, due_date=due_date,
                              priority=priority)
        elif choice == "4":
            task_id = input("ID задачи для удаления: ")
            manager.delete_task(task_id)
        elif choice == "5":
            keyword = input("Введите ключевое слово для поиска: ")
            manager.search_tasks(keyword)
        elif choice == "6":
            task_id = input("ID выполненной задачи: ")
            manager.change_status(task_id)
        elif choice == "7":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
