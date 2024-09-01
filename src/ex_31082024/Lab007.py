#Strings #str
name = "Toshi"
print(type(name))       #<class 'str'>
print(name.upper())     #TOSHI
print(name.lower())     #toshi
print(len(name))        #5

a="90"
print(type(a))          #<class 'str'>
age=90
print(type(age))        #<class 'int'>

name="Line"
print(type(name))       #<class 'str'>
name=name+str(1)
print(name)             #Line1

first_name = "Toshi"
last_name = "Jamdade"
print(first_name + last_name)       #ToshiJamdade

how_many_planes_i_have = None
print(type(how_many_planes_i_have))         #<class 'NoneType'>

val=0
print(type(val))        #<class 'int'>

#id - Return the identity of an object - Address/memory location where it is stored
age=10
age2=10
age3=11
print(id(age))      #140730076564184
print(id(age2))     #140730076564184
print(id(age3))     #140730076564216





