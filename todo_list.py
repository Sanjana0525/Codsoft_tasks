tasks = []

while True:
    print("\n ------ WELCOME TO YOUR TO-DO LIST ------")
    print("1 : Add Task")
    print("2 : View Tasks")
    print("3 : Update Task")
    print("4 : Delete Task")
    print("5 : Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks are available.")
        else:
            print("\nYour Tasks are :")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        num = int(input("Enter the task number to update: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1] = input("Enter the new task to update: ")
            print("Task updated successfully!")
        else:
            print("Invalid task number entered.")

    elif choice == "4":
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        num = int(input("Enter the task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number entered.")

    elif choice == "5":
        print("Exiting from the To-Do List!")
        break

    else:
        print("Invalid choice! Please Try again.")
