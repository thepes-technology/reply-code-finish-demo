"""Test suite for todo list."""
from pathlib import Path
from todo import TASKS_FILE, add_task, list_tasks, mark_done, remove_task, edit_task, duplicate_task, load_tasks

def demo():
    """Run self-check: add, list, mark done, remove, edit, and duplicate tasks."""
    if TASKS_FILE.exists():
        TASKS_FILE.unlink()

    add_task("test task 1")
    add_task("test task 2")
    add_task("test task 3")
    list_tasks()
    print()

    mark_done(0)
    list_tasks()
    print()

    remove_task(1)
    list_tasks()
    print()

    edit_task(0, "edited task 1")
    list_tasks()
    print()

    duplicate_task(0)
    list_tasks()
    print()

    tasks = load_tasks()
    assert tasks[0]["done"] == True
    assert tasks[0]["text"] == "edited task 1"
    assert tasks[1]["text"] == "edited task 1"
    assert tasks[1]["done"] == False
    assert tasks[2]["text"] == "test task 3"
    assert len(tasks) == 3
    TASKS_FILE.unlink()
    print("Self-check passed.")

if __name__ == "__main__":
    demo()
