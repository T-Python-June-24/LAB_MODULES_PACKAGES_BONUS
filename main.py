from library import librarian 
library_dict={}
librarian.add_book(library_dict,"The Catcher in the Rye","J.D. Salinger", "9780316769174")
librarian.add_book(library_dict,"To Kill a Mockingbird","Harper Lee", "9780446310789")
librarian.add_book(library_dict,"1984","George Orwell", "9780451524935")
librarian.display_books(library_dict)
print()
librarian.check_out_book(library_dict,"9780316769174")
librarian.display_books(library_dict)
print()

librarian.return_book(library_dict,"9780316769174")
librarian.display_books(library_dict)
print()

librarian.remove_book(library_dict,"9780446310789")
librarian.display_books(library_dict)
print()

# The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Available
# To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
# 1984 by George Orwell (ISBN: 9780451524935) - Available

# The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Checked Out
# To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
# 1984 by George Orwell (ISBN: 9780451524935) - Available

# The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Available
# To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
# 1984 by George Orwell (ISBN: 9780451524935) - Available