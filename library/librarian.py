def add_book(library:dict, title:str, author:str, isbn:str, available = True):
    if isbn not in library:
        library[isbn]={}
        library[isbn]["title"] = title
        library[isbn]["author"] = author
        library[isbn]["available"] = available
        print(f"{library[isbn]["title"]} by {library[isbn]["author"]} (ISBN: {isbn}) has been added to the library")
    else:
        print(f"You have already added the book: {library[isbn]["title"]}, ISBN: {isbn} to the library.")

def remove_book(library, isbn):
    if isbn in library:
        title = library[isbn]['title']
        author = library[isbn]['author']
        del library[isbn]
        print(f"{title} by {author} (ISBN: {isbn}) has been removed from the library")
    else:
        print(f"The book: {library[isbn]["title"]}, ISBN: {isbn} does not exist in the library.")


def check_out_book(library, isbn):
    if isbn in library:
        if library[isbn]["available"]:
            library[isbn]['available'] = False
            print(f"{library[isbn]["title"]} by {library[isbn]["author"]} (ISBN: {isbn}) has been ckecked out.")
        else:
            print(f"{library[isbn]["title"]} by {library[isbn]["author"]} (ISBN: {isbn}) has already been ckecked out.")
    else:
        print(f"The book with ISBN: {isbn} does not exist in the library.")


def return_book(library, isbn):
    if isbn in library:
        if not library[isbn]["available"]:
            library[isbn]['available'] = True
            print(f"{library[isbn]["title"]} by {library[isbn]["author"]} (ISBN: {isbn}) has been returned.")
        else:
            print(f"{library[isbn]["title"]} by {library[isbn]["author"]} (ISBN: {isbn}) is already available in the library.")
    else:
        print(f"The book with ISBN: {isbn} does not exist in the library.")


def display_books(library):
    for isbn in library:
        if library[isbn]["available"] == True:
            print(f"{library[isbn]["title"]} by {library[isbn]["author"]} (ISBN: {isbn}) - Available")
        else:
            print(f"{library[isbn]["title"]} by {library[isbn]["author"]} (ISBN: {isbn}) - Ckecked Out")

