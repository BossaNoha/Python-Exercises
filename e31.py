#this code is case sensitive
class Expense_Tracker:
    def __init__(self):
        self.expenses = {} # str(category) : [expenses]
        self.error_message = "Invalid input, try again"
    
    def own_input_add_category(self):
        own_input = {input("Fill category: \n") : float(input("Fill expenses: \n"))}
        return own_input
    
    def add_category(self):
        new_entry = self.own_input_add_category()
        for cat, amount in new_entry.items():
            if cat in self.expenses:
                self.expenses[cat].append(amount)
            else:
                self.expenses[cat]=[amount]
        
    def own_input_overview(self):
        own_input = input()
        return own_input

    def todo_input(self):
        print(
            """Options:
            To view overview of expenses type: overview
            To view to overview total expenses type: total
            To add expenses type: add
            To exit type: quit
            """
            )
        todo_input = "haha"
        while todo_input not in ["overview","total","add","quit"]:    
            todo_input = input ("Please decide what will be done: \n")
            if todo_input not in ["overview","total","add","quit"]:
                print(self.error_message)
        return todo_input

    def overview(self):
        print("Select category which you want to overview:")
        category = ""
        for cat in self.expenses:
            print(cat)
        while category not in self.expenses:
            category = self.own_input_overview()
            if category not in self.expenses: print (self.error_message)
        print(self.expenses[category])

    def total(self):
        for cat in self.expenses:
            for expenses in self.expenses[cat]:
                print (expenses)
        total = sum(sum(vals) for vals in self.expenses.values())
        print(f"Total expenses in category: {total}")    

    

    def main(self):
        todo_input = self.todo_input()
        while todo_input != "quit":
            if todo_input == "overview":
                self.overview()
            elif todo_input == "total":
                self.total()
            elif todo_input == "add":
                self.add_category()
            print("What would you like to do next?")
            todo_input = self.todo_input()

run = Expense_Tracker()
run.main()