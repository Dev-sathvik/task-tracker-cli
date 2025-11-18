#!/usr/bin/env python3

import sys
import json
import os
from datetime import date

config_dir = os.path.expanduser("~/.config/task-cli")

os.makedirs(config_dir, exist_ok=True)

COUNT_FILE = os.path.join(config_dir, "count.txt")
JSON_FILE = os.path.join(config_dir, "tasks.json")


def main():
    # Check if the arguments to the program are right.
    if len(sys.argv) < 2:
        sys.exit("Enter atleast 1 valid argument")
    cmd = sys.argv[1]

    # Look for command match.
    match cmd:
        case "add":
            if len(sys.argv) != 3:
                sys.exit("wrong args")
            try:
                task_name = sys.argv[2]
            except IndexError:
                sys.exit("Task name missing.")
            add_task(task_name)

        case "delete":
            if len(sys.argv) != 3:
                sys.exit("wrong args")

            try:
                task_id = int(sys.argv[2])
                with open(JSON_FILE, "r") as file:
                    lines = json.load(file)
                    if len(lines) == 0:
                        raise json.decoder.JSONDecodeError("msg", 'doc', 0)
            except IndexError:
                sys.exit("Task id missing.")
            except json.decoder.JSONDecodeError:
                sys.exit("Tasks list is empty.")
            except ValueError:
                sys.exit("Enter a valid id")
            delete_task(lines, task_id)

        case "update":
            if len(sys.argv) != 4:
                sys.exit("wrong args")

            try:
                task_id = int(sys.argv[2])
                new_task_name = sys.argv[3]
                with open(JSON_FILE, "r") as file:
                    lines = json.load(file)
            except IndexError:
                sys.exit("Missing arguments")
            except json.decoder.JSONDecodeError:
                sys.exit("Tasks list is empty.")
            except ValueError:
                sys.exit("Enter a valid id")
            update_task(new_task_name, task_id, lines)

        case "mark-in-progress":
            if len(sys.argv) != 3:
                sys.exit("wrong args")
            try:
                task_id = int(sys.argv[2])
                with open(JSON_FILE, "r") as file:
                    lines = json.load(file)
            except IndexError:
                sys.exit("Missing task id")
            except json.decoder.JSONDecodeError:
                print("Tasks list is empty.")
                pass
            except ValueError:
                sys.exit("Enter a valid id")
            mark_in_progress(task_id, lines)

        case "mark-done":
            if len(sys.argv) != 3:
                sys.exit("wrong args")

            try:
                task_id = int(sys.argv[2])
                with open(JSON_FILE, "r") as file:
                    lines = json.load(file)
            except IndexError:
                sys.exit("Missing task id")
            except json.decoder.JSONDecodeError:
                print("Tasks list is empty.")
                pass
            except ValueError:
                sys.exit("Enter a valid id")
            mark_done(task_id, lines)

        case "list":
            if len(sys.argv) != 3 and len(sys.argv) != 2:
                sys.exit("wrong args")

            try:
                with open(JSON_FILE, "r") as file:
                    lines = json.load(file)
            except json.decoder.JSONDecodeError:
                sys.exit("Tasks list is empty.")

            if len(sys.argv) == 2:
                status = None
            else:
                status = sys.argv[2]
            list_tasks(lines, status)

        case _: sys.exit("Wrong command: Please refer correct command")


# Add a new task.
def add_task(task_name):

    if not task_name:
        return False

    try:
        with open(COUNT_FILE, "r") as file:
            id = int(file.read().strip())
    except FileNotFoundError:
        id = 0
        with open(COUNT_FILE, "x") as file:
            pass

    id += 1

    with open(COUNT_FILE, "w") as file:
        file.write(str(id))

    task_prop = {
        "id": str(id),
        "description": str(task_name),
        "status": "todo",
        "createdAt": str(date.today().isoformat()),
        "updatedAt": "Not Updated"
    }

    try:
        with open(JSON_FILE, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        open(JSON_FILE, "x")
        data = []
    except json.decoder.JSONDecodeError:
        data = []

    data.append(task_prop)
    with open(JSON_FILE, 'w') as file:
        json.dump(data, file)
        print(f"Task added successfully (ID: {id})")
        return True


# Delete a task.
def delete_task(lines=None, task_id=None):
    if not lines or not task_id:
        return False

    data = []
    for line in lines:
        if line["id"] != str(task_id):
            data.append(line)
    with open(JSON_FILE, "w") as file:
        json.dump(data, file)
        return True


def update_task(new_task_name, task_id, lines):
    data = []
    for line in lines:
        if line["id"] == str(task_id):
            line["description"] = new_task_name
            line["updatedAt"] = str(date.today().isoformat())
        data.append(line)
    with open(JSON_FILE, "w") as file:
        json.dump(data, file)


# Mark task status as in-progress.
def mark_in_progress(task_id, lines):
    helper(task_id, lines, "in-progress")


# Mark task status as done.
def mark_done(task_id, lines):
    helper(task_id, lines, "done")


# List tasks.
def list_tasks(lines=[], status=None):
    if len(lines) == 0:
        print("No tasks to display")
        return False

    if status is None:
        for line in lines:
            print(f" | Task id: {line["id"]} | Description: {line["description"]} | Status: {line["status"]} | Creation Date: {line["createdAt"]} | Updated Date: {line["updatedAt"]} |")
    else:
        for line in lines:
            if line["status"] == status:
                print(f" | Task id: {line["id"]} | Description: {line["description"]} | Creation Date: {line["createdAt"]} | Updated Date: {line["updatedAt"]} |")
    return True


# Helper function.
def helper(task_id, lines, status):
    data = []
    for line in lines:
        if line["id"] == str(task_id):
            line["status"] = status
            line["updatedAt"] = date.today().isoformat()
        data.append(line)
    with open(JSON_FILE, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    main()
