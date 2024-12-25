# Library Management System

A simple Library Management System built using Python's Tkinter for GUI and basic class-based functionality. The system allows users to add, borrow, return, and view books in the library.

## Features

- **Add a Book:** Allows users to add books with details like book ID, title, author, publication year, and available copies.
- **Borrow a Book:** Lets users borrow books by entering the book ID. The system checks if the book is available.
- **Return a Book:** Users can return borrowed books by entering the book ID.
- **View Available Books:** Displays a list of books that are available for borrowing.

## Requirements

- Python 3.x
- Tkinter library (usually included with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ridsb/library-management-system.git
   ```
2. Navigate to the project folder:
   ```bash
   cd library-management-system
   ```
3. Run the application:
   ```bash
   python library_ui.py
   ```

## Functionality Overview

### 1. **Add Book:**

- This function allows users to add a new book to the library by entering details like `book_id`, `title`, `author`, `year`, and `available copies`.
- The system validates that all fields are filled, then adds the book to the library.
- **Function in UI:** `add_book()`

### 2. **Borrow Book:**

- This function lets a user borrow a book by entering its `book_id`.
- The system checks if the book is available for borrowing. If so, it updates the available copies and confirms the borrowing process.
- If the book is not available, the user receives a warning.
- **Function in UI:** `borrow_book()`

### 3. **Return Book:**

- This function allows a user to return a borrowed book by entering its `book_id`.
- The system verifies whether the book was borrowed and updates the availability count.
- If the book is not found or not borrowed, the system shows an error message.
- **Function in UI:** `return_book()`

### 4. **View Available Books:**

- Displays all available books in the library.
- The system shows details like `book_id`, `title`, `author`, `year`, and the number of available copies.
- **Function in UI:** `view_books()`

---

## Class Descriptions

### `Library` Class

The core logic of the library is handled in the `Library` class. This class manages the list of books, and provides methods to:

- `add_book(book_id, title, author, year, available, max_books)`: Adds a new book to the library.
- `borrow_book(book_id)`: Checks if a book is available and reduces its available copies when borrowed.
- `return_book(book_id)`: Increases the available copies when a book is returned.
- `view_available_books()`: Returns a list of all available books in the library.

### `LibraryUI` Class

This class handles the graphical user interface (GUI) using Tkinter. It provides the following:

- **UI Elements**: Labels, entry fields, and buttons to interact with the system (add, borrow, return, and view books).
- **Functions**: Handles user interactions (button clicks) and calls appropriate methods in the `Library` class.

---

## Example Usage

1. **Adding a Book:**
   - Enter the book details in the "Add Book" section and click the "Add Book" button to add the book to the library system.
2. **Borrowing a Book:**
   - Enter the book ID in the "Borrow Book" section and click the "Borrow" button to borrow the book.
3. **Returning a Book:**

   - Enter the book ID in the "Return Book" section and click the "Return" button to return the borrowed book.

4. **Viewing Available Books:**
   - Click the "View Available Books" button to see all the books currently available for borrowing.
