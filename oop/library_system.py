class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_details(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    
    def get_details(self):
        return f"{super().get_details()} [E-book, {self.file_size}MB]"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    
    def get_details(self):
        return f"{super().get_details()} [Print Book, {self.page_count} pages]"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only instances of Book or its subclasses can be added.")
    
    def list_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            for book in self.books:
                print(book.get_details())

# Sample usage
if __name__ == "__main__":
    library = Library()
    
    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
    
    # Add books to the library
    library.add_book(classic_book)
    library.add_book(digital_novel)
    library.add_book(paper_novel)
    
    # List all books in the library
    library.list_books()

