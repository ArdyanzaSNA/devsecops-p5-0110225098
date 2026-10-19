
def generate_task_report(tasks: list) -> dict:
    """Generate summary statistics for a list of tasks."""
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
    }
