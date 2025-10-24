class BookstoreInventoryManager:
    def __init__(self):
        self.BS_inventory = {}

    def book_info(self, name):
        #name, author, qty, price
        author = input("Insert authors name:\n")
        qty = int(input("Insert bought quantity:\n"))
        buy_price = float(input("Insert buy price:\n"))
        sell_price = float(input("Insert sell price:\n"))
        availability = 1 
        book_info = {"author" : author, "qty" : qty, "buy price" :buy_price, "sell price" : sell_price, "availability" : availability}
        self.BS_inventory[name] = book_info

    def add_book(self):
        name = input("Insert name of the book:\n")
        if name not in self.BS_inventory:
            self.book_info(name)
        else: 
            qty = int(input("Insert amount of bought books:"))
            self.BS_inventory[name]["qty"] += qty
        if self.BS_inventory[name]["qty"] > 0: 
            self.BS_inventory[name]["availability"] = 1
        else: self.BS_inventory[name]["availability"] = 0

    def BS_showcase(self):
        BS_showcase = []
        for book in self.BS_inventory:
            if self.BS_inventory[book]["availability"] == 1: 
                BS_showcase.append(book)
        print(BS_showcase)

    def view_inventory(self):
        BS_inventory = {}
        for book in self.BS_inventory:
            if self.BS_inventory[book]["availability"] == 1:
                BS_inventory[book]=self.BS_inventory[book]
        print(BS_inventory)

    def sell_book(self):
        name = ""
        while name not in self.BS_inventory: 
            name = input("Insert name of the book:\n")
            if name not in self.BS_inventory:
                print("Invalid book")
        else: 
            qty = int(input("Insert amount of sold books:"))
            self.BS_inventory[name]["qty"] -= qty
        if self.BS_inventory[name]["qty"] > 0: 
            self.BS_inventory[name]["availability"] = 1
        else: self.BS_inventory[name]["availability"] = 0

    def my_UI(self):
        my_input = 0
        while my_input != 6:
            print("List of options:\n 1 Add book\n 2 Sell book\n 3 View available books to customer\n 4 Check available books\n 5 Check total store value\n 6 Quit\nTo select insert responsive number")
            try:
                my_input = int(input("Your choice: "))
            except ValueError:
                print("Invalid input — please enter a number from 1 to 6.\n")
                continue  # jump back to the top of the loop

            if my_input == 1:
                self.add_book()
            elif my_input == 2:
                self.sell_book()
            elif my_input == 3:
                self.BS_showcase()
            elif my_input == 4:
                self.view_inventory()
            elif my_input == 5:
                self.total_store_value()
            elif my_input == 6:
                print("Exiting Bookstore Inventory Manager. Goodbye!")
            else:
                print("Invalid choice — please select between 1 and 6.\n")

                        
    def total_store_value(self):
        BS_inventory = {}
        for book in self.BS_inventory:
            if self.BS_inventory[book]["availability"] == 1:
                total_sell = self.BS_inventory[book]["qty"]*self.BS_inventory[book]["sell price"]
                total_buy = self.BS_inventory[book]["qty"]*self.BS_inventory[book]["buy price"]
                book_info = {"qty" : self.BS_inventory[book]["qty"], "total buy price" : total_buy, "total sell price" : total_sell}
                BS_inventory[book] = book_info
        print (BS_inventory)
                
bsinv = BookstoreInventoryManager()
bsinv.my_UI()