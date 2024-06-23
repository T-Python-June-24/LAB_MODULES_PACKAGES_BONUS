def add_book(library:dict, title:str, author:str, isbn:str):
    if isbn in library:
        print("The book is already registered to the library.")
    else:
        library[isbn] = {"title": title, "author": author, "available": True}
        print(f"The book with ISBN: {isbn} was registered successfully!")

def remove_book(library:dict, isbn:str):
    if isbn not in library:
        print("This book is not registered to the library.")
    else:
        del library[isbn]
        print(f"The book with ISBN: {isbn} was successfully removed from the library.")

def check_out_book(library:dict, isbn:str):
    if isbn not in library:
        print("This book is not registered to the library.")
    else:
        library[isbn]["available"] = False
        print(f"The book with ISBN: {isbn} has been checked-out.")

def return_book(library:dict, isbn:str):
    if isbn not in library:
        print("This book is not registered to the library.")
    else:
        library[isbn]["available"] = True
        print(f"The book with ISBN: {isbn} has been retured.")

def display_books(library:dict):
    for isbn in library:
        if library[isbn].get("available") == True:
            print(f"{library[isbn].get("title")} by {library[isbn].get("author")} (ISBN: {isbn}) - Available")
        else:
            print(f"{library[isbn].get("title")} by {library[isbn].get("author")} (ISBN: {isbn}) - Checked Out")
