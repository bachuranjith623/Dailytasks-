import os

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        tasks = []
        for line in file:
            parts = line.strip().split("|")
            if len(parts) == 2:
                tasks.append({"task": parts[0], "done": parts[1] == "True"})
        return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for t in tasks:
            file.write(f"{t['task']}|{t['done']}\n")

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("\n📌 No tasks available!\n")
        return
    print("\n📝 To-Do List:")
    for i, t in enumerate(tasks, start=1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")
    print()

# Add a new task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    tasks[:] = load_tasks()
    print("Task added successfully!\n")

# Mark task as complete
def mark_complete(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter task number to mark as complete: "))
        if 1 <= choice <= len(tasks):
            tasks[choice-1]["done"] = True
            save_tasks(tasks)
            tasks[:] = load_tasks()
            print("Task marked as complete!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("📋 To-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Complete")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()