from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Child(Father):
    pass
    # def loan(self):
    #     print("Paid the loan")

child = Child("1L")
child.loan()

# TypeError: Can't instantiate abstract class Child without an implementation for abstract method 'loan'