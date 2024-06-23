from library import librarian
library=[]

# Defined books as required
librarian.add_book(library,"The Catcher in the Rye","J.D. Salinger", "9780316769174")
librarian.add_book(library,"To Kill a Mockingbird","Harper Lee", "9780446310789")
librarian.add_book(library,"1984","George Orwell", "9780451524935")

# EXTRA WORK
def print_menu():
    print("\nLibrary Menu:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Check Out Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")


while True:
    print_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        librarian.add_book(library, title, author, isbn)
    elif choice == '2':
        isbn = input("Enter book ISBN to remove: ")
        librarian.remove_book(library, isbn)
    elif choice == '3':
        isbn = input("Enter book ISBN to check out: ")
        librarian.check_out_book(library, isbn)
    elif choice == '4':
        isbn = input("Enter book ISBN to return: ")
        librarian.return_book(library, isbn)
    elif choice == '5':
        librarian.display_books(library)
    elif choice == '6':
        print("Exiting the library system...\nGoodBye :)")
        break
    else:
        print("Invalid choice. Please try again.")





