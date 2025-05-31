def show_menu():
    print("\n-- To-Do List Menu --")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. delete Task")
    print("4. Exit")

def view_tasks():
    try:
        with open("tasks.txt","r") as file:
            tasks=file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                print("\nYou Tasks:")
                for i,task in enumerate(tasks, 1):
                    print(f"{i}.{task.strip()}")
    except FileNotFoundError:
        print("No tasks file found.Start by adding tasks.")

def add_task():
    task=input("Enter the task:")
    with open("tasks.txt","a") as file:
        file.write(task + "\n")
    print("Task added!")

def delete_task():
    view_tasks()
    try:
        with open("tasks.txt","r")as file:
            tasks=file.readlines()
        task_num=int(input("Enter task numbe to delete:"))
        if 0 < task_num <= len(tasks):
            deleted =tasks.pop(task_num-1)
            with open("tasks.txt","w") as file:
                file.writelines(tasks)
            print(f"Deleted: {deleted.strip()}")
        else:
            print("Invalid task number.")
    except(ValueError,FileNotFoundError):
        print("Error deleting task.")

#Main Loop
while True:
    show_menu()
    choice=input("Enter your choice(1-4):")
    if choice =="1":
        view_tasks()
    if choice =="2":
        add_task()
    if choice =="3":
        delete_task()
    elif choice =="4":
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")


