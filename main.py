from time import sleep
from task_functions import Task

task_list = []
options = ["Add a task",
           "Delete a task",
           "Search tasks",
           "Update a task",
           "Save tasks"]


def main():
    print("TASK MANAGER")
    print("-" * 50)
    sleep(0.8)
    print("Please select an option: ")
    sleep(0.8)
    for i, v in enumerate(options):
        print(f"{i + 1}) {v}")
    sleep(0.5)

    def get_method() -> int:
        while True:
            try:
                selected = int(input("Please select an option (number): "))
            except ValueError:
                print("ERROR: please type in a number!")
                continue

            if 1 > selected > len(options):
                print(f"Please enter a number between 1-{len(options)}")
                continue

            return selected

    method = get_method()

    def task_deletion(tasks):
        print("Please select a task to delete: ")
        for num, item in enumerate(tasks):
            print(f"{num + 1}) {item.name}")

        while True:
            selected = input("Please type in the number to delete (or done to exit): ")

            if selected == "done":  # checks if value is done to break
                break

            try:  # checks to see if the value is an int else loop again
                selected = int(selected)
            except ValueError:
                sleep(0.8)
                print("Please enter a number or 'done'!")
                continue

            if 1 > selected > len(tasks):  # checks to see if it is in the range of the list index
                sleep(0.8)
                print(f"Please enter a number between 1-{len(tasks)}")
                continue

        confirmation = input(f"Please type in the name of the task ({tasks[selected - 1].name})")

        if confirmation == tasks[selected - 1].name:
            tasks[selected - 1].delete_task()
            print("Task deleted!")

        main()

    match method:
        case 1:
            task = Task()
            task.create_task(task_list, main)
        case 2:
            task_deletion(task_list)


if __name__ == "__main__":
    main()
