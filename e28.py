class Librarys:
    def __init__(self):
        self.books = []
    
    def add_book(self, new_book):
        self.books.append(new_book)
    
    def show_books(self):
        i = 1 
        for book in sorted(self.books):
            print (f"{i}. {book}")
            i +=1

    def remove_book(self, removed_book):
        if removed_book in self.books:
            self.books.remove(removed_book)
        else: print (f"{removed_book} was not found")


library = Librarys()
library.add_book("1984")
library.add_book("Brave New World")
library.show_books()
library.remove_book("1984")
library.show_books()