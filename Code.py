import os

# Task file location
TASK_FILE = "tasks.txt"

# Function to read tasks from file
def fetch_tasks():
    if os.path.isfile(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            tasks_list = [task.strip() for task in file.readlines()]
        return tasks_list
    else:
        return []

# Function to write tasks to file
def store_tasks(tasks_list):
    with open(TASK_FILE, "w") as file:
        for task in tasks_list:
            file.write(task + "\n")

# Display menu options
def display_menu():
    print("\n==== My Task Manager ====")
    print("1. Insert New Task")
    print("2. View All Tasks")
    print("3. Delete a Task")
    print("4. Quit")

# Add a new task to the list
def insert_task(tasks_list):
    new_task = input("Type your new task: ")
    tasks_list.append(new_task)
    store_tasks(tasks_list)
    print(f"Task '{new_task}' has been added.")

# Show all existing tasks
def view_tasks(tasks_list):
    if not tasks_list:
        print("No tasks found. Enjoy your free time!")
    else:
        print("Here are your current tasks:")
        for idx, task in enumerate(tasks_list, start=1):
            print(f"{idx}. {task}")

# Remove task by its number
def delete_task(tasks_list):
    view_tasks(tasks_list)
    if tasks_list:
        try:
            task_no = int(input("Enter the task number to remove: "))
            if 1 <= task_no <= len(tasks_list):
                removed_task = tasks_list.pop(task_no - 1)
                store_tasks(tasks_list)
                print(f"Task '{removed_task}' has been removed.")
            else:
                print("That task number doesn't exist.")
        except ValueError:
            print("Please enter a valid number.")

# Main program loop
def main():
    tasks = fetch_tasks()
    while True:
        display_menu()
        option = input("Select an option: ")

        if option == "1":
            insert_task(tasks)
        elif option == "2":
            view_tasks(tasks)
        elif option == "3":
            delete_task(tasks)
        elif option == "4":
            print("Goodbye! Have a productive day.")
            break
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()