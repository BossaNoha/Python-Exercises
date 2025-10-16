class Main:  
    def __init__(self) -> None:
        self.todolist = []

    def add_task(self, newtask):
        self.todolist.append(newtask)
    
    def show_tasks(self):
        if self.todolist == []: print ("all done")
        else: 
            for task in self.todolist:
                print(task)

    def remove_task(self, donetask):
        if donetask in self.todolist:
            self.todolist.remove(donetask)
        else: 
            print("There is no such task")

my_list = Main()

todolist= []

my_list.add_task("Buy groceries")
my_list.add_task("Clean room")
my_list.show_tasks()
my_list.remove_task("Buy groceries")
my_list.show_tasks()
