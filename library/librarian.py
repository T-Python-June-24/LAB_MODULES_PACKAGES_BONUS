def add_book(library:dict, title:str, author:str, isbn:str):
        if not isbn in library.values():
            newBook={
                    "title":title,
                    "autour":author,
                    "isbn":isbn,
                    "avaliable":True
            }
            library.update(newBook)
        else:
              print("Is alerady exist")
        

def remove_book(library, isbn):
      if isbn in library:
        del library[isbn]
      else:
           print("is not exist.")

def check_out_book(library, isbn):
     if isbn in library:
          library[isbn]["avalible"]=False
          print(f"Book with ISBN {isbn} has been checked out.")
     else:
          print("is already checked out")
 

def return_book(library, isbn):
     if isbn in library:
          library[isbn]["avalible"]=True
          print(f"Book with ISBN {isbn} has been returned.")
     else:
          print("is already avaliable")

def display_books(library):
    for i in library['0']:
        print(f'{library['title']}  {library['isbn']}- {library['avalible']}')
