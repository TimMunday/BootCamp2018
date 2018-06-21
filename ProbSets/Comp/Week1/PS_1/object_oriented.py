# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:45:20 2018

@author: Tim
"""

# Lab 3 (object orientated)

from math import sqrt

# Problem 1

class Backpack:
    """ Backpack object class. Has a name and a list of contents.
    Attributes:
        name (str): the name of the backpack's ownder.
        contents (list): the contents of the backpack.
        max_size (int): the maximum number of items
        color (str): the color of the backpack
    """
    def __init__(self, name, color, max_size=5):
        """Set the name and initialize an empty list of contents.
        
        Parameters:
            name (str): the name of the backpack's owner.
            color (str): the color of the backpack's owner
            max_size (int): keyword argument that defaults to 5
        """
        self.name = name
        self.color = color
        self.max_size = max_size
        self.contents = []
    
    def put(self, item):
        """Add 'item' to the backpack's list of contents"""
        if len(self.contents) < self.max_size:
            self.contents.append(item)
        else:
            print('No room!')
        
    def take(self, item):
        """Remove 'item' from the backpack's list of contents"""
        self.contents.remove(item)

    def dump(self):
        """Reset the contents of the backpack to an empty list"""
        self.contents = []
    
    def __add__(self, other):
        """Add the number of contents of each Backpack."""
        return len(self.contents) + len(other.contents)
    
    def __eq__(self, other):
        """Check if two backpack have the same name color
        and number of contents"""
        if (self.color == other.color
            and self.name == other.name
            and len(self.contents) == len(other.contents)):
                return True
        else:
            return False
    
    def __str__(self):
        """Return some output when printing a backpack"""
        output_print = '\tOwner:  ' + str(self.name) + '\n'\
        +'\tColor:  ' +  str(self.color) + '\n'\
        +'\tSize:  ' + str(len(self.contents)) + '\n'\
        +'\tMax Size  ' + str(self.max_size) + '\n'\
        +'\tContents  ' + str(self.contents)
        return output_print

            

#Problem 2

# Inherit from the Backpack class in the class definition.
class Knapsack(Backpack):
    """A Knapsack object class. Inherits from the Backpack class.
    A knapsack is smaller than a backpack and can be tied closed.
    Attributes:
        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit inside.
        contents (list): the contents of the backpack.
        closed (bool): whether or not the knapsack is tied shut.
    """
    def __init__(self, name, color, max_size=3):
        """Use the Backpack constructor to initialize the name, color,
        and max_size attributes. A knapsack only holds 3 item by default.     
        
        Parameters:
            name (str): the name of the knapsack's owner.
            color (str): the color of the knapsack.
            max_size (int): the maximum number of items that can fit inside.
        """
        Backpack.__init__(self, name, color, max_size)
        self.closed = True
        
    def put(self, item): # Override the put() method.
        """If the knapsack is untied, use the Backpack.put() method."""
        if self.closed:
            print("I'm closed!")
        else: # Use Backpack's original put().
            Backpack.put(self, item)

    def take(self, item): # Override the take() method.
        """If the knapsack is untied, use the Backpack.take() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.take(self, item)
            
    def weight(self): # Define a new method just for knapsacks.
        """Calculate the weight of the knapsack by counting the length of the
        string representations of each item in the contents list.
        """
        return sum([len(str(item)) for item in self.contents])
    
class Jetpack(Backpack):
    """A Jetpack object class"""
    def __init__(self, name, color, max_size=2, fuel=10):
        Backpack.__init__(self, name, color, max_size)
        self.fuel=fuel
        
    def fly(self, burn):
        if burn > self.fuel:
            print('Not enough fuel')
        else:
            self.fuel = self.fuel - burn

    def dump(self):
        self.contents=[]
        self.fuel=0

#Problem 4

class ComplexNumber:
    """Complex number class"""
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def conjugate(self):
        return ComplexNumber(self.real, -1*self.imag)
    
    def __str__(self):
        if self.imag>=0:
            output_com =  '(' + str(self.real) + '+' + str(self.imag) + 'j)'
        else:
            output_com =  '(' + str(self.real) + '+' + str(-self.imag) + 'j)'
        return output_com
    
    def __abs__(self):
        absoluteval = sqrt(self.real**2 + self.imag**2)
        return absoluteval

    def __eq__(self, other):
        if (self.real == other.real
            and self.imag == other.imag):
                return True
        else:
            return False
        
    def __add__(self, other):
        return ComplexNumber(self.real+other.real, self.imag+other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        return ComplexNumber((self.real)*(other.real) - (self.imag)*(other.imag), (self.imag)*(other.real) + (self.real)*(other.imag))
    
    def __truediv__(self, other):
        return ComplexNumber((self.real*other.real + self.imag*other.imag)/(other.real**2 + other.imag**2), (self.imag*other.real - self.real*other.imag)/(other.real**2 + other.imag**2))
                             
                             
           
                             
                             
                             
                             
                             
                             
                             
    
    
    