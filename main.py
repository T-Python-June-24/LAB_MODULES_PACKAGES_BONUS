from library.librarian import add_book,display_books,check_out_book,return_book 

# manage a simple library system
try:

    library = {}

    add_book(library,"The Catcher in the Rye","J.D. Salinger","9780316769174")
    add_book(library,"To Kill a Mockingbird","Harper Lee","9780446310789")
    add_book(library,"1984","George Orwell","9780451524935")
    display_books(library)
    check_out_book(library,"9780316769174")
    display_books(library)
    return_book(library,"9780316769174")
    display_books(library)

except Exception as e:

        print(f'''\033[31m 

            Error: {e}

              \033[34m''')

# output 

# The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Available
# To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
# 1984 by George Orwell (ISBN: 9780451524935) - Available

# The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Checked Out
# To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
# 1984 by George Orwell (ISBN: 9780451524935) - Available

# The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Available
# To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
# 1984 by George Orwell (ISBN: 9780451524935) - Available
