class ContactBook:  
    def __init__(self):
        self.book = {}

    def add_contact(self, new_contact):
        self.book.update(new_contact)

    def show_contacts(self):
        for contact in sorted(self.book):
            print(contact, self.book[contact])

    def remove_contact(self, removed_contact):
        if removed_contact in self.book:
            self.book.pop(removed_contact)
        else:
            print("Contact not found")

        

    

book = ContactBook()
book.add_contact({"Alice" : "12345"})
book.add_contact({"Bob" : "67890"})
book.show_contacts()
book.remove_contact("Alice")
book.show_contacts()
