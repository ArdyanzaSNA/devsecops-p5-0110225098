
from app.task_service import TaskService
from app.task_report import generate_task_report


def main():
    service = TaskService()

    while True:
        print("\n=== SecureTask ===")
        print("1. Add task")
        print("2. List tasks")
        print("3. Delete task")
        print("4. Task report")
        print("5. Exit")

        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                title = input("Task title: ")
                task = service.create_task(title)
                print(f"Created task #{task['id']}: {task['title']}")

            elif choice == "2":
                tasks = service.list_tasks()
                if not tasks:
                    print("No tasks found.")
                for task in tasks:
                    status = "Done" if task["completed"] else "Pending"
                    print(f"{task['id']}. {task['title']} [{status}]")

            elif choice == "3":
                task_id = int(input("Task ID: "))
                if service.delete_task(task_id):
                    print("Task deleted.")
                else:
                    print("Task not found.")

            elif choice == "4":
                report = generate_task_report(service.list_tasks())
                print("\n=== Task Report ===")
                print(f"Total tasks: {report['total']}")
                print(f"Completed: {report['completed']}")
                print(f"Pending: {report['pending']}")

            elif choice == "5":
                break

            else:
                print("Invalid choice.")

        except (ValueError, TypeError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
