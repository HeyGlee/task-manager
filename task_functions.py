import datetime  # imports the datetime lib to get access to the datetime data type
from time import sleep  # imports sleep to give the program some wait to make it seems as if its calculating

tags = ["Finance",
        "Software Engineering",
        "Business",
        "Architecture",
        "Cooking",
        "Art",
        "Sport",
        "Deadline",
        "Teams",
        "School",
        "Project",
        "Homework",
        "Family",
        "Hard",
        "Easy",
        "Boring"]


def trying(self, selected):
    try:
        self.tags.append(tags[selected - 1])
        return True
    except IndexError:
        sleep(0.8)
        print("ERROR: Please enter a number in range")
        sleep(0.8)
        return False


def confirmation_task(selecting, q_list, other_func, self) -> int:
    while True:

        selected = input(f"Please type in the number to {selecting} (or done to exit): ")

        if selected == "done":  # checks if value is done to break
            if not other_func:
                break

            print()
            other_func()

        try:  # checks to see if the value is an int else loop again
            selected = int(selected)
        except ValueError:
            sleep(0.8)
            print("Please enter a number or 'done'!")
            continue

        if 1 > selected > len(q_list):  # checks to see if it is in the range of the list index
            sleep(0.8)
            print(f"Please enter a number between 1-{len(q_list)}")
            continue

        if self and not trying(self, selected):
            continue

        if other_func:
            return selected

        #  # adds the tag to the list


def line_sep():
    print("-" * 50)


def operation_loader(message, message_2):
    print()
    print(message, end="")
    sleep(0.6)
    print(".", end="")
    sleep(0.6)
    print(".", end="")
    sleep(0.6)
    print(".")
    sleep(1)
    print()
    print(message_2)


def display_tasks(task_list, is_name):
    for num, item in enumerate(task_list):
        print(f"{num + 1}) {item.name if is_name else item}")


def wait_for_continue(menu):
    input("Press enter to continue.")
    print()
    menu()


class Task:
    def __init__(self):
        self.name = "Placeholder"  # for all prop. it will just assign default values obviously tbc
        self.date_due = datetime.datetime(2000, 1, 1)
        self.description = "This is a basic task description."
        self.tags = []

    def create_task(self, tasks, menu):
        # gets the name and description of a task
        print("\nTask creation: ")
        line_sep()
        sleep(1)
        self.name = input("Please enter the task name: ")
        sleep(1)
        self.description = input(f"Please enter the description of \"{self.name}\": ")
        sleep(1)

        # TODO: refactor code here and actually make date verification work. May need to remove datetime type?
        def get_date(message) -> int:
            try:
                date = int(input(f"Please enter the {message} \"{self.name}\" is due: "))  # attempts to enter date
                sleep(0.8)
                today = datetime.date.today()
                match message:
                    case "year":
                        if today.year > date:
                            print(f"ERROR: Please enter the current year ({today.year}) or later!")
                            get_date(message)
                    case "month":
                        if 1 > date or date > 12:
                            print("ERROR: Please enter an actual month number!")
                            get_date(message)
                return date
            except ValueError:
                print("ERROR: Please enter a number!")
                get_date(message)

        # gets the date due
        line_sep()
        self.date_due = datetime.datetime(get_date("year"), get_date("month"), get_date("day"))
        line_sep()

        def get_tags(tags_list: list):
            print("Tags:")
            sleep(0.5)
            display_tasks(tags_list, False)

        get_tags(tags)

        # ask the user to add any tags for the final step before displaying the task
        confirmation_task("add that tag", tags, None, self)
        line_sep()
        sleep(1)

        # display newly created task
        print(f"Task name: {self.name}")
        print(f"Task description: {self.description}")
        print(f"Date due: {self.date_due.strftime('%Y-%m-%d')}")
        print(f"Tags:", end=" ")

        for i, v in enumerate(self.tags):
            if i + 1 != len(self.tags):
                print(v, end=", ")
            else:
                print(v)

        operation_loader("Creating task ", "Task created!")
        line_sep()
        tasks.append(self)
        wait_for_continue(menu)

    def delete_task(self):
        del self
