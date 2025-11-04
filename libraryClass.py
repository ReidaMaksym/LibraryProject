from bookClass import Book
from memberClass import Member
import json
from datetime import date

class Library:

    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.members = []
        self.load_books()
        self.load_members()

    # Book methods ___________________________________________

    def load_books(self) -> list[dict] | list:

        books = []

        try:
            with open('data.json', 'r') as file:
                books = json.load(file)

            for book in books:
                title = book.get('title')
                author = book.get('author')
                genre = book.get('genre')
                is_available = book.get('is_available')

                self.books.append(Book(title, author, genre, is_available))
        except FileNotFoundError:
            print("data.json not found. Starting with an empty library.")
        except json.JSONDecodeError:
            print("Error reading JSON data.")

        return books


    def add_book(self, title: str, author: str, genre: str, is_available: bool):
        new_book = Book(title, author, genre, is_available)

        self.books.append(new_book)

        books_database = self.load_books()

        books_database.append({
            "title": new_book.title,
            "author": new_book.author,
            "genre": new_book.genre,
            "is_available": new_book.is_available
        })

        with open("data.json", "w") as file:
            json.dump(books_database, file, indent=4)


    def get_all_books(self) -> list[Book]:
        return self.books


    def show_all_books(self) -> None:
        for book in self.books:
            print(book)


    def get_genres(self) -> list[str]:
        all_genres = []

        for genre in self.books:
            all_genres.append(genre.genre)

        unique_genres = list(set(all_genres))

        return unique_genres


    def get_books_by_genre(self, genre: str) -> list[Book] | None:

        available_genres = self.get_genres()
        books = []

        if genre in available_genres:
            for book in self.books:
                if book.genre == genre:
                    books.append(book)
            return books
        else:
            return None


    def get_authors(self) -> list[str]:

        all_authors = []

        for author in self.books:
            all_authors.append(author.author)

        unique_author = list(set(all_authors))

        return unique_author


    def get_books_by_author(self, author: str) -> list[Book] | None:

        authors = self.get_authors()

        books = []

        if author in authors:
            for book in self.books:
                if book.author == author:
                    books.append(book)
            return books
        else:
            return None


    def get_book_by_name(self, book_title: str) -> Book | None:

        for book in self.books:
            if book_title == book.title:
                return book

        return None


    def give_book(self, book_title: str, first_name: str, last_name: str):

        book = self.get_book_by_name(book_title)
        member = self.get_member_by_first_and_last_name(first_name, last_name)
        member_database = self.load_members()
        books_database = self.load_books()

        if book and book.is_available:
            if member:
                book.borrow_book()
                for user in member_database:
                    print(user)
                    if user.get('first_name') == member.get('first_name') and user.get('last_name') == member.get('last_name'):
                        print("The user is found")
                        current_date = date.today()
                        user.get('books').append({
                            "title": book.title,
                            "date": current_date.isoformat()
                        })
                        break
                for book_item in books_database:
                    if book_item.get('title') == book.title and book_item.get('author') == book.author:
                        book_item['is_available'] = False
                        break
            else:
                print(f"The member {first_name} {last_name} is not found")
        else:
            print(f"The book with title {book_title} is not found in the library")

        print(member_database)

        with open("members.json", "w") as file:
            json.dump(member_database, file, indent=4)

        with open("data.json", "w") as file:
            json.dump(books_database, file, indent=4)


    def receive_book_back(self, book_title: str, first_name: str, last_name: str):
        book = self.get_book_by_name(book_title)
        member = self.get_member_by_first_and_last_name(first_name, last_name)
        members_database = self.load_members()
        books_database = self.load_books()

        if book and book.is_available == False:
            if member:
                book.receive_book()
                for member_item in members_database:
                    if member_item.get('first_name') == first_name and member_item.get("last_name") == last_name:
                        print(member_item.get('books'))
                        member_item['books'] = [book for book in member_item['books'] if book['title'] != book_title]
                        print(member_item.get('books'))
                        break

                for book_item in books_database:
                    if book_item.get('title') == book.title and book_item.get('author') == book.author:
                        book_item['is_available'] = True
                        break
        else:
            print(f"The book '{book_title}' is not found in the library")

        with open("members.json", "w") as file:
            json.dump(members_database, file, indent=4)

        with open("data.json", "w") as file:
            json.dump(books_database, file, indent=4)


    #Member methods ________________________________________
    def load_members(self) -> list[dict] | list:

        users = []

        try:
            with open('members.json', 'r') as file:
                users = json.load(file)
                if len(users) != 0:
                    for user in users:
                        first_name = user.get('first_name')
                        last_name = user.get('last_name')

                        self.members.append(Member(first_name, last_name))
        except FileNotFoundError:
            print("members.json not found. Starting with an empty library.")
        except json.JSONDecodeError:
            print("Error reading JSON data in members.json.")

        return users


    def add_member(self, first_name: str, last_name: str):
        new_member = Member(first_name, last_name)

        self.members.append(new_member)

        members_database = self.load_members()

        members_database.append({
            "first_name": first_name,
            "last_name": last_name,
            "books": []
        })

        with open("members.json", "w") as file:
            json.dump(members_database, file, indent=4)


    def get_member_by_first_and_last_name(self, first_name: str, last_name: str) -> dict | None:
        members_database = self.load_members()

        for member in members_database:
            if member.get('first_name') == first_name and member.get('last_name') == last_name:
                print(member)
                return member

        return None


library = Library("Test")
# print(library.get_book_by_name("The Rational Mind"))
#
# print(library.members)
# print(library.load_members())
# library.add_book("Test title", "Test author", "Test genre", True)
# library.add_member("Test", "2")


# print(library.get_member_by_first_and_last_name("Maksym", "Reida"))
# library.give_book("The Rational Mind", "Maksym", "Reida")
# library.get_member_by_first_and_last_name("Maksym", "Reida")

library.receive_book_back("The Rational Mind", "Maksym", "Reida")