class Book():

    def __init__(self, book, author, pages):
        self.book = book
        self.author = author
        self.page = pages
    
    def __str__(self) -> str:   # returns back the acual string representation
        return (f"{self.book} by {self.author}")

    def __len__(self):    # return back the length of the object
        return self.page
    
    def __del__(self):
        print("A book object has been deleted")
book1 = Book(book="Python rocks", author="Jose", pages=200)
print(book1)
print(len(book1))

del book1  # delete variables from memory

print(book1)