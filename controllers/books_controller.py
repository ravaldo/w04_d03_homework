from flask import Flask, Blueprint, render_template, request, redirect
from repositories import author_repository
from repositories import book_repository
from models.book import Book
from models.author import Author


books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
	books = book_repository.select_all()
	return render_template("books/index.html", all_books = books)


@books_blueprint.route("/books/<id>/delete")
def delete_task(id):
	book_repository.delete(id)
	return redirect("/books")

@books_blueprint.route("/books/new")
def new_book():
	authors = author_repository.select_all()
	return render_template("books/new.html", authors = authors)


@books_blueprint.route("/add_author", methods=["POST"])	
def new_author():
	first_name = request.form["first_name"]
	last_name = request.form["last_name"]
	author = Author(first_name, last_name)
	author_repository.save(author)
	return redirect("/books/new")
	
	
@books_blueprint.route("/books", methods=["POST"])	
def add_author():
	title = request.form["title"]
	genre = request.form["genre"]
	pages = request.form["numpages"]
	author = author_repository.select(request.form["author_id"])
	book = Book(title, author, genre, pages)
	book_repository.save(book)
	return redirect("/books")