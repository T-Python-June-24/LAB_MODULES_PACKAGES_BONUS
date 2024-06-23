# main.py content

from library.librarian import add_book, remove_book, check_out_book, return_book, display_books

# Initialize the library dictionary
library = {}

add_book(library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
add_book(library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
add_book(library, "1984", "George Orwell", "9780451524935")
display_books(library)

remove_book(library, "9780451524935")
display_books(library)

#check out a book
check_out_book(library, "9780451524935")
display_books(library)


check_out_book(library, "9780316769174")
display_books(library)



check_out_book(library, "9780316769174")
display_books(library)

# Display books 
display_books(library)

# Return a book
return_book(library, "9780316769174")
display_books(library)

