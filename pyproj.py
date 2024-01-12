
class Item:
    def __init__(self, title, _id):
        self.title = title
        self.id = _id

    def display(self):
        print(f"ID: {self.id}, Title: {self.title}")


class Book(Item):
    def __init__(self, title, _id, author):
        super().__init__(title, _id)
        self.author = author
        self.is_borrowed = False

    def display(self):
        super().display()
        print(f"Author: {self.author}, Status: {'Borrowed' if self.is_borrowed else 'Available'}")

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False


class User(Item):
    def __init__(self, username, _id):
        super().__init__("", _id)
        self.username = username

    def display(self):
        print(f"Username: {self.username}, ", end="")
        super().display()


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def display_items(self):
        print("Books:")
        for book in self.books:
            book.display()

        print("\nUsers:")
        for user in self.users:
            user.display()

    def borrow_book(self, book_id, user_id):
        for book in self.books:
            if book.id == book_id:
                for user in self.users:
                    if user.id == user_id:
                        if book.borrow_book():
                            print("Book borrowed successfully!")
                            return True
                        else:
                            print("Book is already borrowed.")
                            return False
                print("User not found.")
                return False
        print("Book not found.")
        return False

    def return_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                book.return_book()
                print("Book returned successfully!")
                return
        print("Book not found.")


def main():
    library = Library()

    book1 = Book("C programming", 1, "Dennis Ritchie")
    book2 = Book("Operating system", 2, "Rajkumar")
    user1 = User("Keerthana", 1)
    user2 = User("Porkodi", 2)

    library.add_book(book1)
    library.add_book(book2)
    library.add_user(user1)
    library.add_user(user2)

    choice = -1
    while choice != 0:
        print("\nLibrary Management System")
        print("1. Display Library Items")
        print("2. Add Book")
        print("3. Add User")
        print("4. Borrow Book")
        print("5. Return Book")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            library.display_items()
        elif choice == 2:
            title = input("Enter book title: ")
            author = input("Enter author: ")
            book_id = int(input("Enter book ID: "))
            new_book = Book(title, book_id, author)
            library.add_book(new_book)
        elif choice == 3:
            username = input("Enter username: ")
            user_id = int(input("Enter user ID: "))
            new_user = User(username, user_id)
            library.add_user(new_user)
        elif choice == 4:
            book_id = int(input("Enter book ID to borrow: "))
            user_id = int(input("Enter user ID: "))
            library.borrow_book(book_id, user_id)
        elif choice == 5:
            book_id = int(input("Enter book ID to return: "))
            library.return_book(book_id)
        elif choice == 0:
            print("Terminating")
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()


