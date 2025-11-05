from libraryClass import Library
from bookClass import Book
from memberClass import Member

library = Library("New Library")
def add_space():
    print("\n\n")

while True:
    user_choice = input("1: Add a new book: \n"
                       "2: Get list of all books: \n"
                       "3: Get the list of all genres: \n"
                       "4: Get the list of books by genre: \n"
                       "5: Get the list of authors: \n"
                        "6: Get the list of books by author: \n"
                        "7: Get the book by name: \n"
                        "8: To borrow book: \n")

    if user_choice == '1':

        title = input("Enter the book title: ")
        author = input("Enter the Author: ")
        genre = input("Enter the Genre: ")
        library.add_book(title, author, genre, is_available=True)
        add_space()

    elif user_choice == '2':

        books = library.get_all_books()

        for book in books:
            print(book)
        add_space()

    elif user_choice == '3':

        genres = library.get_genres()

        for genre in genres:
            print(genre)
        add_space()

    elif user_choice == '4':

        genre = input("Enter the genre: ")
        books_list = library.get_books_by_genre(genre)

        if books_list is None:
            print("Sorry, you entered genre that is not present in our library: ")
        else:
            for book in books_list:
                print(book)
        add_space()

    elif user_choice == '5':

        authors = library.get_authors()

        for author in authors:
            print(author)
        add_space()

    elif user_choice == '6':

        author = input("The the author: ")
        books_list = library.get_books_by_author(author)

        if books_list is None:
            print(f"Sorry, we don't any books written by {author}")
        else:
            for book in books_list:
                print(book)
        add_space()

    elif user_choice == '7':

        book_title = input("Enter the book's title: ")
        book = library.get_book_by_name(book_title)

        if book is None:
            print(f"The book with title: '{book_title}' is not precent in our library")
        else:
            print(book)
        add_space()

    elif user_choice == '8':
        # Нужно проверить почему не добавляется, а перезаписывается
        book_title = input("Enter the book's title: ")
        first_name = input("Enter the First name: ")
        last_name = input("Enter the Last name: ")

        library.give_book(book_title, first_name, last_name)

        add_space()

    elif user_choice == "0":
        library.save_books_to_file()
        library.save_members_to_file()
        break
