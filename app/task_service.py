
from app.storage import TaskStorage
from app.validators import validate_title


class TaskService:
    """Business logic for task management."""

    def __init__(self, storage=None):
        self.storage = storage or TaskStorage()

    def create_task(self, title: str) -> dict:
        clean_title = validate_title(title)
        return self.storage.add(clean_title)

    def list_tasks(self) -> list:
        return self.storage.list_all()

    def get_task(self, task_id: int):
        return self.storage.get(task_id)

    def delete_task(self, task_id: int) -> bool:
        return self.storage.delete(task_id)
