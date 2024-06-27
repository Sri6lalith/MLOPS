from Searchhistory import database_connect as Page1DB
from Wishlist import database_connect as Page2DB, WishlistGenerator
from Bestsellers import database_connect as Page3DB
from Readinghistory import database_connect as Page4DB

def display_user_history(user_id):
    sql_library = Page1DB()
    user_history = sql_library.user_history(user_id)
    print("User History for user", user_id, ":")
    for book in user_history:
        print("  Title:", book.title)
        print("  Author:", book.author)
        print("  Genre:", book.genre)
        print("  Rating:", book.rating)
        print("  Date Read:", book.date_read)

def display_wishlist(user_id):
    sql_library = Page2DB()
    wishlist_generator = WishlistGenerator(sql_library)
    wishlist = wishlist_generator.generate_wishlist(user_id)
    print("\nWishlist for user", user_id, ":")
    for book in wishlist:
        print("- Title:", book.title)
        print("  Author:", book.author)
        print("  Genre:", book.genre)
        print("  Rating:", book.rating)
        print("  Date Read:", book.date_read)

def display_best_sellers():
    sql_library = Page3DB()
    best_sellers = sql_library.get_best_sellers()
    print("\nBest Sellers:")
    for book in best_sellers:
        print("- Title:", book.title)
        print("  Author:", book.author)

def display_started_books(user_id):
    sql_library = Page4DB()
    started_books = sql_library.get_started_books(user_id)
    print("\nBooks Started Reading for user", user_id, ":")
    for book in started_books:
        print("- Title:", book.title)
        print("  Author:", book.author)
        print("  Genre:", book.genre)

#Runnable method 
'''The if __name__ == "__main__": block is a common Python idiom that checks whether the script is being run as the main program or if it's being imported as a module into another script.'''
if __name__ == "__main__":
    user_id = "123"  # Example user_id
    while True:
        print("\nMenu:")
        print("1. List of products based on your history")
        print("2. Wish List")
        print("3. List of Best Sellers")
        print("4. List of Books I Have Started Reading")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_user_history(user_id)
        elif choice == '2':
            display_wishlist(user_id)
        elif choice == '3':
            display_best_sellers()
        elif choice == '4':
            display_started_books(user_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
