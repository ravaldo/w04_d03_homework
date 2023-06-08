from flask import Flask, Blueprint, render_template
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
	
