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

class WishlistGenerator:
    def __init__(self, library: Kindle_store):
        self.library = library

    def generate_wishlist(self, user_id):
        reading_history = self.library.user_history(user_id)
        wishlist = self.analyze(reading_history)
        return wishlist

    def analyze(self, user_history):
        wishlist = []
        for book in user_history:
            if book.rating >= 4.0:
                wishlist.append(book)
        return wishlist

class database_connect(Kindle_store):
    def user_history(self, user_id):
        return [
            Book("Book1", "Author1", "Fantasy", 4.5, "2023-05-15"),
            Book("Book2", "Author2", "Mystery", 3.8, "2023-07-20"),
            Book("Book3", "Author3", "Science Fiction", 4.2, "2023-09-10")
        ]

# Usage
if __name__ == "__main__":
    sql_library = database_connect()
    wishlist_generator = WishlistGenerator(sql_library)
    user_id = "123"

    # Generate wishlist
    wishlist = wishlist_generator.generate_wishlist(user_id)
    print("\nWishlist for user", user_id, ":")
    for book in wishlist:
        print("- Title:", book.title)
        print("  Author:", book.author)
        print("  Genre:", book.genre)
        print("  Rating:", book.rating)
        print("  Date Read:", book.date_read)
