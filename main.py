from library.librarian import add_book, remove_book, check_out_book, return_book, display_books


library = {}
try:
    add_book(library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
except Exception as e:
    print(f"Error adding book: {e}")

try:
    add_book(library, "To Kill a Mockingbird    ", "Harper Lee", "9780446310789")
except Exception as e:
    print(f"Error adding book: {e}")

try:
    add_book(library, "1984", "George Orwell", "9780451524935")
except Exception as e:
    print(f"Error adding book: {e}")

try:
    check_out_book(library, "9780316769174")
except Exception as e:
    print(f"Error checking out book: {e}")

try:
    return_book(library, "9780316769174")
except Exception as e:
    print(f"Error returning book: {e}")

try:
    remove_book(library, "9780316769174")
except Exception as e:
    print(f"Error removing book: {e}")

try:
    display_books(library)
except Exception as e:
    print(f"Error displaying books: {e}")