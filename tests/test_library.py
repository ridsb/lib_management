import pytest
from library import Library  # Assuming Library is imported from your library.py

@pytest.fixture(scope="module")
def setup_library():
    """Set up the Library instance for the entire module."""
    library = Library()  # Create an instance of the Library
    yield library
    # No need to call close() if it's not defined in Library class


def test_add_book(setup_library):
    """Test adding a book to the library."""
    library = setup_library
    library.clear_db()
    library.add_book("1", "Test Book", "Test Author", 2023, 5, 5)
    # Fetch all available books and check if the added book exists
    all_books = library.view_available_books()
    added_book = None
    for book in all_books:
        if book['book_id'] == "1":
            added_book = book
            break
    
    assert added_book is not None  # Ensure the book was added
    assert added_book['book_id'] == "1"  # Check the book ID matches
  # Check the book ID matches


def test_borrow_book(setup_library):
    """Test borrowing a book."""
    library = setup_library
    library.clear_db()
    library.add_book("2", "Test Book 2", "Test Author", 2022, 3, 3)
    result = library.borrow_book("2")
    assert result is not None  # Book should be borrowed
    assert result['available'] == 2  # Assuming availability reduces by 1
    result = library.borrow_book("2")
    assert result['available']==1  # Book is no longer available
    result=library.borrow_book("2")
    assert result['available']==0

def test_return_book(setup_library):
    """Test returning a borrowed book."""
    library = setup_library
    library.clear_db()
    library.add_book("3", "Test Book 3", "Test Author", 2021, 5, 5)
    library.borrow_book("3")
    result = library.return_book("3")
    assert result is not None  # Book should be returned
    assert result['available'] == 5  # Ensure availability is restored
    result = library.return_book("3")
    assert result is None  # Book not found in borrowed list


def test_view_available_books(setup_library):
    """Test viewing available books in the library."""
    library = setup_library
    library.clear_db()
    library.add_book("4", "Test Book 4", "Test Author", 2020, 5, 5)
    available_books = library.view_available_books()
    assert len(available_books) > 0  # Ensure there are books in the library
    assert any(book['book_id'] == "4" for book in available_books)  # Check if added book is available
