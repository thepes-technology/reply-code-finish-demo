import csv
import json
import sys
from pathlib import Path
TASKS_FILE = Path('todo.json')

def print_todo_banner():
    print('  ┏━━━━┓')
    print('  ┃TODO┃')
    print('  ┗━━━━┛')

def load_tasks():
    if TASKS_FILE.exists():
        return json.loads(TASKS_FILE.read_text())
    return []

def save_tasks(tasks):
    TASKS_FILE.write_text(json.dumps(tasks, indent=2))

def add_task(text):
    print_todo_banner()
    tasks = load_tasks()
    tasks.append({'text': text, 'done': False})
    save_tasks(tasks)
    print(f'Added: {text}')

def list_tasks():
    print_todo_banner()
    tasks = load_tasks()
    if not tasks:
        print('No tasks.')
        return
    print('┌───┬────────┬─────────────────────────┐')
    print('│ # │ Status │ Task                    │')
    print('├───┼────────┼─────────────────────────┤')
    for i, task in enumerate(tasks):
        status = '✓' if task['done'] else ' '
        text = task['text'][:23].ljust(23)
        print(f'│ {i} │   {status}    │ {text} │')
    print('└───┴────────┴─────────────────────────┘')

def mark_done(index):
    print_todo_banner()
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        save_tasks(tasks)
        print(f'Done: {tasks[index]['text']}')
    else:
        print(f'Invalid task index: {index}')

def remove_task(index):
    print_todo_banner()
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f'Removed: {removed['text']}')
    else:
        print(f'Invalid task index: {index}')

def edit_task(index, new_text):
    print_todo_banner()
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        old_text = tasks[index]['text']
        tasks[index]['text'] = new_text
        save_tasks(tasks)
        print(f"Updated: '{old_text}' -> '{new_text}'")
    else:
        print(f'Invalid task index: {index}')

def duplicate_task(index):
    print_todo_banner()
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        original = tasks[index]
        new_task = {'text': original['text'], 'done': False}
        tasks.insert(index + 1, new_task)
        save_tasks(tasks)
        print(f"Duplicated: '{original['text']}'")
    else:
        print(f'Invalid task index: {index}')

def export_tasks():
    print_todo_banner()
    tasks = load_tasks()
    print(json.dumps(tasks, indent=2))

def import_tasks(path):
    print_todo_banner()
    file_path = Path(path)
    if not file_path.exists():
        print(f'File not found: {path}')
        return
    if file_path.suffix == '.csv':
        with file_path.open(newline='') as f:
            reader = csv.DictReader(f)
            tasks = [{'text': row['Texto'], 'done': row['Status'] == 'Concluído'} for row in reader]
    else:
        tasks = json.loads(file_path.read_text())
    save_tasks(tasks)
    print(f'Imported {len(tasks)} task(s) from {path}')

def export_csv():
    print_todo_banner()
    tasks = load_tasks()
    output = csv.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Texto', 'Status'])
    for task in tasks:
        status = 'Concluído' if task['done'] else 'Pendente'
        writer.writerow([task['text'], status])
    print(output.getvalue(), end='')
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python todo.py [add|list|done|remove|edit|duplicate|export|export-csv|import|test]')
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'add' and len(sys.argv) > 2:
        add_task(' '.join(sys.argv[2:]))
    elif cmd == 'list':
        list_tasks()
    elif cmd == 'done' and len(sys.argv) > 2:
        mark_done(int(sys.argv[2]))
    elif cmd == 'remove' and len(sys.argv) > 2:
        remove_task(int(sys.argv[2]))
    elif cmd == 'edit' and len(sys.argv) > 3:
        edit_task(int(sys.argv[2]), ' '.join(sys.argv[3:]))
    elif cmd == 'duplicate' and len(sys.argv) > 2:
        duplicate_task(int(sys.argv[2]))
    elif cmd == 'export':
        export_tasks()
    elif cmd == 'export-csv':
        export_csv()
    elif cmd == 'import' and len(sys.argv) > 2:
        import_tasks(sys.argv[2])
    elif cmd == 'test':
        from test_todo import demo
        demo()
    else:
        print('Unknown command or missing arguments.')
