import csv
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from todo import TASKS_FILE, add_task, list_tasks, mark_done, remove_task, edit_task, duplicate_task, export_tasks, export_csv, load_tasks

def setup_function():
    if TASKS_FILE.exists():
        TASKS_FILE.unlink()

def teardown_function():
    if TASKS_FILE.exists():
        TASKS_FILE.unlink()

def test_add_and_list_tasks():
    add_task("test task 1")
    add_task("test task 2")
    add_task("test task 3")

    tasks = load_tasks()
    assert len(tasks) == 3
    assert tasks[0]["text"] == "test task 1"
    assert tasks[1]["text"] == "test task 2"
    assert tasks[2]["text"] == "test task 3"

def test_mark_done():
    add_task("test task 1")
    add_task("test task 2")

    mark_done(0)
    tasks = load_tasks()
    assert tasks[0]["done"] == True
    assert tasks[1]["done"] == False

def test_remove_task():
    add_task("test task 1")
    add_task("test task 2")
    add_task("test task 3")

    remove_task(1)
    tasks = load_tasks()
    assert len(tasks) == 2
    assert tasks[0]["text"] == "test task 1"
    assert tasks[1]["text"] == "test task 3"

def test_edit_task():
    add_task("test task 1")
    edit_task(0, "edited task 1")

    tasks = load_tasks()
    assert tasks[0]["text"] == "edited task 1"

def test_duplicate_task():
    add_task("test task 1")
    duplicate_task(0)

    tasks = load_tasks()
    assert len(tasks) == 2
    assert tasks[0]["text"] == "test task 1"
    assert tasks[1]["text"] == "test task 1"

def test_export_tasks_json():
    add_task("test task 1")
    mark_done(0)

    tasks = load_tasks()
    exported_json = json.dumps(tasks, indent=2)
    assert '"text": "test task 1"' in exported_json
    assert '"done": true' in exported_json

def test_export_tasks_csv():
    add_task("test task 1")
    add_task("test task 2")
    mark_done(0)

    tasks = load_tasks()
    csv_output = io.StringIO()
    writer = csv.writer(csv_output)
    writer.writerow(["Texto", "Status"])
    for task in tasks:
        status = "Concluído" if task["done"] else "Pendente"
        writer.writerow([task["text"], status])
    csv_content = csv_output.getvalue()

    assert "Texto,Status" in csv_content
    assert "test task 1,Concluído" in csv_content
    assert "test task 2,Pendente" in csv_content

def test_full_workflow():
    add_task("test task 1")
    add_task("test task 2")
    add_task("test task 3")

    mark_done(0)
    remove_task(1)
    edit_task(0, "edited task 1")
    duplicate_task(0)

    tasks = load_tasks()
    assert tasks[0]["done"] == True
    assert tasks[0]["text"] == "edited task 1"
    assert tasks[1]["text"] == "edited task 1"
    assert tasks[1]["done"] == False
    assert tasks[2]["text"] == "test task 3"
    assert len(tasks) == 3
