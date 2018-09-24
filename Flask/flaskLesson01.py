#!/usr/bin/env python3

from flask import Flask, jsonify, request, Response
import json
from settings import *
from bookModel import *

def request_validation(bookObject):
    if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False


@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if(request_validation(request_data)):
        Book.add_book(request_data["name"],request_data["isbn"],request_data["price"])
        response = Response("", 201, mimetype="application/json")
        response.headers['Location'] = "/books/" + str(request_data['isbn'])
        return response
    else:
        invalidBookObjectErrMsg = {
            "error": "Invalid book passed",
            "helpString": "Dta shouldbe..."
        }
        response = Response(json.dumps(invalidBookObjectErrMsg), status=400, mimetype="application/json")
        return response
    #print(typeof(request_data))
    #return jsonify(books)

#@app.route('/books')
#def shwo_all_books():
#    return jsonify(books)


@app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
    request_data = request.get_json()
    new_book = {
        "name": request_data['name'],
        "price": request_data['price'],
        "isbn": isbn
    }
    i = 0
    for book in books:
        print("HALIK")
        current_isbn = book["isbn"]
        if current_isbn == isbn:
            books[i] = new_book
        i += 1
        response = Response("", status=204)
    return response


@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
    index = 0
    book_to_remove={}
    for book in books:
        if book["isbn"] == isbn:
            book_to_remove=book
            break
        index += 1
    print("INDEX: " + str(index))
    try:
        books.remove(book_to_remove)
    except:
        pass
    return jsonify(books)


@app.route('/books/<int:isbn>', methods=['GET'])
def show_book_by_isbn(isbn):
    return_value = Book.get_book(isbn)
    return jsonify(return_value)

@app.route('/books', methods=['GET'])
def show_book_all():
    return jsonify({"books": Book.get_all_books()})



app.run(port=5000)
