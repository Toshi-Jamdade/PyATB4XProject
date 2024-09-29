from abc import ABC, abstractmethod
class PyATB(ABC):

    @abstractmethod
    def payFee(self):
        pass

    def enrolled(self):
        print("Enrolled")

class Student1(PyATB):
    def payFee(self):
        print("Paid")

Toshi = Student1()
Toshi.enrolled()        # Enrolled