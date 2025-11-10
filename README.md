---

# Task Tracker CLI

A simple **Command Line Interface (CLI)** tool to manage and track your tasks.
You can add, update, delete, and mark tasks as done or in progress — all from your terminal.

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Dev-sathvik/task-tracker-cli.git
   cd task-tracker-cli
   ```

2. **(Optional) Create and activate a virtual environment**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

---

## How to Run

Run the program using Python:

```bash
python task-tracker-cli.py <command> [arguments]
```

---

## Examples

```bash
# Add a new task
python task-tracker-cli.py add "Buy groceries"

# Update a task
python task-tracker-cli.py update 1 "Buy groceries and cook dinner"

# Delete a task
python task-tracker-cli.py delete 1

# Mark a task as in progress
python task-tracker-cli.py mark-in-progress 1

# Mark a task as done
python task-tracker-cli.py mark-done 1

# List all tasks
python task-tracker-cli.py list

# List tasks by status
python task-tracker-cli.py list done
python task-tracker-cli.py list todo
python task-tracker-cli.py list in-progress
```

**Author:** Sathvik
**GitHub:** [Dev-sathvik](https://github.com/Dev-sathvik)

---
