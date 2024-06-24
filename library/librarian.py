
def add_book(library:dict, title:str, author:str, isbn:str):
    if "isbn" in library:
        print(f"A book with the ISBN '{isbn}' already exists in the library.")
    else : 
     library[isbn]={"title":title,
             "author":author,
             
              "available":True
    }
    print(f"The Book with the isbn ({isbn})is added sucssefuly !!")
    
    
def remove_book(library:dict, isbn:str):
     if isbn in library:
       del library[isbn]
     else :
        print("There is no existing book with the {isbn} to delete") 


def check_out_book(library:dict, isbn:str):
   if isbn not in library:
      print(f"The {isbn} does not exist in the library") 
   else:
    library[isbn]['available'] = False
    print(f"You have checked out the book with ISBN '{isbn}'.")

def return_book(library:dict, isbn:str):
   if isbn not in library:
      print(f"the given isbn {isbn} is not exist in the library")
   else :
      library[isbn]['available']=True 
def display_books(library:dict):
    for isbn in library:

        # print(f"Available: {'Available' if book['available'] else 'Checked Out'}")
        if library[isbn].get('available') == True:
         print(f"{library[isbn].get("title")} by {library[isbn].get("author")} (ISBN: {isbn}) - {'Available'} ")
        else:
          print(f"{library[isbn].get("title")} by {library[isbn].get("author")} (ISBN: {isbn}) - {'Cheacked out'} ")


