tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks available!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_no = int(input("Enter task number to delete: "))

            if 1 <= task_no <= len(tasks):
                deleted_task = tasks.pop(task_no - 1)
                print(f"'{deleted_task}' deleted successfully!")
            else:
                print("Invalid task number!")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")