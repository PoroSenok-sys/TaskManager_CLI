from app.models import Task
from app.services import TaskManager

import pytest


@pytest.fixture
def manager():
    test_json = "tests.json"
    with open(test_json, "w"):
        pass
    manager = TaskManager(test_json)
    return manager


def test_add_task(manager):
    assert not manager.tasks

    manager.add_task(Task(title="title", description="description", category="category",
                          due_date="not data", priority="priority"))
    assert not manager.tasks

    manager.add_task(Task(title="", description="description", category="category",
                          due_date="2025-02-02", priority="priority"))
    assert not manager.tasks

    manager.add_task(Task(title="title", description="description", category="category",
                          due_date="2025-02-02", priority="priority"))
    assert manager.tasks[0].title == "title"
    assert manager.tasks[0].description == "description"
    assert manager.tasks[0].category == "category"
    assert manager.tasks[0].due_date == "2025-02-02"
    assert manager.tasks[0].priority == "priority"


def test_delete_task(manager):
    manager.tasks.append(Task(title="title", description="description", category="category",
                              due_date="2025-02-02", priority="priority"))
    assert manager.tasks
    manager.delete_task("1")
    assert not manager.tasks


def test_edit_task(manager):
    assert not manager.tasks
    manager.tasks.append(Task(title="title", description="description", category="category",
                              due_date="2025-02-02", priority="priority"))
    assert manager.tasks

    manager.edit_task(task_id="1")
    assert manager.tasks[0].title == "title"
    assert manager.tasks[0].description == "description"
    assert manager.tasks[0].category == "category"
    assert manager.tasks[0].due_date == "2025-02-02"
    assert manager.tasks[0].priority == "priority"

    manager.edit_task(task_id="1", title="not data")
    assert manager.tasks[0].due_date == "2025-02-02"

    manager.edit_task(task_id="1", title="new title")
    assert manager.tasks[0].title == "new title"
