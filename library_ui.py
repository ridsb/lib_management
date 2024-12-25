import tkinter as tk
from tkinter import messagebox
from library import Library  # Import the existing Library class

class LibraryUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        self.library = Library()  # Initialize the library object

        # Add Book Section
        self.add_book_frame = tk.LabelFrame(self.root, text="Add Book", padx=10, pady=10)
        self.add_book_frame.grid(row=0, column=0, padx=20, pady=10)

        self.book_id_label = tk.Label(self.add_book_frame, text="Book ID:")
        self.book_id_label.grid(row=0, column=0)
        self.book_id_entry = tk.Entry(self.add_book_frame)
        self.book_id_entry.grid(row=0, column=1)

        self.title_label = tk.Label(self.add_book_frame, text="Title:")
        self.title_label.grid(row=1, column=0)
        self.title_entry = tk.Entry(self.add_book_frame)
        self.title_entry.grid(row=1, column=1)

        self.author_label = tk.Label(self.add_book_frame, text="Author:")
        self.author_label.grid(row=2, column=0)
        self.author_entry = tk.Entry(self.add_book_frame)
        self.author_entry.grid(row=2, column=1)

        self.year_label = tk.Label(self.add_book_frame, text="Year:")
        self.year_label.grid(row=3, column=0)
        self.year_entry = tk.Entry(self.add_book_frame)
        self.year_entry.grid(row=3, column=1)

        self.available_label = tk.Label(self.add_book_frame, text="Available Copies:")
        self.available_label.grid(row=4, column=0)
        self.available_entry = tk.Entry(self.add_book_frame)
        self.available_entry.grid(row=4, column=1)

        self.add_button = tk.Button(self.add_book_frame, text="Add Book", command=self.add_book)
        self.add_button.grid(row=5, columnspan=2)

        # Borrow Book Section
        self.borrow_frame = tk.LabelFrame(self.root, text="Borrow Book", padx=10, pady=10)
        self.borrow_frame.grid(row=1, column=0, padx=20, pady=10)

        self.borrow_book_id_label = tk.Label(self.borrow_frame, text="Book ID to Borrow:")
        self.borrow_book_id_label.grid(row=0, column=0)
        self.borrow_book_id_entry = tk.Entry(self.borrow_frame)
        self.borrow_book_id_entry.grid(row=0, column=1)

        self.borrow_button = tk.Button(self.borrow_frame, text="Borrow", command=self.borrow_book)
        self.borrow_button.grid(row=1, columnspan=2)

        # Return Book Section
        self.return_frame = tk.LabelFrame(self.root, text="Return Book", padx=10, pady=10)
        self.return_frame.grid(row=2, column=0, padx=20, pady=10)

        self.return_book_id_label = tk.Label(self.return_frame, text="Book ID to Return:")
        self.return_book_id_label.grid(row=0, column=0)
        self.return_book_id_entry = tk.Entry(self.return_frame)
        self.return_book_id_entry.grid(row=0, column=1)

        self.return_button = tk.Button(self.return_frame, text="Return", command=self.return_book)
        self.return_button.grid(row=1, columnspan=2)

        # View Available Books Section
        self.view_button = tk.Button(self.root, text="View Available Books", command=self.view_books)
        self.view_button.grid(row=3, column=0, pady=10)

        # Clear Database Button
        self.clear_button = tk.Button(self.root, text="Clear Database", command=self.clear_database)
        self.clear_button.grid(row=3, column=1, pady=10)

        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.grid(row=4, column=0, padx=20, pady=10)

    def add_book(self):
        """Add a book to the library."""
        book_id = self.book_id_entry.get()
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        available = self.available_entry.get()
        max_Books = available

        if not book_id or not title or not author or not year or not available:
            messagebox.showwarning("Input Error", "All fields must be filled!")
            return

        self.library.add_book(book_id, title, author, int(year), int(available), int(max_Books))
        messagebox.showinfo("Success", f"Book '{title}' added successfully!")

    def borrow_book(self):
        """Borrow a book from the library."""
        book_id = self.borrow_book_id_entry.get()

        if not book_id:
            messagebox.showwarning("Input Error", "Please enter a book ID!")
            return

        book = self.library.borrow_book(book_id)

        if book:
            messagebox.showinfo("Success", f"Book '{book['title']}' borrowed successfully!")
        else:
            messagebox.showwarning("Borrowing Failed", "Book not available!")

    def return_book(self):
        """Return a borrowed book."""
        book_id = self.return_book_id_entry.get()

        if not book_id:
            messagebox.showwarning("Input Error", "Please enter a book ID!")
            return

        book = self.library.return_book(book_id)

        if book:
            messagebox.showinfo("Success", f"Book '{book['title']}' returned successfully!")
        else:
            messagebox.showwarning("Return Failed", "The book was not borrowed or not found in the library!")

    def view_books(self):
        """View all available books."""
        available_books = self.library.view_available_books()
        self.output_text.delete(1.0, tk.END)  # Clear previous output
        if available_books:
            for book in available_books:
                self.output_text.insert(tk.END, f"ID: {book['book_id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Available: {book['available']}\n")
        else:
            self.output_text.insert(tk.END, "No available books.\n")

    def clear_database(self):
        """Clear the entire database."""
        result = messagebox.askyesno("Confirm", "Are you sure you want to clear the database?")
        if result:
            try:
                self.library.clear_db()  # Call the clear_db method from Library class
                messagebox.showinfo("Success", "Database cleared successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while clearing the database: {e}")

# Create the main Tkinter window and pass it to LibraryUI
if __name__ == "__main__":
    root = tk.Tk()
    ui = LibraryUI(root)
    root.mainloop()
