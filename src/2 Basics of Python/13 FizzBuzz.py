#Fizz Buzz Program

# if number is multiple of 3 then print Fizz
# if number is multiple of 5 then print Buzz
# if number is multiple of both 3 & 5 then print Fizz Buzz

# Logic: First check if the number is multiple of 15 then other two numbers

for i in range(1, 101):
    if i%15==0:
        print("Fizz Buzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)
