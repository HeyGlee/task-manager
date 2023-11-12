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


class Task:
    def __init__(self):
        self.name = "Placeholder"  # for all prop. it will just assign default values obviously tbc
        self.date_due = datetime.datetime(2000, 1, 1)
        self.description = "This is a basic task description."
        self.tags = []

    def create_task(self, tasks, menu):
        # gets the name and description of a task
        print("Task creation: ")
        print("-" * 50)
        sleep(1)
        self.name = input("Please enter the task name: ")
        sleep(1)
        self.description = input(f"Please enter the description of \"{self.name}\": ")
        sleep(1)

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
        print("-" * 50)
        self.date_due = datetime.datetime(get_date("year"), get_date("month"), get_date("day"))
        print("-" * 50)

        def get_tags(tags_list: list):
            print("Tags:")
            sleep(0.5)
            for index, value in enumerate(tags_list):
                print(f"{index + 1}) {value}")
            print("-" * 50)

        get_tags(tags)
        # ask the user to add any tags for the final step before displaying the task
        while True:
            selected = input("Please select tags (type done to continue or tag number): ")
            if selected == "done":  # checks if value is done to break
                break
            try:  # checks to see if the value is an int else loop again
                selected = int(selected)
            except ValueError:
                sleep(0.8)
                print("Please enter a number or 'done'!")
                continue
            if 1 > selected > len(tags):  # checks to see if it is in the range of the list index
                sleep(0.8)
                print(f"Please enter a number between 1-{len(tags)}")
                continue
            self.tags.append(tags[selected - 1])  # adds the tag to the list

        print("-" * 50)
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
        print()
        print("Creating task ", end="")
        sleep(0.6)
        print(".", end="")
        sleep(0.6)
        print(".", end="")
        sleep(0.6)
        print(".")
        sleep(1)
        print("Task created!")
        print("-" * 50)
        tasks.append(self)
        input("Press enter to continue.")
        print()
        menu()

    def delete_task(self):
        del self
