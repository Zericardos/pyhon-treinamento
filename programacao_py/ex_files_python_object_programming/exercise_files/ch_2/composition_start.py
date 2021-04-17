# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects
# Because sometimes we want to extract only some objects, not all of them
"""
class Book:
    def __init__(self, title, price, authorfname, authorlname):
        self.title = title
        self.price = price
        
        self.authorfname = authorfname
        self.authorlname = authorlname

        self.chapters = []

    def addchapter(self, name, pages):
        self.chapters.append((name, pages))
"""
class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price
        
        self.author = author
        
        self.chapters = []
    #use addchapter standard method to add chapters and extra pagecount
    def addchapter(self, chapter):
        self.chapters.append(chapter)
    
    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result

class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def __str__(self):
        return f"{self.fname} {self.lname}"

class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount
        
auth = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, auth)

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.title)
print(b1.auth)
print(b1.getbookpagecount())