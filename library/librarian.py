
'''

   - `add_book(library, title, author, isbn)` - takes a dictionary (library), a title (string), an author (string), 
   and an ISBN (string) as input, and adds a new book to the library as a dictionary with the keys 'title', 'author', 'isbn', and 'available'.
   The 'available' key should have a boolean value, 
   initially set to True. If the ISBN already exists in the library, print an appropriate message.


   - `remove_book(library, isbn)` - takes a dictionary (library) and an ISBN (string) as input,
   and removes the book with the given ISBN from the library. If the ISBN does not exist in the library,
   print an appropriate message.


   - `check_out_book(library, isbn)` - takes a dictionary (library) and an ISBN (string) as input,
   and sets the 'available' key of the book with the given ISBN to False. 
   If the ISBN does not exist in the library or the book is not available,
   print an appropriate message.


   - `return_book(library, isbn)` - 
   takes a dictionary (library) and an ISBN (string) as input, and sets the 'available' key of the book with the given ISBN to True.
   If the ISBN does not exist in the library, print an appropriate message.

   
   - `display_books(library)` - takes a dictionary (library) as input and prints all the books in the library in a formatted way.

'''



def add_book(library,title ,author,isbn):
    if isbn in library:
        print(f"Book with isbn: {isbn}. is already exists in the library ✅.")
    else:
        library[isbn] = {'title': title, 'author': author, 'isbn': isbn, 'available': True}
        print(f"The Book with isbn: {isbn}  is added to the library 📚.\n \nthank you 🩵 \n")


def remove_book(library, isbn):
     if isbn in library:
        del library[isbn]
        print(f"The Book with isbn: {isbn} .\n\n has been deleted from the library 👋.\n")
     else:
        print(f"Book with isbn: {isbn} .\n\n is dose not exists in the library 🤔.\n")



def check_out_book(library, isbn):
    if isbn not in library:
        print(f"Book with isbn: {isbn} .\n\n dose not exists in the library 🤔.\n")
    elif not library[isbn]['available']:
        print(f"Book with ISBN {isbn} is not available for checkout 😓")
    else:
        library[isbn]['available'] = False
        
        
        
def return_book(library, isbn):
    if isbn not in library:
        print(f"Book with isbn: {isbn} .\n\n is dose not exists in the library 🤔.\n")
    else:
        library[isbn]['available'] = True
        print(f"Book with ISBN {isbn} has been returned. 📚")
        



def display_books(library):
    for book in library.values():
        status = "Available" if book['available'] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")
        print("\n")