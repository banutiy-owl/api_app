# models/__init__.py
from .book import db, Book

def init_app(app):
    db.connect()
    db.create_tables([Book], safe=True)
