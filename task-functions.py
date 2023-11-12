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
        "Family"
        "Hard",
        "Easy",
        "Boring"]


class Task:
    def __init__(self):
        self.name = "Placeholder"  # for all prop. it will just assign default values obviously tbc
        self.date_due = datetime.datetime(2000, 1, 1)
        self.description = "This is a basic task description."
        self.tags = []

    def create_task(self, tasks):
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
            for i, v in enumerate(tags_list):
                print(f"{i + 1}) {v}")
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
        print({self.description})
        print(f"Date due: {self.date_due}")
        print(f"Task name:", end=" ")
        for i, v in enumerate(self.tags):
            if i != len(self.tags):
                print(v, end=", ")
            else:
                print(v)
        print("-" * 50)
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

    def delete_task(self, tasks):
        del self
        # print("Please select a task to delete: ")
        # for i, v in enumerate(tasks):
        #     print(f"{i + 1}) {v.name}")
        #
        # while True:
        #     selected = input("Please type in the number to delete (or done to exit): ")
        #
        #     if selected == "done":  # checks if value is done to break
        #
        #
        #     try:  # checks to see if the value is an int else loop again
        #         selected = int(selected)
        #     except ValueError:
        #         sleep(0.8)
        #         print("Please enter a number or 'done'!")
        #         continue
        #
        #     if 1 > selected > len(tasks):  # checks to see if it is in the range of the list index
        #         sleep(0.8)
        #         print(f"Please enter a number between 1-{len(tasks)}")
        #         continue

        # confirmation = input(f"Please type in the name of the task ({tasks[selected].name})")
