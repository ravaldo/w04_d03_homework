
class Book():
	def __init__(self, title, author, genre, numpages, id=None):
		self.title = title
		self.author = author
		self.genre = genre
		self.numpages = numpages
		self.id = id
	
	def __repr__(self):
		return f"{self.title} ({self.id}) by {self.author}"
		