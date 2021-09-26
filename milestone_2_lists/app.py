from utils import database

USER_CHOICE = """
    Enter:
    - 'a' to add a new book
    - 'l' to lista all books
    - 'r' to mark a book as read
    - 'd' to delete a book
    - 'q' to quit
    
    Your choice:"""

def menu():
    user_imput = input(USER_CHOICE)
    while user_imput != 'q':
        pass

    # def prompt_add_book() ask for book name and author
    # def list_books() show all the books in our list
    # def primpt_read_book()