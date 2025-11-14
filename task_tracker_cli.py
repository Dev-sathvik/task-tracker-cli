import sys, json
from datetime import date


def main():
    #usage python task-name task parameters(optional)

    if len(sys.argv) < 2:
        sys.exit("Enter atleast 1 valid argument")
    cmd = sys.argv[1]

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
                    with open("tasks.json", "r") as file:
                        lines = json.load(file)
                        if len(lines) == 0:
                             raise json.decoder.JSONDecodeError("msg", 'doc', 0)
                        ##
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
                    with open("tasks.json", "r") as file:
                        lines = json.load(file)
                        #
                except IndexError:
                    sys.exit("Missing arguments")
                except json.decoder.JSONDecodeError:
                    print("Tasks list is empty.")
                    pass
                except ValueError:
                    sys.exit("Enter a valid id")
                update_task(new_task_name, task_id, lines)
        case "mark-in-progress":
                            if len(sys.argv) != 3:
                                sys.exit("wrong args")
                            try:
                                task_id = int(sys.argv[2])
                                with open("tasks.json", "r") as file:
                                    lines = json.load(file)
                                    #
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
                        with open("tasks.json", "r") as file:
                            lines = json.load(file)
                            #
                    except IndexError:
                        sys.exit("Missing task id")
                    except json.decoder.JSONDecodeError:
                        print("Tasks list is empty.")
                        pass
                    except ValueError:
                        sys.exit("Enter a valid id")
                    mark_done(task_id, lines)
        case "list":
                if len(sys.argv) != 3 or len(sys.argv) != 2:
                    print(len(sys.argv))
                    sys.exit("wrong args")
                try:
                    with open("tasks.json", "r") as file:
                        lines = json.load(file)
                        #
                except IndexError:
                    pass
                except json.decoder.JSONDecodeError:
                    print("Tasks list is empty.")
                    pass
                except ValueError:
                    pass
                if len(sys.argv) == 2:
                        status = None
                else: 
                    status = sys.argv[2].lower()
                list_tasks(lines, status)
        case _ : sys.exit("Wrong command: Please refer correct command")
    


def add_task(task_name):
        if not task_name:
             return False 
        
        with open("count.txt", "r") as file:
            for cnt in file:
                id = int(cnt)

        id = id + 1

        with open("count.txt", "w") as file:
            file.write(str(id))
        task_prop = {
                        "id": str(id),
                        "description": str(task_name),
                        "status": "todo",
                        "createdAt": str(date.today().isoformat()),
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
            return True


def delete_task(lines = None, task_id = None):
        if not lines or not task_id:
             return False
        data = []
        for line in lines:
            if line["id"] != str(task_id):
                data.append(line)
        with open("tasks.json", "w") as file:
            json.dump(data, file)
            return True


def update_task(new_task_name, task_id, lines):
        data = []
        for line in lines:
            if line["id"] == str(task_id):
                line["description"]= new_task_name
                line["updatedAt"] = str(date.today().isoformat())
            data.append(line)
        with open("tasks.json", "w") as file:
            json.dump(data, file)



def mark_in_progress(task_id, lines):
        data = []
        for line in lines:
            if line["id"] == str(task_id):
                line["status"]= "in-progress"
                line["updatedAt"] = str(date.today().isoformat())
            data.append(line)
        with open("tasks.json", "w") as file:
            json.dump(data, file)


def mark_done(task_id, lines):
        data = []
        for line in lines:
            if line["id"] == str(task_id):
                line["status"]= "done"
                line["updatedAt"] = date.today().isoformat()
            data.append(line)
        with open("tasks.json", "w") as file:
            json.dump(data, file)


def list_tasks(lines = [], status = None):
        listed = False
        #
        if status is None:
            for line in lines:
                print(f" Task id: {line["id"]} | Description: {line["description"]} | Status: {line["status"]} | Creation Date: {line["createdAt"]} | Updated Date: {line["updatedAt"]}")
                listed = True
        else:
            for line in lines:
                if line["status"] == status:
                    print(f" Task id: {line["id"]} | Description: {line["description"]} | Creation Date: {line["createdAt"]} | Updated Date: {line["updatedAt"]}")
                    listed = True
        return listed


if __name__ == "__main__":
    main()