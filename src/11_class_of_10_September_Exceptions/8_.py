# Custom exception
# user defined exception

class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

balance = 100
withdraw = int(input("Enter the amt u want to withdraw\n"))

if withdraw > balance:
    raise MyCustomException ("Balance is low")
else:
    print("Remaining balance", (balance-withdraw))

