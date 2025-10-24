class Main:  
    def __init__(self):
        self.todolist = []

    def add_task(self):
        #task = {name : input, status : pending, estimated time : input, spent : 0 }
        task_name = input("What shall be name of the task?")
        estimated_time = input(f"How much time do you expect to be finish {task_name}")
        new_task = {"name" : task_name, "status" : "pending", "estimated time" : float(estimated_time), "spent" : 0, "remaining time" : float(estimated_time) }
        self.todolist.append(new_task)

    def show_list(self): 
        if self.todolist != []:
            for task in self.todolist:
                print(f"{task['name']} | Status: {task['status']} | Est: {task['estimated time']} | Spent: {task['spent']} | Remaining: {task['remaining time']}")
        else: print("to do list seems to be empty")

    def progressed_task(self):
        task_name = input("On what task did you already work?")
        spent_time = float(input("How much time did you spend doing it?"))
        enough_time = ""
        while enough_time != "y" and enough_time != "n":
            enough_time = input("Was it enough? (y/n)")
            if enough_time != "y" and enough_time != "n": print("Invalid entry")
        for task in self.todolist:
            if task["name"] == task_name:
                task["spent"] += spent_time
                if enough_time == "y":
                    task["status"] = "done"
                    task["remaining time"] = 0
                else: 
                    if task["remaining time"] > spent_time:
                        task["remaining time"] -= spent_time
                    else: task["remaining time"]=float(input("Since time spent has exceeded expected time, how much time do you think you will need to complete this task?"))

    def my_UI(self):
        my_input = ""
        while my_input != "quit":
            print(f"Choose one of the following options: \n add task \n quit \n show list \n progress task")
            my_input = input("What would you like to do?").lower()
            if my_input == "quit": print("quitting")
            elif my_input == "add task": self.add_task()
            elif my_input == "show list": self.show_list()
            elif my_input == "progress task": self.progressed_task()
            else: print("Invalid input, try again")




my_list = Main()
my_list.my_UI()