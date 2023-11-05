from flask import Flask, jsonify, request, render_template
from books import BookService
import requests

app = Flask(__name__, template_folder='templates')
book_service = BookService()

book_service.generate_books()

@app.route('/books', methods=['GET'])
def get_books():
    result = book_service.get_all_books()
    return render_template('index.html', data=result)


@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    response = book_service.add_book(data)
    if response["status_code"] == 200:
        return jsonify({"message": response["message"]}), 200
    else:
        return jsonify({"message": response["message"]}), response["status_code"]


@app.route('/books/<string:book_name>', methods=['GET', 'PUT'])
def handle_book(book_name):
    if request.method == 'GET':
        result = book_service.get_book(book_name)
        return jsonify(result)
    elif request.method == 'PUT':
        data = request.get_json()
        return book_service.update_book(book_name, data)

@app.route('/books/<string:book_name>', methods=['DELETE'])
def delete(book_name):
    response, status_code = book_service.delete_book(book_name)
    return jsonify({"message": response}), status_code

if __name__ == '__main__':
    app.run(debug=True)
