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
    def get_best_sellers(self):
        pass

class database_connect(Kindle_store):
    def get_best_sellers(self):
        # Placeholder implementation to retrieve best sellers from SQL database
        return [
            Book("Book6", "Author6", "Thriller", 4.8, "2023-10-05"),
            Book("Book7", "Author7", "Historical Fiction", 4.7, "2023-11-15")
        ]

# Usage
if __name__ == "__main__":
    sql_library = database_connect()

    # Get best sellers
    best_sellers = sql_library.get_best_sellers()
    print("\nBest Sellers:")
    for book in best_sellers:
        print("- Title:", book.title)
        print("  Author:", book.author)
