from flask import Flask, jsonify, request

app = Flask(__name__)


#This is for me to see if I did  it correct


# Sample data: list of books
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "published_date": "1925-04-10"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "published_date": "1960-07-11"},
]

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get a specific book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book["id"] == id), None)
    return jsonify(book) if book else ("Book not found", 404)

# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_book["id"] = len(books) + 1
    books.append(new_book)
    return jsonify(new_book), 201

# Update a book by ID
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    return ("Book not found", 404)

# Delete a book by ID
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book["id"] != id]
    return ("", 204)

if __name__ == '__main__':
    app.run(debug=True)
