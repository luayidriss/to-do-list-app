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
    new_task = (task_name, due_date)
    tasks.append(new_task)
    print("Task Added")
    return tasks

def remove_task():
    """
    The use can remove any task by searching for its name
    """
    print("Input the name of the task you would like to remove")
    task_name = input("Enter Task Name you want to remove:")
    for i, (name,date) in enumerate(task):
        del tasks[i]
        print("Task Deleted")
        break
    else:
        print("Task not found")
    
updated_task = add_task()
print(updated_task)

