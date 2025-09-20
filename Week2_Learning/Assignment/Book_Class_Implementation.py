# Create a Python class named Book with the following:
#  Attributes: title, author, and publication_year.
#  A method get_age() that calculates and returns the age of the book in years (current year
# – publication_year).

from datetime import datetime
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.publication_year

# Example usage:
book = Book("1984", "George Orwell", 1949)
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"Age of the book: {book.get_age()} years")