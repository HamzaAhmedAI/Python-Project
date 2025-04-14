import json

class BookCollection:
    """A Class to manage a collection of books, Allows to store and organize their reading materials."""

    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage."""
        self.books = []
        self.storage_file = 'books_data.json'
        self.read_from_file()
    
    def read_from_file(self):
        """Load saved books from a JSON file into memory.
        If the file doesn't exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, 'r') as file:
                self.books_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books_list = []

    def save_to_file(self):
        """Store the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, 'w') as file:
            json.dump(self.books_list, file, indent=4)

    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user."""
        book_title = input("Enter the book title: ")
        book_author = input("Enter the author's name: ")
        publication_year = input("Enter the publication year: ")
        book_genre = input("Enter the genre: ")
        is_book_read = input("Have you read this book? (yes/no): ").strip().lower() == 'yes'
        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        self.books_list.append(new_book)
        self.save_to_file()
        print("Book added successfully!\n")

    def delete_book(self):
        """Remove a book from the collection by its title."""
        book_title = input("Enter the title of the book you want to delete: ")

        for book in self.books_list:
            if book["title"].lower() == book_title.lower():
                self.books_list.remove(book)
                self.save_to_file()
                print(f"Book '{book_title}' deleted successfully!\n")
                return
        print(f"Book '{book_title}' not found in the collection.\n")

    def find_book(self):
        """Search for a book in the collection by title or author name."""
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
        search_text = input("Enter search text: ").lower()
        found_books = [
            book
            for book in self.books_list
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]
    
        if found_books:
            print("Matching books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Not Read"
                print(
                    f"{index}. Title: {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
                )
        else:
            print("No matching books found.\n")

    def update_book(self):
        """Update the details of an existing book in the collection."""
        book_title = input("Enter the title of the book you want to update: ")
        for book in self.books_list:
            if book['title'].lower() == book_title.lower():
                print("Leave blank to keep the existing value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = input(f"New author ({book['author']}): ") or book["author"]
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                book["read"] = input(f"Have you read this book? (yes/no): ").strip().lower() == 'yes'
                self.save_to_file()
                print(f"Book '{book_title}' updated successfully!\n")
                return
        print(f"Book '{book_title}' not found in the collection.\n")

    def show_all_books(self):
        """Display all books in the collection with their details."""
        if not self.books_list:
            print("Your collection is empty.\n")
            return
        
        print("Your book collection:")
        for index, book in enumerate(self.books_list, 1):
            reading_status = "Read" if book["read"] else "Not Read"
            print(
                f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
            )
        print("\n")

    def show_reading_progress(self):
        """Calculate and display statistics about your progress reading."""
        total_books = len(self.books_list)
        completed_books = sum(1 for book in self.books_list if book["read"])
        completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0
        print(f"Total books in the collection: {total_books}")
        print(f"Reading progress: {completion_rate:.2f}%\n")


def start_application():
    """Run the main application loop with a user-friendly menu."""
    book_collection = BookCollection()
    while True:
        print("📚 Welcome to your Book Collection Manager!")
        print("1. Add a new book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Update book details")
        print("5. View all books")
        print("6. View reading progress")
        print("7. Exit")
        user_choice = input("Enter your choice (1-7): ")

        if user_choice == "1":
            book_collection.create_new_book()
        elif user_choice == "2":
            book_collection.delete_book()
        elif user_choice == "3":
            book_collection.find_book()
        elif user_choice == "4":
            book_collection.update_book()
        elif user_choice == "5":
            book_collection.show_all_books()
        elif user_choice == "6":
            book_collection.show_reading_progress()
        elif user_choice == "7":
            print("Thank you for using the Book Collection Manager!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    start_application()