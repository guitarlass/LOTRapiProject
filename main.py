# from flask import Flask, render_template
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import os
from lotrapi import LotrAPI

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkeyoltr"
Bootstrap5(app)

@app.route('/')
def index():
    lotrapi = LotrAPI()
    books_data = lotrapi.get_data("book")
    movies_data = lotrapi.get_data("movie")
    characters_data = lotrapi.get_data1("character")
    return render_template('index.html', books=books_data, movies=movies_data, characters=characters_data)

if __name__ == '__main__':
    app.run(debug=True)
