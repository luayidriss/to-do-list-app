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

    task_name = input("Enter Task Name:")
    due_date = input("Enter Due Date:")
    new_task = {'name': task_name, 'due_date': due_date}
    tasks.append(new_task)
    print("Task Added")
    return tasks

def remove_task():
    """
    The use can remove any task by searching for its name
    """
    task_to_remove = input("Input the name of the task to remove: ")
    for task in tasks:
        if task['name'] == task_to_remove:
            tasks.remove(task)
            print(f"Task {task_to_remove} has been removed.")
            return
    print(f"Task {task_to_remove} not found.")
        

def view_tasks():
    print("To Do:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['name']} - Due Date: {task['due_date']}")

def main():
    options = {
    1: "Add Task",
    2: "Remove Task",
    3: "View Tasks",
    4: "Sort Tasks",
    5: "Load Tasks",
    6: "Save Tasks",
    7: "Exit To Do List"
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
            view_tasks()
        else:
            print("Invalid option selected, please try again.")

main()
