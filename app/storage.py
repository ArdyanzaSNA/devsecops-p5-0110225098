
class TaskStorage:
    """In-memory storage for tasks."""

    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def add(self, title: str) -> dict:
        task = {
            "id": self._next_id,
            "title": title,
            "completed": False,
        }
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task.copy()

    def list_all(self) -> list:
        return [task.copy() for task in self._tasks.values()]

    def get(self, task_id: int):
        task = self._tasks.get(task_id)
        return task.copy() if task else None

    def delete(self, task_id: int) -> bool:
        return self._tasks.pop(task_id, None) is not None
