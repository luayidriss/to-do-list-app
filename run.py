import csv
import os
from datetime import datetime

tasks = []

TASK_VIEW_TEMPLATE = """
{index}. {name} - Due Date: {due_date} - Completion Status: {status}
"""

WELCOME_MSG = """
Welcome to the To Do List App. Please choose an option:

    1: Add Task
    2: Remove Task
    3: Edit Task
    4: View Tasks
    5: Sort Tasks
    6: Load Tasks
    7: Save Tasks
    8: Exit To Do List
"""
ADD_TASK_MSG = """
Please enter your task name and its due date
The due date should follow this format DD-MM-YYYY
Example:
Task Name: Fold Laundry
Due Date: 02-11-2023
By default a new task will be marked as incomplete
"""

UPDATE_TASK_MSG = """
How would you like to edit your task?

    1: Edit Name
    2: Edit Due Date
    3: Mark as Complete
    4: Mark as In Progress
    5: Mark as Incomplete
    6: Return to Main Menu
"""

SORT_TASKS_MSG = """
How would you like to sort your tasks?

1: Sort by Due Date
2: Sort by Completion Status
3: Return to Main Menu
"""

LOAD_CSV_MSG = """
Loading a csv file will initialize your current to do list,
Do you wish to proceed?
    1: No 
    2: Yes
    """

FILE_PATH = "/workspace/to-do-list-app/to_do_lists"


def validate_name():
    """
    Makes sure no empty name is inputted for a task.
    """
    while True:
        name = input("Enter the task name: ")
        if name:
            return name
        else:
            print("Task name cannot be empty.")


def validate_date():
    """
    Validates a date input so it fits the format of a date.
    """
    while True:
        date = input("Enter Due Date:")
        try:
            datetime.strptime(date, "%d-%m-%Y")
            return date
        except ValueError:
            print("Incorrect date format, should be dd-mm-yyyy")


def validate_file():
    """
    Validates a file path and if its a csv file conforms to program standard.
    """
    while True:
        path = input("Enter the file path:")
        try:
            with open(path, "r") as file:
                reader = csv.reader(file)
                header = next(reader)
                if (
                    "name" not in header
                    and "due_date" not in header
                    and "Completion Status" not in header
                ):
                    print(
                        "CSV file must have headers 'name', 'due_date', 'Completion Status'."
                    )
                    return
                for row in reader:
                    try:
                        datetime.strptime(
                            row[header.index("due_date")], "%d-%m-%Y"
                        )
                    except ValueError:
                        print(
                            f"Incorrect date format in row {row}, should be dd-mm-yyyy"
                        )
                        return
                print("File is valid")
                return path
        except FileNotFoundError:
            print("File not found.")
            return
        except csv.Error:
            print("File is not a valid CSV file.")
            return


def add_task():
    """
    The user inputs the task they want to add
    it will add it to the to do list.
    """
    print(ADD_TASK_MSG)
    task_name = validate_name()
    due_date = validate_date()
    new_task = {
        "name": task_name,
        "due_date": due_date,
        "Completion Status": "Incomplete",
    }
    tasks.append(new_task)
    print(f"Task {new_task['name']} has been adeed.")


def find_task():
    """
    Finds a task by its name, to allow for removal or editing the task.
    """
    task_to_find = input("Enter the name of the task you want to find: ")
    for task in tasks:
        if task["name"] == task_to_find:
            return task
    return None


def remove_task():
    """
    The use can remove any task by searching for its name
    """
    task_to_remove = find_task()
    if task_to_remove:
        tasks.remove(task_to_remove)
        print(f"Task {task_to_remove['name']} has been removed.")
    else:
        print(f"Task {task_to_remove} not found.")


def view_tasks():
    """
    View all tasks as a to do list.
    """
    print("To Do:")
    for i, task in enumerate(tasks):
        print(TASK_VIEW_TEMPLATE.format(index=i+1, name=task['name'], due_date=task['due_date'], status=task['Completion Status']))


def update_task():
    """
    The user can update the completion status of any task by searching
    for its name or edit its name and due date.
    """
    task_to_update = find_task()
    if not task_to_update:
        print(f"Task {task_to_update} not found.")
    else:
        print(UPDATE_TASK_MSG)
        while True:
            try:
                selection = int(input("Enter the number of your selection: "))
            except ValueError:
                print("Invalid option selected, please try again.")
                continue
            if selection == 1:
                updated_name = input("Enter the new name of the task:")
                task_to_update["name"] = updated_name
                print(f"Task {task_to_update['name']} is now named {updated_name}.")
                return
            if selection == 2:
                updated_due_date = validate_date()
                task_to_update["due_date"] = updated_due_date
                print(
                    f"Task {task_to_update['name']}'s due date is now {updated_due_date}."
                )
                return
            if selection == 3:
                task_to_update["Completion Status"] = "Complete"
                print(f"Task {task_to_update['name']} is now set as complete.")
                return
            if selection == 4:
                task_to_update["Completion Status"] = "In Progress"
                print(f"Task {task_to_update['name']} is now set as in progress.")
                return
            if selection == 5:
                task_to_update["Completion Status"] = "Incomplete"
                print(f"Task {task_to_update['name']} is now set as incomplete.")
                return
            if selection == 6:
                main()
            else:
                print("Invalid option selected, please try again.")



def sort_tasks():
    """
    Sorts your to do list by due date or by completion status.
    """
    while True:
        print(SORT_TASKS_MSG)
        try:
            selection = int(input("Enter the number of your selection: "))
        except ValueError:
            print("Invalid option selected, please try again.")
            continue
        global tasks
        if selection == 1:
            sorted_tasks = sorted(tasks, key=lambda x: x["due_date"])
            tasks = sorted_tasks
            print("Tasks sorted by Due Date.")
            return tasks
        elif selection == 2:
            sorted_tasks = sorted(
                tasks,
                key=lambda x: (
                    x["Completion Status"] != "In Progress",
                    x["Completion Status"] != "Incomplete",
                    x["Completion Status"] != "Complete",
                ),
            )
            tasks = sorted_tasks
            print("Tasks sorted by Completion Status.")
            return tasks
            view_tasks()
        elif selection == 3:
            main()
        else:
            print("Invalid option selected, please try again.")


def save_to_csv():
    """
    Saves the current list to a csv file.
    """
    file_name = input("Enter the file name: ")
    file_path = "/workspace/to-do-list-app/to_do_lists"
    full_path = os.path.join(file_path, file_name)
    with open(full_path, "w", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["name", "due_date", "Completion Status"]
        )
        writer.writeheader()
        writer.writerows(tasks)
        # for task in tasks:
        #     writer.writerow(task)
    print(f"Tasks saved to {full_path}")


def load_csv():
    """
    Users can load a csv file with the same format unto the program and edit it.
    """
    while True:
        print(LOAD_CSV_MSG)
        try:
            selection = int(input("Enter the number of your selection: "))
        except ValueError:
            print("Invalid option selected, please try again.")
            continue

        if selection == 1:
            break
        elif selection == 2:
            global tasks
            file_path = validate_file()
            if isinstance(file_path, str):
                # tasks = []
                with open(file_path, "r") as csv_file:
                    reader = csv.DictReader(csv_file)
                    tasks = list(reader)
                    # for row in reader:
                    #     tasks.append(dict(row))
                print("File is loaded.")
                return tasks
            else:
                print(
                    "File was not loaded, make sure the file fits the criteria."
                )
                return
        else:
            print("Invalid option selected, please try again.")


def main():
    """
    Main Menu.
    """
    while True:
        print(WELCOME_MSG)
        selection = None
        try:
            selection = int(input("Enter the number of your selection: "))
        except ValueError:
            print("Invalid option selected, please try again.")
            continue

        if selection == 1:
            add_task()
        elif selection == 2:
            remove_task()
        elif selection == 3:
            update_task()
        elif selection == 4:
            view_tasks()
        elif selection == 5:
            sort_tasks()
        elif selection == 6:
            load_csv()
        elif selection == 7:
            save_to_csv()
        elif selection == 8:
            exit()
        else:
            print("Invalid option selected, please try again.")


if __name__ == "__main__":
    main()
