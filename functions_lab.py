tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# # MVP
# # As a user, to manage my task list I would like a program that allows me to:

# # Print a list of uncompleted tasks
def uncompleted_tasks(tasks):
    list_uncompleted = ""
    for task in tasks:
        if task["completed"] == False:
            list_uncompleted += task["description"]+ ", "
    if list_uncompleted == "":
        return "All tasks completed!!"
    return print("Uncompleted tasks: " + list_uncompleted [:-2] + ".")

# Print a list of completed tasks
def completed_tasks(tasks):
    list_completed = ""
    for task in tasks:
        if task["completed"] == True:
            list_completed += task["description"]+ ", "
    if list_completed == "":
        return "NO tasks completed!!"
    return print("Completed tasks: " + list_completed [:-2] + ".")

# Print a list of all task descriptions
def task_descriptions(tasks):
    list=[]
    for task in tasks:
        list.append(task["description"])
    return print(list)

# Print a list of tasks where time_taken is at least a given time
def task_min_time(tasks, min_time):
    list=[]
    for task in tasks:
        if task["time_taken"] >= min_time:
            list.append(task["description"])
    return print(list)

# Print any task with a given description
def task_by_description(tasks, task_description):
    for task in tasks:
        if task["description"].lower() == task_description:
            return print(task)
    return print("Task not found!")

# Extension
# Given a description update that task to mark it as complete.
def mark_as_complete(tasks, task_description):
    for task in tasks:
        if task["description"].lower() == task_description:
            task["completed"] = True
            return print(task)
    return print("Task not found!")


# Add a task to the list
def add_task(new_task, new_completed, new_time_taken):
    tasks.append({
        "description" : new_task,
        "completed" : new_completed,
        "time_taken" : new_time_taken,
    })
    return print(tasks)

# Further Extensions
# Use a while loop to display the following menu and allow the use to enter an option.
# Call the appropriate function depending on the users choice.
def open_menu():
        print("Menu:")
        print("1: Display All Tasks")
        print("2: Display Uncompleted Tasks")
        print("3: Display Completed Tasks")
        print("4: Mark Task as Complete")
        print("5: Get Tasks Which Take Longer Than a Given Time")
        print("6: Find Task by Description")
        print("7: Add a new Task to list")
        print("M or m: Display this menu")
        print("Q or q: Quit")
        return menu(input("Select option: ").lower())

def menu(option):
    while option != "q":
        while (option in ["1","2","3","4","5","6","7","m"]) == False:
            return open_menu()
        if option == "1":
            task_descriptions(tasks)
            option = input()
        elif option == "2":
            uncompleted_tasks(tasks)
            option = input()
        elif option == "3":
            completed_tasks(tasks)
            option = input()
        elif option == "4":
            user_input = input("Input a completed task: ").lower()
            mark_as_complete(tasks, user_input)
            option = input()
        elif option == "5":
            at_least = int(input("Input minimum time of task: "))
            task_min_time(tasks, at_least)
            option = input()
        elif option == "6":
            user_input = input("Input a task: ").lower()
            task_by_description(tasks, user_input)
            option = input()
        elif option == "7":
            user_input_task = input("Add task to list: ")
            user_input_completed = bool(input(f"Have you completed {user_input_task}, True or False: "))
            user_input_time = int(input(f"How long will {user_input_task} take in minutes?: "))
            add_task(user_input_task, user_input_completed, user_input_time)
            option = input()
        elif option == "m":
            return open_menu()
    return

open_menu()


