import sys, json
from datetime import date

id  = 0
def main():

    #usage python task-name task parameters(optional)
    global id 
    with open("count.txt", "r") as file:
        for cnt in file:
            id = int(cnt)

    if len(sys.argv) < 2:
        sys.exit("Enter atleast 1 valid argument")
    cmd = sys.argv[1]

    match cmd:
        case "add": add_task()
        case "delete": delete_task()
        case "update": update_task()
        case "mark-in-progress": mark_in_progress()
        case "mark-done": mark_done()
        case "list": list_tasks()
        case _ : sys.exit("Wrong command: Please refer correct command")
    
    with open("count.txt", "w") as file:
        file.write(str(id))

def add_task():
    try:
        task_name = sys.argv[2]
    except IndexError:
        sys.exit("Task name missing.")
    else:
        global id
        id += 1
        task_prop = {
                        "id": id,
                        "description": task_name,
                        "status": "to-do",
                        "createdAt": date.today().isoformat(),
                        "updatedAt": None
                    }
        
        try:
            with open("tasks.json", 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            open("tasks.json", "x")
            data = []
        except json.decoder.JSONDecodeError:
            data = []



        data.append(task_prop)
        with open("tasks.json", 'w') as file:
            json.dump(data, file)
            print(f"Task added successfully (ID: {id})")


def delete_task():
    try:
        task_id = int(sys.argv[2])
        with open("tasks.json", "r") as file:
            lines = json.load(file)
            print(lines)
    except IndexError:
        sys.exit("Task id missing.")
    except json.decoder.JSONDecodeError:
        print("Tasks list is empty.")
        pass
    except ValueError:
        sys.exit("Enter a valid id")

    else:
        data = []
        for line in lines:
            if line["id"] != task_id:
                data.append(line)
        with open("tasks.json", "w") as file:
            json.dump(data, file)

def update_task():
    try:
        task_id = int(sys.argv[2])
        new_task_name = sys.argv[3]
        with open("tasks.json", "r") as file:
            lines = json.load(file)
            print(lines)
    except IndexError:
        sys.exit("Missing arguments")
    except json.decoder.JSONDecodeError:
        print("Tasks list is empty.")
        pass
    except ValueError:
        sys.exit("Enter a valid id")

    else:
        data = []
        for line in lines:
            if line["id"] == task_id:
                line["description"]= new_task_name
                line["updatedAt"] = date.today().isoformat()
            data.append(line)
        with open("tasks.json", "w") as file:
            json.dump(data, file)

def mark_in_progress():
    try:
        task_id = int(sys.argv[2])
        with open("tasks.json", "r") as file:
            lines = json.load(file)
            print(lines)
    except IndexError:
        sys.exit("Missing task id")
    except json.decoder.JSONDecodeError:
        print("Tasks list is empty.")
        pass
    except ValueError:
        sys.exit("Enter a valid id")

    else:
        data = []
        for line in lines:
            if line["id"] == task_id:
                line["status"]= "In-progress"
                line["updatedAt"] = date.today().isoformat()
            data.append(line)
        with open("tasks.json", "w") as file:
            json.dump(data, file)

def mark_done():
    try:
        task_id = int(sys.argv[2])
        with open("tasks.json", "r") as file:
            lines = json.load(file)
            print(lines)
    except IndexError:
        sys.exit("Missing task id")
    except json.decoder.JSONDecodeError:
        print("Tasks list is empty.")
        pass
    except ValueError:
        sys.exit("Enter a valid id")

    else:
        data = []
        for line in lines:
            if line["id"] == task_id:
                line["status"]= "done"
                line["updatedAt"] = date.today().isoformat()
            data.append(line)
        with open("tasks.json", "w") as file:
            json.dump(data, file)

def list_tasks():
    try:
        with open("tasks.json", "r") as file:
            lines = json.load(file)
            print(lines)
    except IndexError:
        pass
    except json.decoder.JSONDecodeError:
        print("Tasks list is empty.")
        pass
    except ValueError:
        pass
    else:
        if len(sys.argv) == 2:
            status = None
        else: 
            status = sys.argv[2].lower()
        if status is None:
            for line in lines:
                print(f" Task id: {line["id"]} | Description: {line["description"]} | Status: {line["status"]} | Creation Date: {line["createdAt"]} | Updated Date: {line["updatedAt"]}")
        else:
            for line in lines:
                if line["status"].lower() == status:
                    print(f" Task id: {line["id"]} | Description: {line["description"]} | Creation Date: {line["createdAt"]} | Updated Date: {line["updatedAt"]}")

main()