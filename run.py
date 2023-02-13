from datetime import datetime

tasks = []

def validate_date():
    while True:
        date = input("Enter Due Date:")
        try:
            datetime.strptime(date, '%d-%m-%Y')
            return date
        except ValueError:
            print("Incorrect date format, should be dd-mm-yyyy")

def add_task():
    """
    The user inputs the task they want to add and it will add it to the to do lisy
    """
    print("Please enter your task name and its due date")
    print("The due date should follow this format DD-MM-YYYY")
    print("Example:")
    print("Task Name: Fold Laundry")
    print("Due Date: 02-11-2023")
    print("By default a new task will be marked as incomplete")

    task_name = input("Enter Task Name:")
    due_date = validate_date()
    new_task = {'name': task_name, 'due_date': due_date, 'Completion Status': 'Incomplete'}
    tasks.append(new_task)
    print("Task Added")


def find_task():
    task_to_find = input("Enter the name of the task you want to find: ")
    for task in tasks:
        if task['name'] == task_to_find:
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
    print("To Do:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['name']} - Due Date: {task['due_date']} - Completion Status: {task['Completion Status']}")

def update_task():
    """
    The user can update the completion status of any task by searching for its name
    """
    options = {
    1: "Edit Name",
    2: "Edit Due Date",
    3: "Mark as Complete",
    4: "Mark as In Progress",
    5: "Mark as Incomplete",
    }

    task_to_update = find_task()
    if task_to_update:
        for key, value in options.items():
            print(f"{key}: {value}")
        selection = int(input("Enter the number of your selection: "))
        if selection == 1:
            updated_name = input("Enter the new name of the task:")
            task_to_update['name'] = updated_name
            print(f"Task {task_to_update['name']} is now named {updated_name}.")
            return
        if selection == 2:
            updated_due_date = validate_date()
            task_to_update['due_date'] = updated_due_date
            print(f"Task {task_to_update['name']}'s due date is now {updated_due_date}.")
            return
        if selection == 3:
            task_to_update['Completion Status'] = 'Complete'
            print(f"Task {task_to_update['name']} is now set as complete.")
            return
        if selection == 4:
            task_to_update['Completion Status'] = 'In Progress'
            print(f"Task {task_to_update['name']} is now set as in progress.")
            return
        if selection == 5:
            task_to_update['Completion Status'] = 'Incomplete'
            print(f"Task {task_to_update['name']} is now set as incomplete.")
            return
        else:
            print("Invalid option selected, please try again.")
    else:
        print(f"Task {task_to_update} not found.")

def sort_tasks():
    options = {
    1: "Sort by Due Date",
    2: "Sort by Completion Status"
}
    while True:
        print("Please select an option:")
        for key, value in options.items():
            print(f"{key}: {value}")
    
        selection = int(input("Enter the number of your selection: "))
        global tasks
        if selection == 1:
            sorted_tasks = sorted(tasks, key=lambda x: x['due_date'])
            tasks = sorted_tasks
            return tasks
        elif selection == 2:
            sorted_tasks = sorted(tasks, key=lambda x: 
                       (x['Completion Status'] != "In Progress", 
                        x['Completion Status'] != "Incomplete", 
                        x['Completion Status'] != "Complete"))
            tasks = sorted_tasks
            return tasks
        else:
            print("Invalid option selected, please try again.")
   
def main():
    options = {
    1: "Add Task",
    2: "Remove Task",
    3: "Edit Task",
    4: "View Tasks",
    5: "Sort Tasks",
    6: "Load Tasks",
    7: "Save Tasks",
    8: "Exit To Do List"
}

    while True:
        print("Please select an option:")
        for key, value in options.items():
            print(f"{key}: {value}")
    
        selection = int(input("Enter the number of your selection: "))
    
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
        else:
            print("Invalid option selected, please try again.")

main()
