import sqlite3

class Library:
    def __init__(self):
        """Initialize the library and create the database connection."""
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()
        self.create_books_table()

    def create_books_table(self):
        """Create a table to store book information."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
            book_id TEXT PRIMARY KEY,
            title TEXT,
            author TEXT,
            year INTEGER,
            available INTEGER,
            max_Books INTEGER
        )''')
        self.conn.commit()

    def add_book(self, book_id, title, author, year, available,max_Books):
        """Add a book to the library."""
        self.cursor.execute("INSERT INTO books (book_id, title, author, year, available,max_Books) VALUES (?, ?, ?, ?, ?,?)",
                            (book_id, title, author, year, available,max_Books))
        self.conn.commit()

    def borrow_book(self, book_id):
        """Borrow a book from the library."""
        self.cursor.execute("SELECT * FROM books WHERE book_id = ? AND available > 0", (book_id,))
        book = self.cursor.fetchone()
        if book:
            self.cursor.execute("UPDATE books SET available = available - 1 WHERE book_id = ?", (book_id,))
            self.conn.commit()
            return {'book_id': book[0], 'title': book[1], 'author': book[2], 'year': book[3], 'available': book[4] - 1,'max_Books': book[5]}
        return None

    def return_book(self, book_id):
        """Return a borrowed book to the library."""
        # Retrieve the book information from the database
        self.cursor.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
        book = self.cursor.fetchone()

        if book:
            # Check if the book is currently borrowed
            available = book[4]  # available field is at index 4
            max_books = book[5]  # max_books field is at index 5

            # If the book is borrowed (available is 0), we can return it
            if available < max_books:
                # Update the availability count (increment available)
                self.cursor.execute("UPDATE books SET available = available + 1 WHERE book_id = ?", (book_id,))
                self.conn.commit()

                # Fetch the updated book information and return it
                self.cursor.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
                updated_book = self.cursor.fetchone()

                return {'book_id': updated_book[0], 'title': updated_book[1], 'author': updated_book[2], 'year': updated_book[3], 'available': updated_book[4]}

            else:
                # If the book wasn't borrowed, notify the user
                return None
        else:
            return None


    def view_available_books(self):
        """Get a list of available books."""
        self.cursor.execute("SELECT * FROM books WHERE available > 0")
        books = self.cursor.fetchall()
        available_books = []
        for book in books:
            available_books.append({'book_id': book[0], 'title': book[1], 'author': book[2], 'year': book[3], 'available': book[4],'max_Books': book[5]})
        return available_books
    
    def clear_db(self):
        try:
            self.cursor.execute("DELETE FROM books")
            #self.cursor.execute("DELETE FROM borrowed_books")
            self.conn.commit()
            print("Database cleared successfully.")
        except sqlite3.Error as e:
            print(f"Error clearing the database: {e}")
        finally:
            pass