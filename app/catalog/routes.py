from app.catalog import main
from app import db
from app.catalog.models import Book, Publication
from flask import render_template

@main.route('/')
def display_books():
    books = Book.query.all()
