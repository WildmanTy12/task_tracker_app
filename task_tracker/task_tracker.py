import json

tasks = []


def save_tasks():
    """Save the tasks after an edit using JSON format"""

    with open("tasks.json", "w") as f:
        json.dump(tasks, f)


def load_tasks():
    """
    Load the task list from a JSON file,
    or return an empty list if the file doesn't exist.
    """

    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


tasks = load_tasks()


def menu():
    """Display the main menu and prompt the user to choose an action."""

    while True:
        try:
            print("\n--- Task Tracker ---")
            print("1. Add a new task")
            print("2. Update an existing task")
            print("3. View all tasks")
            print("4. Exit")

            menu_input = int(input("Enter 1, 2, 3, or 4: "))

            if menu_input == 1:
                add_task()

            elif menu_input == 2:
                update_tasks()

            elif menu_input == 3:
                view_tasks()

            elif menu_input == 4:
                print("Goodbye!")
                exit()

            else:
                print("Invalid option. Please enter 1-4.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def display_tasks():
    """Display all tasks with emoji status indicators for better UX."""

    for index, task in enumerate(tasks, start=1):
        status = "✅ Completed" if task['done'] else "⏳ Not done"
        print(f"{index}. {task['title']} {status}")


def add_task():
    """Prompt the user to add a new task and save it to the task list."""

    while True:
        title = input(
            "Enter a new task or Press Enter to return to the main menu: "
        ).strip()

        if title == "":
            return

        task = {"title": title, "done": False}
        tasks.append(task)
        save_tasks()
        print(f"Task '{title}' added!")


def view_tasks():
    """Display all current tasks."""

    if not tasks:
        print("No tasks to view.")
        return

    display_tasks()

    input("Press Enter to return to the main menu.")


def update_tasks():
    """
    Prompt the user to select a task and
    either update its title, status,
    or delete it.
    """

    if not tasks:
        print("No tasks to update.")
        return

    display_tasks()

    selection = input(
        "Which task do you want to update? "
        "Enter the number or Press Enter to return to the main menu: "
    ).strip()

    if selection == "":
        return

    if not selection.isdigit():
        print("Invalid input. Please enter a number.")
        return

    task_index = int(selection) - 1

    if task_index < 0 or task_index >= len(tasks):
        print("That task number does not exist.")
        return

    task = tasks[task_index]

    option = input(
        f"What do you want to do with '{task['title']}'?\n"
        "1. Update title\n"
        "2. Update status\n"
        "3. Delete task\n"
        "Or press Enter to cancel: "
    ).strip()

    if option == "":
        return

    if option == "1":
        new_title = input("Enter new title: ").strip()

        if new_title == "":
            print("No title entered. Returning to menu.")
            return

        task["title"] = new_title
        save_tasks()
        print(f"Title updated to '{new_title}'.")

    elif option == "2":
        new_status = input(
            "Enter new status: 'd' for done, 'n' for not done: "
        ).strip().lower()

        if new_status == "":
            return

        if new_status not in ("d", "n"):
            print(f"'{new_status}' is not a valid option.")
            return

        task["done"] = new_status == "d"
        save_tasks()
        status_friendly = "✅ Completed" if task['done'] else "⏳ Not done"
        print(f"Status updated to {task['title']} {status_friendly}.")

    elif option == "3":
        delete_confirmation = input(
            f"Are you sure you want to delete {task['title']}"
            "? y/n ")

        if delete_confirmation == "y":
            tasks.remove(task)
            save_tasks()
            print(f"'{task['title']}' has been removed.")
            return

        return


def main():
    """Run the main menu loop."""

    menu()


if __name__ == "__main__":
    main()
