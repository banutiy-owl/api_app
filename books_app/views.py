# view.py
from flask import render_template

def init_app(app):
    @app.route('/')
    def index(books):
        return render_template('index.html', books=books)
