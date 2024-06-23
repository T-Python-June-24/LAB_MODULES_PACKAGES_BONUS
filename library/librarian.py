def add_book(library:dict, title:str, author:str, isbn:str):
    """Adds a book to the library

    Args:
        library (dict): The library to add the book to
        title (str): The title of the book
        author (str): The author of the book
        isbn (str): The ISBN of the book
    """
    if not title or not author or not isbn:
        print("Invalid input: Title, author, and ISBN must be provided")
        return
    if isbn in library:
        print("Book already exists")
    else:
        library[isbn] = {"title": title, "author": author, "checked_out": "Available"}
        print(f"Book {title} by {author} added to the library") 

def remove_book(library:dict, isbn:str):
    """Removes a book from the library

    Args:
        library (dict): The library to remove the book from
        isbn (str): The ISBN of the book
    """
    if not isbn:
        print("Invalid input: ISBN must be provided")
        return
    if isbn in library:
        del library[isbn]
        print(f"Book {library[isbn]['title']} by {library[isbn]['author']} removed from the library")
    else:
        print("Book not found")

def check_out_book(library:dict, isbn:str):
    """Checks out a book from the library

    Args:
        library (dict): The library to check out the book from
        isbn (str): The ISBN of the book
    """
    if not isbn:
        print("Invalid input: ISBN must be provided")
        return
    if isbn in library:
        if library[isbn]["checked_out"] == "Not Available":
            print("Book is already checked out")
        else:
            library[isbn]["checked_out"] = "Not Available"
            print(f"Book {library[isbn]['title']} by {library[isbn]['author']} checked out")
    else:
        print("Book not found")

def return_book(library:dict, isbn:str):
    """Returns a book to the library

    Args:
        library (dict): The library to return the book to
        isbn (str): The ISBN of the book
    """
    if not isbn:
        print("Invalid input: ISBN must be provided")
        return
    if isbn in library:
        if library[isbn]["checked_out"] == "Available":
            print("Book is already available")
        else:
            library[isbn]["checked_out"] = "Available"
            print(f"Book {library[isbn]['title']} by {library[isbn]['author']} returned to the library")
    else:
        print("Book not found")

def display_books(library:dict):
    """Displays all books in the library

    Args:
        library (dict): The library to display the books from
    """
    if not library:
        print("No books in the library")
        return
    for isbn, book in library.items():
        print(f"{book['title']} by {book['author']}, (ISBN: {isbn}) - {book['checked_out']}")