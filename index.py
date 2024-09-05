class Book:
    def __init__(self, title: str, author: str, isbn: str, available=True) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self) -> str:

        availability = "Available" if self.available else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {availability}"

    def borrow(self) -> bool:

        if self.available:
            self.available = False
            print(f"{self.title} has been borrowed successfully.")
            return True

        print(f"{self.title} is not available for borrowing.")
        return False

    def return_book(self) -> bool:

        if not self.available:
            self.available = True
            print(f"{self.title} has been returned successfully.")
            return True

        print(f"{self.title} was not borrowed and cannot be returned.")
        return False


class Member:
    def __init__(self, name: str, member_id: str, borrowed_books=[]) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books

    def __str__(self) -> str:
        return f"Name:{self.name}, Id:{self.member_id}"

    def borrow_book(self, book: Book) -> bool:

        if not book.borrow():
            return False

        self.borrowed_books.append(book)
        return True

    def return_book(self, book: Book) -> bool:

        if book not in self.borrowed_books:
            print("You have not borrowed this book.")
            return False

        elif not book.return_book():
            return False

        self.borrowed_books.remove(book)
        return True


class Library:

    def __init__(self) -> None:
        self.books = []
        self.members = []

    def add_book(self, book: Book) -> bool:
        self.books.append(book)
        print("Book added successfully.")
        return True

    def register_member(self, member: Member) -> bool:
        if member in self.members:
            print("Member is already registered.")
            return False
        self.members.append(member)
        print("Member registered successfully.")
        return True

    def find_member(self, member_id: str):
        return next(
            (member for member in self.members if member.member_id == member_id), None
        )

    def find_book(self, isbn: str):
        return next((book for book in self.books if book.isbn == isbn), None)

    def issue_book(self, member_id: str, isbn: str) -> bool:
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member:
            print("Member is not available.")
            return False

        if not book:
            print("Book is not available.")
            return False

        if not member.borrow_book(book):
            return False
        
        return True

    def return_book(self, member_id: str, isbn: str) -> bool:
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member:
            print("Member is not available.")
            return False

        if not book:
            print("Book is not available.")
            return False

        if not member.return_book(book):
            return False

        return True
