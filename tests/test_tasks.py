
import unittest

from app.task_service import TaskService
from app.task_report import generate_task_report


class TaskServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = TaskService()

    def test_create_task(self):
        task = self.service.create_task("Finish assignment")
        self.assertEqual(task["title"], "Finish assignment")
        self.assertFalse(task["completed"])

    def test_reject_empty_title(self):
        with self.assertRaises(ValueError):
            self.service.create_task("   ")

    def test_list_tasks(self):
        self.service.create_task("Task A")
        self.service.create_task("Task B")
        self.assertEqual(len(self.service.list_tasks()), 2)

    def test_delete_task(self):
        task = self.service.create_task("Temporary task")
        self.assertTrue(self.service.delete_task(task["id"]))
        self.assertIsNone(self.service.get_task(task["id"]))


class TaskReportTests(unittest.TestCase):
    def test_generate_task_report(self):
        tasks = [
            {"id": 1, "title": "Task A", "completed": True},
            {"id": 2, "title": "Task B", "completed": False},
            {"id": 3, "title": "Task C", "completed": False},
        ]

        report = generate_task_report(tasks)

        self.assertEqual(report["total"], 3)
        self.assertEqual(report["completed"], 1)
        self.assertEqual(report["pending"], 2)

    def test_empty_task_report(self):
        report = generate_task_report([])

        self.assertEqual(report["total"], 0)
        self.assertEqual(report["completed"], 0)
        self.assertEqual(report["pending"], 0)


if __name__ == "__main__":
    unittest.main()
