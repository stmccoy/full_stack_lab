import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_repository.delete_all()
book_repository.delete_all()

author_1 = Author("JRR Tolkien")
author_repository.save(author_1)
author_2 = Author("JK Rowling")
author_repository.save(author_2)

book_1 = Book("Lord of the Rings", author_1)
book_repository.save(book_1)
book_2 = Book("Harry Potter", author_2)
book_repository.save(book_2)

pdb.set_trace()