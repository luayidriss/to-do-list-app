tasks = []

def add_task():
    """
    The user inputs the task they want to add and it will add it to the to do lisy
    """
    print("Please enter your task name and its due date")
    print("The due date should follow this format MM-DD-YYYY")
    print("Example:")
    print("Task Name: Fold Laundry")
    print("Due Date: 02-11-2023")
    print("By default a new task will be marked as incomplete")

    task_name = input("Enter Task Name:")
    due_date = input("Enter Due Date:")
    new_task = {'name': task_name, 'due_date': due_date, 'Completion Status': 'Incomplete'}
    tasks.append(new_task)
    print("Task Added")

def remove_task():
    """
    The use can remove any task by searching for its name
    """
    task_to_remove = input("Input the name of the task to remove: ")
    found_task = False
    for task in tasks:
        if task['name'] == task_to_remove:
            found_task = True
            tasks.remove(task)
            print(f"Task {task_to_remove} has been removed.")
            return
    if not found_task:
            print(f"Task {task_to_complete} not found.")
        
def view_tasks():
    print("To Do:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['name']} - Due Date: {task['due_date']} - Completion Status: {task['Completion Status']}")

def update_task_completion():
    """
    The user can update the completion status of any task by searching for its name
    """
    options = {
    1: "Complete",
    2: "In Progress",
    3: "Incomplete",
    }

    task_to_complete = input("Input the name of the task to update: ")

    while True:
        for key, value in options.items():
            print(f"{key}: {value}")
    
        selection = int(input("Please select a completion status:"))
        found_task = False
        for task in tasks:
            if task['name'] == task_to_complete:
                found_task = True
                if selection == 1:
                    task['Completion Status'] = 'Complete'
                    print(f"Task {task_to_complete} is now set as complete.")
                    return
                if selection == 2:
                    task['Completion Status'] = 'In Progress'
                    print(f"Task {task_to_complete} is now set as in progress.")
                    return
                if selection == 3:
                    task['Completion Status'] = 'Incomplete'
                    print(f"Task {task_to_complete} is now set as incomplete.")
                    return
                else:
                    print("Invalid option selected, please try again.") 
        if not found_task:
            print(f"Task {task_to_complete} not found.")
            break

def main():
    options = {
    1: "Add Task",
    2: "Remove Task",
    3: "Set Task Completion Status",
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
            update_task_completion()
        elif selection == 4:
            view_tasks()
        else:
            print("Invalid option selected, please try again.")

main()
