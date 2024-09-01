# Grade Calculator
# Write a program that calculates and displays the letter grade for a given numerical score

#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59

# user input Numerical score - integer
# o/p - Str - grade

numerical_score = int(input("Enter your numerical score"))
if 90 <= numerical_score <= 100:
    print("Your Grade is A")
elif 80 <= numerical_score <= 89:
    print("Your Grade is B")
elif 70 <= numerical_score <= 79:
    print("Your Grade is C")
elif 60 <= numerical_score <= 69:
    print("Your Grade is D")
elif numerical_score > 100:
    print("Please enter a valid numerical score")
else:
    print("Your Grade is F")

