#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 09:03:43 2021

@author: ricardo
"""

class Book:

     
    #Properties defined at the class level are shared by all instances
        
    # Python Object Oriented Programming by Joe Marini course example
    # Using class-level and static methods
    """
    instance methods receive a specific object instance as an argument
    and operate on data specific to that object instance"""

    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    # TODO: double-underscore properties are hidden from other classes
    __booklist = None
    #If you want to call it or subscribe it, use class._Book__booklist
    # TODO: create a class method

    @classmethod

    def getbooktypes(cls):
        return cls.BOOK_TYPES
    # TODO: create a static method

    @staticmethod
    
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance

    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype
    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    def setdiscount(self, amount):
        self._discount = amount
        
       
# TODO: access the class attribute
print("Book types: ", Book.getbooktypes())

# TODO: Create some book instances
b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "PAPERBACK")
#b3 = Book("Title 3", "COMIC")
print(b1)

# TODO: Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)