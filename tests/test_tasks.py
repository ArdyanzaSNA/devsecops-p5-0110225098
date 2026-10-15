
import unittest

from app.task_service import TaskService


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


if __name__ == "__main__":
    unittest.main()
