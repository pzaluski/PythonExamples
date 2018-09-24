from flask import Flask, jsonify
app = Flask(__name__)

data="dfaldfj;alksdf"
print(data.len

books = [
    {
        'name': 'Green Eggs',
        'price': 29.99
    },
    {
        'name': 'Cat in the hat',
        'price': 49.99
    }


]

#GET /books
@app.route('/books')
def get_books():
    return jsonify({'books': books})

app.run(port=5000)

