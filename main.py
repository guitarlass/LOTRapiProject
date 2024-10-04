# from flask import Flask, render_template
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap5
import os
from lotrapi import LotrAPI


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap5(app)

@app.route('/')
def index():
    lotrapi = LotrAPI()
    books_data = lotrapi.get_data("book")
    movies_data = lotrapi.get_data("movie")
    characters_data = lotrapi.get_random_character_data("character")
    return render_template('index.html', books=books_data, movies=movies_data, characters=characters_data)


@app.route('/get_book_quotes', methods=['GET'])
def get_book_quotes():
    character_name = request.args.get('character')
    lotrapi = LotrAPI()
    # Mockup logic to fetch quotes for the character (replace with actual logic)
    quotes = lotrapi.fetch_quotes_for_character(character_name)  # Implement this function
    # print(quotes)
    return jsonify({'quotes': quotes})


if __name__ == '__main__':
    app.run(debug=True)
