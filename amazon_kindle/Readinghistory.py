from abc import ABC, abstractmethod

class Book:
    def __init__(self, title, author, genre, rating, date_read):
        self.title = title
        self.author = author
        self.genre = genre
        self.rating = rating
        self.date_read = date_read

class Kindle_store(ABC):
    @abstractmethod
    def get_started_books(self, user_id):
        pass

class database_connect(Kindle_store):
    def get_started_books(self, user_id):
        # Placeholder implementation to retrieve books that a user has started reading
        return [
            Book("Book10", "Author10", "Fantasy", None, None),
            Book("Book11", "Author11", "Thriller", None, None)
        ]

# Usage
if __name__ == "__main__":
    sql_library = database_connect()
    user_id = "123"

    # Get started books
    started_books = sql_library.get_started_books(user_id)
    print("\nBooks Started Reading for user", user_id, ":")
    for book in started_books:
        print("- Title:", book.title)
        print("  Author:", book.author)
        print("  Genre:", book.genre)
