from time import sleep
import task_functions


def main():
    options = ["Add a task",
               "Delete a task",
               "Search tasks",
               "Update a task",
               "Save tasks"]

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

    match method:
        case 1:
            pass





if __name__ == "__main__":
    main()