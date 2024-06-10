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
    def user_history(self, user_id):
        pass

class database_connect(Kindle_store):
    def user_history(self, user_id):
        # Placeholder implementation to retrieve reading history from SQL database
        return [
            Book("Book1", "Author1", "Fantasy", 4.5, "2023-05-15"),
            Book("Book2", "Author2", "Mystery", 3.8, "2023-07-20"),
            Book("Book3", "Author3", "Science Fiction", 4.2, "2023-09-10")
        ]

# Usage
if __name__ == "__main__":
    sql_library = database_connect()
    user_id = "123"

    # Get reading history
    user_history = sql_library.user_history(user_id)
    print("User History for user", user_id, ":")
    for book in user_history:
        print("- Title:", book.title)
        print("  Author:", book.author)
        print("  Genre:", book.genre)
        print("  Rating:", book.rating)
        print("  Date Read:", book.date_read)
