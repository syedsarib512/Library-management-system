class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.is_admin = False

class Librarian(User):
    def __init__(self, user_id, username, password):
        super().__init__(user_id, username, password)
        self.is_admin = True

class Book:
    def __init__(self, book_id, title, author, ISBN, available_copies, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available_copies = available_copies
        self.total_copies = total_copies

class Transaction:
    def __init__(self, transaction_id, user_id, book_id, due_date):
        self.transaction_id = transaction_id
        self.user = user_id
        self.book = book_id
        self.checkout_date = None
        self.due_date = due_date
        self.return_date = None

class Library:
    def __init__(self):
        self.users = {}  # Dictionary to store users (user_id: User object)
        self.books = {}  # Dictionary to store books (book_id: Book object)
        self.transactions = {}  # Dictionary to store transactions (transaction_id: Transaction object)

    def add_user(self, user):
        self.users[user.user_id] = user

    def add_book(self, book):
        self.books[book.book_id] = book

    # Other methods for managing the library system

# Console-based UI class for interaction with users
class ConsoleUI:
    def __init__(self, library):
        self.library = library

    def run(self):
        # Implement console-based UI to interact with the library system and users
        print("Wellcome To Console Based Library Management Sysytem")
        print("1. Librarian\n 2. Student or Teacher")







# Example Usage:

# Create a library instance

library = Library()

# Add users and books to the library
librarian = Librarian(1, "admin", "admin_password")
user1 = User(2, "user1", "user1_password")
book1 = Book(1, "Book Title 1", "Author 1", "ISBN123", 5, 10)

library.add_user(librarian)
library.add_user(user1)
library.add_book(book1)

# Initialize the console-based UI and run the system
ui = ConsoleUI(library)
ui.run()
