# controllers/app.py
from flask import Flask, jsonify, request, render_template
from models import db, Book
import random

app = Flask(__name__)

def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['JSON_AS_ASCII'] = False
    app.config['JSONIFY_MIMETYPE'] = "application/json"
    return app

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.select()
    return render_template('index.html', books=books)

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book.create(name=data['name'], description=data['description'], year=data['year'])
    return jsonify({"message": "Book added successfully", "status_code": 200})

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    try:
        book = Book.get_by_id(book_id)
        return jsonify({'name': book.name, 'description': book.description, 'year': book.year})
    except Book.DoesNotExist:
        return jsonify({"message": "Book not found", "status_code": 404})

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    try:
        book = Book.get_by_id(book_id)
        book.name = data['name']
        book.description = data['description']
        book.year = data['year']
        book.save()
        return jsonify({"message": "Book updated successfully", "status_code": 200})
    except Book.DoesNotExist:
        return jsonify({"message": "Book not found", "status_code": 404})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    try:
        book = Book.get_by_id(book_id)
        book.delete_instance()
        return jsonify({"message": "Book deleted successfully", "status_code": 200})
    except Book.DoesNotExist:
        return jsonify({"message": "Book not found", "status_code": 404})
    

def generate_books():
    words = ["Adventure", "Mountain", "Eagle", "Ocean", "Sunset", "Forest", "Rainbow", "Dream", "Serenity", "Mystery",
             "Chocolate", "Sunflower", "River", "Moonlight", "Passion", "Freedom", "Hope", "Inspire", "Wisdom", "Victory",
             "Harmony", "Brilliant", "Celebrate", "Glorious", "Innovation"]

    for _ in range(10):
        name = ' '.join(random.choices(words, k=2))
        description = ' '.join(random.choices(words, k=5))
        year = random.randint(1900, 2023)
        Book.create(name=name, description=description, year=year)



if __name__ == '__main__':
    db.connect()
    Book.truncate_table()
    db.create_tables([Book])

    # Generate books
    with app.app_context():
        generate_books()

    app = create_app()
    app.run(debug=True)


