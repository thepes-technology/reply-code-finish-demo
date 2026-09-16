
import csv
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / ))
from todo import TASKS_FILE, add_task, list_tasks, mark_done, remove_task, edit_task, duplicate_task, export_tasks, export_csv, load_tasks

def setup_function():
    
    if TASKS_FILE.exists():
        TASKS_FILE.unlink()

def teardown_function():
    
    if TASKS_FILE.exists():
        TASKS_FILE.unlink()

def test_add_and_list_tasks():
    
    add_task()
    add_task()
    add_task()

    tasks = load_tasks()
    assert len(tasks) == 3
    assert tasks[0][] == 
    assert tasks[1][] == 
    assert tasks[2][] == 

def test_mark_done():
    
    add_task()
    add_task()

    mark_done(0)
    tasks = load_tasks()
    assert tasks[0][] == True
    assert tasks[1][] == False

def test_remove_task():
    
    add_task()
    add_task()
    add_task()

    remove_task(1)
    tasks = load_tasks()
    assert len(tasks) == 2
    assert tasks[0][] == 
    assert tasks[1][] == 

def test_edit_task():
    
    add_task()
    edit_task(0, )

    tasks = load_tasks()
    assert tasks[0][] == 

def test_duplicate_task():
    
    add_task()
    duplicate_task(0)

    tasks = load_tasks()
    assert len(tasks) == 2
    assert tasks[0][] == 
    assert tasks[1][] == 

def test_export_tasks_json():
    
    add_task()
    mark_done(0)

    tasks = load_tasks()
    exported_json = json.dumps(tasks, indent=2)
    assert  in exported_json
    assert  in exported_json

def test_export_tasks_csv():
    
    add_task()
    add_task()
    mark_done(0)

    tasks = load_tasks()
    csv_output = io.StringIO()
    writer = csv.writer(csv_output)
    writer.writerow([, ])
    for task in tasks:
        status =  if task[] else 
        writer.writerow([task[], status])
    csv_content = csv_output.getvalue()

    assert  in csv_content
    assert  in csv_content
    assert  in csv_content

def test_full_workflow():
    
    add_task()
    add_task()
    add_task()

    mark_done(0)
    remove_task(1)
    edit_task(0, )
    duplicate_task(0)

    tasks = load_tasks()
    assert tasks[0][] == True
    assert tasks[0][] == 
    assert tasks[1][] == 
    assert tasks[1][] == False
    assert tasks[2][] == 
    assert len(tasks) == 3
