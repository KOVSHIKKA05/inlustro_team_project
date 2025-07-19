tasks = []

while True:
    print("\n1. View  2. Add  3. Done  4. Delete  5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t['task']} - {'Done' if t['done'] else 'Not Done'}")

    elif choice == "2":
        name = input("Enter task: ")
        tasks.append({"task": name, "done": False})

    elif choice == "3":
        num = int(input("Task number to mark done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True

    elif choice == "4":
        num = int(input("Task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            tasks.pop(num)

    elif choice == "5":
        break

    else:
        print("Invalid option.")