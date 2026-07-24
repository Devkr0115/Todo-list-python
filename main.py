import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task = input("Enter task: ").strip()

    if not task:
        print("Task cannot be empty!")
        return

    tasks.append({
        "task": task,
        "completed": False
    })

    save_tasks(tasks)
    print("✅ Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n====== TO-DO LIST ======")

    for index, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{index}. [{status}] {task['task']}")


def complete_task(tasks):
    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        choice = int(input("Enter task number to mark completed: "))

        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            save_tasks(tasks)
            print("✅ Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        choice = int(input("Enter task number to delete: "))

        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"🗑 Deleted: {removed['task']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def show_menu():
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


def main():
    tasks = load_tasks()

    while True:
        show_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("👋 Thank you for using the To-Do List App.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()