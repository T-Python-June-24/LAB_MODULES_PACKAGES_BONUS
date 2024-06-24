def add_book(library, title:str, author:str, isbn:str):
    if isbn in library:
        print(f"The book with ISBN {isbn} already exists in the library.")
    else:
        library[isbn] = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True
        }
        print(f"Book '{title}' by {author} added to the library.")

def remove_book(library, isbn:str):
    if isbn in library:
        removed_book = library.pop(isbn)
        print(f"Book '{removed_book['title']}' by {removed_book['author']} removed from the library.")
    else:
        print(f"No book found with ISBN {isbn}.")

def check_out_book(library, isbn:str):
    if isbn in library:
        if library[isbn]['available']:
            library[isbn]['available'] = False
            print(f"Book '{library[isbn]['title']}' checked out.")
        else:
            print(f"Book '{library[isbn]['title']}' is already checked out.")
    else:
        print(f"No book found with ISBN {isbn}.")

def return_book(library, isbn:str):
    if isbn in library:
        if not library[isbn]['available']:
            library[isbn]['available'] = True
            print(f"Book '{library[isbn]['title']}' returned.")
        else:
            print(f"Book '{library[isbn]['title']}' was not checked out.")
    else:
        print(f"No book found with ISBN {isbn}.")

def display_books(library):
    if library:
        for isbn, book in library.items():
            status = 'Available' if book['available'] else 'Checked out'
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {isbn}, - {status}")
    else:
        print("The library is empty.")
