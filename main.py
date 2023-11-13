from time import sleep
from task_functions import Task
from task_functions import wait_for_continue, operation_loader, display_tasks, line_sep, confirmation_task


task_list = []
options = ["Add a task",
           "Delete a task",
           "Search tasks",
           "Update a task",
           "Save tasks"]


def main():
    print("TASK MANAGER")
    line_sep()
    sleep(0.8)
    print("Please select an option: ")
    sleep(0.8)
    display_tasks(options, False)
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
        print("DELETE A TASK: \n")
        print("Please select a task to delete: ")
        line_sep()

        if not len(tasks):  # checks to see if the task list is empy
            print("No tasks have been created")
            wait_for_continue(main)

        display_tasks(task_list, True)

        selected = confirmation_task("to delete", tasks, main, None)
        confirmation = input(f"Please type in the name of the task ({tasks[selected - 1].name}): ")

        if confirmation == tasks[selected - 1].name:
            tasks[selected - 1].delete_task()
            operation_loader("Deleting task ", "Task deleted!")
            print()

        main()

    match method:
        case 1:
            task = Task()
            task.create_task(task_list, main)
        case 2:
            task_deletion(task_list)


if __name__ == "__main__":
    main()
