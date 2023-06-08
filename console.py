import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("J. R. R.", "Tolkien")
author2 = Author("J. K.", "Rowling")
author3 = Author("Geroge", "Orwell")
author_repository.save(author1)
author_repository.save(author2)
author_repository.save(author3)
author1.first_name = "J.R.R."
author_repository.update(author1)
author_repository.delete(author3.id)
print(author_repository.select(author2.id))
authors = author_repository.select_all()
assert(len(authors) == 2)


book_1 = Book("The Hobbit", author1, "Fiction", 30)
book_2 = Book("The Lord of the Rings: The Fellowship of the Ring", author1, "Fiction", 654)
book_3 = Book("The Lord of the Rings: The Two Towers", author1, "Fiction", 654)
book_4 = Book("The Lord of the Rings: The Return of the King", author1, "Fiction", 987)
book_5 = Book("Harry Potter 1", author2, "Fiction", 654)
book_6 = Book("Harry Potter 2", author2, "Fiction", 321)
book_7 = Book("Harry Potter 3", author2, "Fiction", 987)

book_repository.save(book_1)
book_repository.save(book_2)
book_repository.save(book_3)
book_repository.save(book_4)
book_repository.save(book_5)
book_repository.save(book_6)
book_repository.save(book_7)


book_5.title = "Harry Potter and the Philosopher's Stone"
book_repository.update(book_5)
book_repository.delete(book_7.id)
books = book_repository.select_all()
assert(len(books) == 6)

for a in authors:
	print(a)

for b in books:
	print(b)