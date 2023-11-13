# models/book.py
from peewee import SqliteDatabase, Model, CharField, IntegerField
import random


db = SqliteDatabase('books.db')

class BaseModel(Model):
    class Meta:
        database = db

class Book(BaseModel):
    name = CharField()
    description = CharField()
    year = IntegerField()


