# Concerned with storing and retrieving books from a list.

books = []

def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})