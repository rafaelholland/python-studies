# Concerned with storing and retrieving books from a json file.
import sqlite3


def create_book_table():
    connect = sqlite3.connect('data.db')
    cursor = connect.cursor()

    cursor.execute('create table if not exists books(name text primary key, author text, read integer)')
    connect.commit()
    connect.close()


def add_book(name, author):
    #
    connect = sqlite3.connect('data.db')
    cursor = connect.cursor()
    try:
        cursor.execute('INSERT INTO BOOKS VALUES (?, ?, 0)', (name, author))
    except:
        print('Book already listed on our database')

    connect.commit()
    connect.close()


def get_all_books():
    connect = sqlite3.connect('data.db')
    cursor = connect.cursor()

    cursor.execute('select * from books')
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in
             cursor.fetchall()]  # [(name, author, read), (name, author, read)]
    connect.close()
    return books


def mark_book_as_read(name):
    connect = sqlite3.connect('data.db')
    cursor = connect.cursor()

    cursor.execute('update books set read = 1 where name = ?', (name,))

    connect.commit()
    connect.close()


def delete_book(name):
    connect = sqlite3.connect('data.db')
    cursor = connect.cursor()

    cursor.execute('delete from books where name = ?', (name,))

    connect.commit()
    connect.close()
