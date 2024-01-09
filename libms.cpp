#include <iostream>
#include <vector>
#include <string>
using namespace std;
class Item {
protected:
    string title;
    int id;

public:
    Item(string _title, int _id) : title(_title), id(_id) {}

    virtual void display() =0 ;
        
    

    
};

class Book : public Item {
private:
    string author;
    bool isBorrowed;

public:
    Book(string _title, int _id, string _author) : Item(_title, _id), author(_author), isBorrowed(false) {}

    void display() override {
        cout << "ID: " << id << ", Title: " << title << endl;
        cout << "Author: " << author << ", Status: " << (isBorrowed ? "Borrowed" : "Available") << endl;
    }

    bool borrowBook() {
        if (!isBorrowed) {
            isBorrowed = true;
            return true;
        }
        return false;
    }

    void returnBook() {
        isBorrowed = false;
    }
     int getID()  {
        return id;
    }
};

class User : public Item {
private:
    string username;

public:
    User(string _username, int _id) : Item("", _id), username(_username) {}

    void display() override {
        cout << "Username: " << username << ", ";
    }
    
    int getID()  {
        return id;
    }
};

class Library {
private:
    std::vector<Book> books;
    std::vector<User> users;
    Item *ptr;

public:
    void addBook(Book& book) {
        books.push_back(book);
    }

    void addUser(User& user) {
        users.push_back(user);
    }

    void displayItems()  {
        cout << "Books:" << endl;
        for ( auto& book : books) {
            ptr=&book;
            ptr->display();
        }

        cout << "\nUsers:" << endl;
        for ( auto& user : users) {
            ptr=&user;
            ptr->display();
        }
    }

    bool borrowBook(int bookID, int userID) {
        for (auto& book : books) {
            if (book.getID() == bookID) {
                for (auto& user : users) {
                    if (user.getID() == userID) {
                        if (book.borrowBook()) {
                            cout << "Book borrowed successfully!" << endl;
                            return true;
                        } else {
                            cout << "Book is already borrowed." << endl;
                            return false;
                        }
                    }
                }
                cout << "User not found." << endl;
                return false;
            }
        }
        cout << "Book not found." << endl;
        return false;
    }

    void returnBook(int bookID) {
        for (auto& book : books) {
            if (book.getID() == bookID) {
                book.returnBook();
                cout << "Book returned successfully!" << endl;
                return;
            }
        }
        cout << "Book not found." << endl;
    }
};

int main() {
    Library library;
    
    Book book1("C programming", 1, "Dennis Ritchie");
    Book book2("Operating system", 2, "Rajkumar");
    User user1("Keerthana", 1);
    User user2("Porkodi", 2);

    library.addBook(book1);
    library.addBook(book2);
    library.addUser(user1);
    library.addUser(user2);

    int choice;
    do {
        cout << "\nLibrary Management System\n";
        cout << "1. Display Library Items\n";
        cout << "2. Add Book\n";
        cout << "3. Add User\n";
        cout << "4. Borrow Book\n";
        cout << "5. Return Book\n";
        cout << "0. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                library.displayItems();
                break;
            case 2: {
                string title, author;
                int id;
                cout << "Enter book title: ";
                cin.ignore();
                getline(std::cin, title);
                cout << "Enter author: ";
                getline(std::cin, author);
                cout << "Enter book ID: ";
                cin >> id;
                Book newBook(title, id, author);
                library.addBook(newBook);
                break;
            }
            case 3: {
                string username;
                int id;
                cout << "Enter username: ";
                cin.ignore();
                getline(std::cin, username);
                cout << "Enter user ID: ";
                cin >> id;
                User newUser(username, id);
                library.addUser(newUser);
                break;
            }
            case 4: {
                int bookID, userID;
                cout << "Enter book ID to borrow: ";
                cin >> bookID;
                cout << "Enter user ID: ";
                cin >> userID;
                library.borrowBook(bookID, userID);
                break;
            }
            case 5: {
                int bookID;
                cout << "Enter book ID to return: ";
                cin >> bookID;
                library.returnBook(bookID);
                break;
            }
            case 0:
                cout << "Terminating\n";
                break;
            default:
                cout << "Invalid choice. Please enter a valid option.\n";
                break;
        }

    } while (choice != 0);

    return 0;
}
