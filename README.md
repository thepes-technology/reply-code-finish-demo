# Simple Todo List

A minimal CLI todo list that stores tasks in JSON.

## Project Structure

```
├── src/
│   └── todo.py          # Main CLI implementation
├── tests/
│   └── test_todo.py     # Test suite
└── README.md
```

## Usage

Add a task:
```bash
python src/todo.py add "buy milk"
```

List all tasks:
```bash
python src/todo.py list
```

Mark a task as done (by index):
```bash
python src/todo.py done 0
```

Edit a task (by index):
```bash
python src/todo.py edit 0 "buy organic milk"
```

Duplicate a task (by index):
```bash
python src/todo.py duplicate 0
```

Remove a task (by index):
```bash
python src/todo.py remove 0
```

Export all tasks as JSON:
```bash
python src/todo.py export
```

Run tests:
```bash
python -m pytest tests/test_todo.py
