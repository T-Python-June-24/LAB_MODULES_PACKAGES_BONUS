from library.librarian import *
library:dict = {}
# Adding books
add_book(library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
add_book(library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
add_book(library, "1984", "George Orwell ", "9780451524935")
print()
display_books(library)
print()

# Checking a book out
check_out_book(library, "9780316769174")
print()
display_books(library)
print()

# Returning the checked out book
return_book(library, "9780316769174")
print()
display_books(library)

# Removing a book
remove_book(library, "9780316769174")
print()
display_books(library)
print()

