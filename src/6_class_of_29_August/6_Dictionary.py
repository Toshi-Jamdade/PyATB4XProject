# Dictionary is an unordered collection of data
# Key & Value
# name -> "Toshi"

#Dictionary is very very important. Will be used in JSON format of API Automation.

student_info = {"name" : "Toshi",
                "age" : 24,
                "address" : "Pune"}

print(student_info)     #{'name': 'Toshi', 'age': 24, 'address': 'Pune'}
print(student_info["name"])     #Toshi

student_info = {"name" : "Toshi",
                "age" : 24,
                "age" : 23,     #Keys are always unique, the latest value will be considered.
                "address" : "Pune"}
print(student_info)     # {'name': 'Toshi', 'age': 23, 'address': 'Pune'}

student_info["age"] = 100
print(student_info)     # {'name': 'Toshi', 'age': 100, 'address': 'Pune'}

#Another way to write a dictionary
student_info = dict(name="Toshi", age=24, address="Hinjewadi")
print(student_info)     #{'name': 'Toshi', 'age': 24, 'address': 'Hinjewadi'}

student_info = {"name" : "Toshi",
                "age" : 24,
                "address" : {
                    "home_address" : "Matheran",
                    "office_address" : "Pune"
                }}
print(student_info)
# {'name': 'Toshi', 'age': 24, 'address': {'home_address': 'Matheran', 'office_address': 'Pune'}}
