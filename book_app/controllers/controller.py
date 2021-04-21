from app import app
from flask import render_template, request
from repositories import author_repository
from repositories import book_repository 
from models.task import Book
# from models.author import Author

@app.route('/')
def index():
    return render_template('index.html')