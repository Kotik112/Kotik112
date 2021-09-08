#TODO: Add line number when printing out library content.
#      Write and read library contents to a file.

#LIST OF METHOD DECLARATIONS
class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def print_instance(self):
        print("Book Name: {}, Author: {}, Year: {}".format(self.name, self.author, self.year))      

#LIST OF FUNCTION DECLARATIONS
def print_menu():
    print ("""
    The menu takes inputs from 1 to 5.
    ---------------------------------
    1.  Show all books available in library.
    2.  Add a new book to library.
    3.  Edit a book.
    4.  Delete a book from library
    5.  Exit Program.
    """)

def print_edit_menu():
    print ("""
    The menu takes inputs from 1 to 4.
    ---------------------------------
    1.  Change the name of a book.
    2.  Change the name of the author.
    3.  Change the year of publication.
    4.  Go back a step.
    """)


#Reads a list of objects and prints the individual elements within the object.
def print_book_list(list):
    for book in list:
        book.print_instance()
        #Add Line No

#Pre-defined list for testing and/or debugging purposes
book_list = [Book("Prisoner of Azkaban", "J. K. Rowling", 1999), Book("Roger Ackroyd", "Agatha Christie", 1981), Book("Digital Fortress", "Dan Brown", 2003)]

menu_selection = 0
while menu_selection != 5:
    print_menu()
    menu_selection = int(input("Enter your choice:"))

    if menu_selection < 1 or menu_selection > 5:
        print("You made an invalid selection!")

    elif menu_selection == 1:
        print_book_list(book_list)

    elif menu_selection == 2:
        #Adding a new book to the end of the list of books
        book_name = input("Enter the book name: ")
        author = input("Author's name: ")
        year = input("Year of publication: ")
        book_list = book_list + [Book(book_name, author, year)]

    elif menu_selection == 3:
        #Edit a book
        print_edit_menu()
        edit_choice = 0
        edit_choice = int(input("Enter your choice: "))

        if edit_choice > 4 or edit_choice < 1:
            print("You made an invalid selection.")

        elif edit_choice == 1:
            print_book_list(book_list)
            line_select = int(input("Enter book number you want to change:"))
            book_list[line_select-1].name = input("Enter the new title for the book: ")

        elif edit_choice == 2:
            print_book_list(book_list)
            line_select = int(input("Enter book number you want to change:"))
            book_list[line_select-1].author = input("Enter the new name of the Author: ")

        elif edit_choice == 3:
            print_book_list(book_list)
            line_select = int(input("Enter book number you want to change:"))
            book_list[line_select-1].year = input("Enter the new year of publication: ")

        elif edit_choice == 4:
            pass

    elif menu_selection == 4:
        #Delete a book
        print_book_list(book_list)
        line_select = int(input("Select the line you want to remove: "))
        if book_list.pop(line_select-1):
            print("Book at position {} was successfully removed.".format(line_select))

    elif menu_selection == 5:
        #Exit out of program
        raise SystemExit


#def __init__(self, name, max_students):
#   self.name = name
#   self.max_students = max_students
#   self.students = []

#  Vad är @ och -> symboler?