

class Book:

    def __init__(self, title: str, author: str, genre: str, is_available: str):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = is_available
        self.borrowed_to = []

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        """Метод __repr__() — це “службовий” (спеціальний) метод, який визначає,
        як об’єкт буде відображатись у технічному (debug) форматі, тобто як Python
        показує його в консолі, списках, логах тощо."""
        return f"<Book title={self.title!r}, author={self.author!r}, genre={self.genre!r}>"

    def borrow_book(self):
        if not self.is_available:
            print("The book is not available")
        else:
            self.is_available = False


    def receive_book(self):
        self.is_available = True
