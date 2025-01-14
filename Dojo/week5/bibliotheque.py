class Library:
    def __init__(self):
        self.books =[]

    def add_book(self, title, author):
        book = {"title" : title, 
                "author" : author, 
                "borrowed" : False }
        self.books.append(book)
        print(f"The book '{title}' by {author} has been added to the library")
            
    
    def search_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                print(f"The book '{title}' is in the library")
                return book
        print(f"The book '{title}' is not in the library")
            
    
    def borrow_book(self, title):
        book = self.search_book(title)
        if book is None:
            raise ValueError(f"The book '{title}' doesn't exists.")
        if not book["borrowed"]:
            book["borrowed"]= True
            print(f"The book '{title}' is not available.")
        else:
            raise ValueError(f"The book '{title}' is borrowed.")
    
    def return_book(self, title):
        book = self.search_book(title)
        if book is None:
            raise ValueError(f"The book '{title}' doesn't exist.")
        if book["borrowed"]:
            book["borrowed"] = False
            print(f"The book '{title}' has been returned.")
        else:
            raise ValueError(f"The book '{title}' is not borrowed.")

