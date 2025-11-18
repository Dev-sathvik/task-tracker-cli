
# Task Tracker CLI

A simple **Command Line Interface (CLI)** tool to manage and track your tasks.
You can add, update, delete, and mark tasks as done or in progress — all from your terminal.

---

## Installation

1.**Clone the repository**

```bash
git clone https://github.com/Dev-sathvik/task-tracker-cli.git && cd task-tracker-cli
```

2.**Rename the *task_tracker_cli.py* into *task-cli* and copy it into the */usr/local/bin* and make it executable**

```bash
sudo cp task_tracker_cli.py /usr/local/bin/task-cli && sudo chmod +x /usr/local/bin/task-cli
```


## How to Run

Run the program in terminal:

```bash
task-cli <command> [arguments]
```

---

## Examples

```bash
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress

```
---

**Author:** Sathvik  
**GitHub:** [Dev-sathvik](https://github.com/Dev-sathvik)  
**Problem Statement:** https://roadmap.sh/projects/task-tracker

---
