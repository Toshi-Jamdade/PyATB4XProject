class Bank:

    def __init__(self, account_number, balance):
        self.balance = balance
        self.__account_number = account_number

    def deposit(self, amount):
        self.balance = self.balance + amount

    def check_balance(self):
        print(self.balance)

    def show_acc_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not allowed")

    def __internal_method(self):    #private method, cannot be access outside the class
        print("Private method")
        print(self.__account_number)
        self.show_acc_number()


icici = Bank(98753456889, 100)
icici.deposit(900)
icici.check_balance()
print(icici.show_acc_number(True))
#icici.__internal_method()   #AttributeError: 'Bank' object has no attribute '__internal_method'. Did you mean: '_Bank__internal_method'?