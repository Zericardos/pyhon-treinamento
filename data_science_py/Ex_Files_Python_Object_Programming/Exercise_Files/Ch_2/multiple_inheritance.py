#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:01:39 2021

@author: ricardo
"""
class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"

class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"

class C(B, A):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)
c = C()
c.showprops()

"""note two classes A, B have the same attribute name, but with
different values. So class C inherits the first value from the first class from
left to right. The method resolution order (__mro__) clarifies the order which the classes
are loades"""

print(C.__mro__)

