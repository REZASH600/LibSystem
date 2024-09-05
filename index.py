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

