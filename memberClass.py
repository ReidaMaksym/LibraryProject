
class Member:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.borrowed_books = []

    def __str__(self):
        return f"First name: {self.first_name}, Last name: {self.last_name}"

    def __repr__(self):
        return f"<Member first_name={self.first_name!r}, last_name={self.last_name!r}, borrowed_books={self.borrowed_books!r}>"