# library_management.py

class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize a book with title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Check out the book (mark as unavailable)."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False  # Already checked out
    
    def return_book(self):
        """Return the book (mark as available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False  # Already available
    
    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize an empty library."""
        self._books = []  # Private list to store Book instances
    
    def add_book(self, book):
        """Add a book to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book instances can be added to the library")
    
    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"Successfully checked out '{title}'")
                    return True
        print(f"Book '{title}' is not available for checkout")
        return False
    
    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"Successfully returned '{title}'")
                    return True
        print(f"Book '{title}' was not checked out or doesn't exist")
        return False
    
    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are currently available")
    
    def get_total_books(self):
        """Get the total number of books in the library."""
        return len(self._books)
    
    def get_available_count(self):
        """Get the number of available books."""
        return len([book for book in self._books if book.is_available()])
    
    def get_checked_out_count(self):
        """Get the number of checked out books."""
        return len([book for book in self._books if not book.is_available()])
    
    def find_book(self, title):
        """Find a book by title and return it, or None if not found."""
        for book in self._books:
            if book.title == title:
                return book
        return None
