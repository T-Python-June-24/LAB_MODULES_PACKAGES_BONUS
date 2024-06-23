def add_book(library, title, author, isbn):
    book = {
        'title': title,
        'author': author,
        'isbn': isbn,
        'status': True
    }
    if any(b['isbn'] == isbn for b in library):
        print(f"The book with ISBN '{isbn}' already exists in the library.")
    else:
        library.append(book)
        print(f"The book with ISBN '{isbn}' has been added.")

def remove_book(library, isbn):
    for book in library:
        if book['isbn'] == isbn:
            library.remove(book)
            print(f"The book with ISBN '{isbn}' has been removed.")
            return
    print(f"The book with ISBN '{isbn}' does not exist in the library.")

def check_out_book(library, isbn):
    for book in library:
        if book['isbn'] == isbn:
            if book['status']:
                book['status'] = False
                print(f"The book with ISBN '{isbn}' has been checked out.")
            else:
                print(f"The book with ISBN '{isbn}' is already checked out.")
            return
    print(f"The book with ISBN '{isbn}' does not exist in the library.")

def return_book(library, isbn):
    for book in library:
        if book['isbn'] == isbn:
            if not book['status']:
                book['status'] = True
                print(f"The book with ISBN '{isbn}' has been returned.")
            else:
                print(f"The book with ISBN '{isbn}' was not checked out.")
            return
    print(f"The book with ISBN '{isbn}' does not exist in the library.")

def display_books(library):
    print("\nLibrary Collection:")
    for i,book in enumerate(library, start=1):
        status = "Available" if book['status'] else "Checked Out"
        print(f"{i}- {book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")
