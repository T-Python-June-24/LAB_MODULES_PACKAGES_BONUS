mydict={"title":'red line','isbn':'1234','available':True}
from library import librarian as lib
lib.add_book(mydict,'blue line','saeed','54')
lib.remove_book(mydict,'1234')
lib.check_out_book(mydict,'1234')
lib.return_book(mydict,'1234')
lib.return_book(mydict,'1234')