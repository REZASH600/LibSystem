# LibSystem

LibSystem is a simple Python-based library management system for managing books, members, and borrowing/returning books.

## Features
- Add new books to the library.
- Register library members.
- Issue books to members.
- Return borrowed books.
- Track the availability of books.

## Classes Overview

### 1. `Book`
Represents a book in the library.
- **Attributes:**
  - `title`: The title of the book.
  - `author`: The author of the book.
  - `isbn`: The unique ISBN of the book.
  - `available`: Boolean indicating if the book is available for borrowing.

- **Methods:**
  - `borrow()`: Marks the book as borrowed if available.
  - `return_book()`: Marks the book as returned if borrowed.
  - `__str__()`: Returns a string representation of the book’s status.

### 2. `Member`
Represents a library member.
- **Attributes:**
  - `name`: The name of the member.
  - `member_id`: A unique identifier for the member.
  - `borrowed_books`: A list of books the member has borrowed.

- **Methods:**
  - `borrow_book(book)`: Allows the member to borrow a book.
  - `return_book(book)`: Allows the member to return a borrowed book.
  - `__str__()`: Returns a string representation of the member.

### 3. `Library`
Represents the library itself.
- **Attributes:**
  - `books`: A list of books available in the library.
  - `members`: A list of registered library members.

- **Methods:**
  - `add_book(book)`: Adds a new book to the library.
  - `register_member(member)`: Registers a new member in the library.
  - `issue_book(member_id, isbn)`: Issues a book to a member by their ID and the book’s ISBN.
  - `return_book(member_id, isbn)`: Processes the return of a borrowed book.

## Example Usage

```python
# Creating books
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")

# Creating library and adding books
library = Library()
library.add_book(book1)
library.add_book(book2)

# Registering a member
member = Member("Alice", "M001")
library.register_member(member)

# Issuing a book to the member
library.issue_book("M001", "1234567890")

# Returning the book
library.return_book("M001", "1234567890")
