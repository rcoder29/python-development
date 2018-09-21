'''
Sample caclulator calss to be used for Unit testing example
'''

"""
Create a simple calculator class - the calculator shoud allow addition, division, multiplication and subtract. 
It should also allow memory to be used to add, or subtract value. It should also be possible to clear the memory.
"""

# define class calculator
class calculator(object):

    def __init__(self):
        self.total=0
        # Initialize calculator object
        pass

    def add(self, x, y):
        z=x+y
        self.total+=z
        return z

    def subtract(self, x, y):
        z=x-y
        self.total+=z
        return z

    def multiply(self, x, y):
        z=x*y
        self.total+=z
        return z

    def divide(self, x, y):
        z=x/y
        self.total+=z
        return z

    def clear(self):
        self.total=0

    def total(self):
        return self.total
