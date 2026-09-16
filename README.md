# Simple Todo List

A minimal CLI todo list that stores tasks in JSON.

## Usage

Add a task:
```bash
python todo.py add "buy milk"
```

List all tasks:
```bash
python todo.py list
```

Mark a task as done (by index):
```bash
python todo.py done 0
```

Run self-check:
```bash
python todo.py test
```

## How it works

- Tasks are stored in `todo.json` in the current directory
- Each task has `text` and `done` status
- Commands are processed via `sys.argv` with no external dependencies

