# OOPS Concepts:
# Class - Blueprint
# Object - Instance of a class
# Encapsulation - private __, protected _, public
# Inheritance - single, multiple, mutlilevel, hierarchical, hybrid
# Polymorphism - method overriding, method overloading(x)
# self, super, __init__
# Abstraction
# Static methods

# Abstraction - Hide the details and show what is required
# focuses on hiding the complex implementation details while exposing only the essential features of an object.

# To create an abstract class in Python, you need to:
#1. Import the ABC class and the abstractmethod decorator from the abc module
#2. Define a class that inherits from ABC.
#3. Use the @abstractmethod decorator to define abstract methods.

from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
         print("Bark")      #if we don't complete this method then will get error

dog = Dog("PP")
dog.sound()     # Bark

