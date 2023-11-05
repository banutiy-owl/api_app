from book import Book
import random

class BookService:
    def __init__(self):
        self.books = [Book("MyBook", "MyAuthor", "description", 1999)]
        self.authors = []

    def generate_books(self):
        words = ["Adventure", "Mountain", "Eagle", "Ocean", "Sunset", "Forest", "Rainbow", "Dream", "Serenity", "Mystery",
         "Chocolate", "Sunflower", "River", "Moonlight", "Passion", "Freedom", "Hope", "Inspire", "Wisdom", "Victory",
         "Harmony", "Brilliant", "Celebrate", "Glorious", "Innovation"]
        for i in range(10):
            name = ' '.join(random.choices(words, k=2))
            description = ' '.join(random.choices(words, k=5)) 
            year = random.randint(1900, 2023)
            author_name = ' '.join(random.choices(words, k=2))
            book = Book(name, author_name, description, year)
            self.authors.append(author_name)
            self.books.append(book)
            

    def get_all_books(self):
        return self.books

    def add_book(self, data):
        self.books.append(data)
        return {"message": "Book added successfully", "status_code" : 200}

    def get_book(self, book_name):
        for book in self.books:
            if book.get('name') == book_name:
                return book
        return {"message": "Book not found"}

    def update_book(self, book_name, data):
        for book in self.books:
            if book.get('name') == book_name:
                book.update(data)
                return {"message": "Book updated successfully"}
        return {"message": "Book not found"}

    def delete_book(self, book_name):
            for book in self.books:
                if book.name == book_name:
                    self.books.remove(book)
                    return {"message": "Book deleted successfully", "status_code" : 200}
            return {"message": "Book not found", "status_code" : 404}


    def delete_author(self, author_name):
            if author_name in self.authors:
                self.authors.remove(author_name)
                return {"message": "Author deleted successfully", "status_code" : 200}
            return {"message": "Author not found", "status_code" : 404}