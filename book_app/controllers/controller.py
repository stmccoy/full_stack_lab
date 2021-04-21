from app import app
from flask import render_template, request, redirect
from repositories import author_repository
from repositories import book_repository 
from models.book import Book
from flask import Blueprint
# from models.author import Author

books_blueprint = Blueprint("books", __name__)
@books_blueprint.route('/books')
def index():
    books = book_repository.select_all()
    return render_template('books.html', all_books=books)

@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(int(id))
    return redirect('/books')