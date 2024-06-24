
def add_book(library, title, author, isbn):
# cheack before add If the ISBN already exists in the library, print an appropriate message.
    if isbn in library:
        print(f'''\033[31m 
              
            The book with ISBN '{isbn}' already exists
              
              \033[34m''')
    else:
        library[isbn] = {}
        library[isbn].update(title = title,author=author,isAvabile=True)

        print(f'''\033[32m 
              
            Book with details Title: '{title}', Author: '{author}', ISBN: '{isbn}' was added successfully.
              
              \033[34m''')

def remove_book(library, isbn):
# If the ISBN does not exist in the library, print an appropriate message.
    if isbn not in library:

        print(f'''\033[31m 
              
            Can't remove book with ISBN '{isbn}' becuase it dosn't exist in the library
              
              \033[34m''')
    else:

        del library[isbn]

        print(f'''\033[33m 
              
            Book with ISBN: '{isbn}' was deleted successfully.
              
              \033[34m''')

def check_out_book(library, isbn):
# and sets the 'available' key of the book with the given ISBN to False. 
# If the ISBN does not exist in the library or the book is not available, print an appropriate message.
    if isbn not in library:

        print(f'''\033[31m 
              
            Can't check out book with ISBN '{isbn}' becuase it dosn't exist in the library
              
              \033[34m''')
        
    elif library[isbn]["isAvabile"]:

        library[isbn]["isAvabile"] = False

        print(f'''\033[33m 
              
            Book with ISBN: '{isbn}' was checked out successfully.
              
              \033[34m''')
    
    else:

        print(f'''\033[31m 
              
            Can't check out book with ISBN '{isbn}' becuase its not avaliale
              
              \033[34m''')


def return_book(library, isbn):
# nd sets the 'available' key of the book with the given ISBN to True. 
# If the ISBN does not exist in the library, print an appropriate message.
    if isbn not in library:

        print(f'''\033[31m 
              
            Can't return book with ISBN '{isbn}' becuase it dosn't exist in the library
              
              \033[34m''')
    
    else:

        library[isbn]["isAvabile"] = True
        print(f'''\033[33m 
              
            book with ISBN '{isbn}' was returned successfully
              
              \033[34m''')

def display_books(library):

    for key in library.keys():
        if library[key]["isAvabile"]:
            print(f'''\033[34m 
            {library[key]["title"]} by {library[key]["author"]} (ISBN: {key}) - Available\033[34m ''')     
        else:
            print(f'''\033[34m 
            {library[key]["title"]} by {library[key]["author"]} (ISBN: {key}) - Checked Out\033[34m ''')    

