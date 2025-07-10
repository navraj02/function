class library:
    
    def __init__(self,name):
        self.name=name 
        self.books=[]
        
    def display_book(self):
        if self.books:
            print(f"books available in {self.name}:")
            for book in self.books:
                print(f"-{book}")
                
        else:
            print("no book is vailable in {self.name}.")
            
    def add_book(self,books):
        self.books.append(books)
        print(f"book'{books}'added to {self.name}.")
        
    def remove_book(self,books):
        if books in self.books:
            self.books.remove(books)
            print(f"book'{books}'removed from {self.name}")
        else:
            print(f"book'{books}'not found in {self.name}")
            
            
            
my_library=library("city library")

my_library.add_book("YOU CAN WIN")
my_library.add_book("A CUT LIKE WOUND")
my_library.add_book("A SUITABLE BOY")
my_library.add_book("KITE RUNNER")

my_library.display_book()

my_library.remove_book("KITE RUNNER")

#display books after removing
my_library.display_book()