class Myclass:

    #public var (instance)
    public_var = "I am public"

    #private variable - starts with __ (double underscore) -> cannot be accessed outside the class
    __private_var = "I'm private"

    #protected variable - starts with _ (underscore) -> accessible only in the same package
    _protected_var = "I'm protected"

object = Myclass()
print(object.public_var)        # I am public
#print(object.__privare_var)     #AttributeError: 'Myclass' object has no attribute '__privare_var'
print(object._protected_var)    # I'm protected

