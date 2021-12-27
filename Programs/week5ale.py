grade_per = int(input("What is your grade percentage? "))
print()
# Challenge 1 Sign of grade
last_digit = grade_per % 10
if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""
# Challenge 2 Only A
if grade_per >= 93:
    sign = ""
# Challenge 3
elif grade_per <60:
    sign =""

if grade_per >= 90:
    print(f"Your grade is A{sign} \nCongratulations! Your approved") 
elif grade_per >= 80:
    print(f"Your grade is B{sign} \nCongratulations! Your approved")
elif grade_per >= 70:
    print(f"Your grade is C{sign} \nCongratulations! Your approved")
elif grade_per >= 60:
    print(f"Your grade is D{sign} \nYour approved")
else:
    print(f"Your grade percent is: F{sign} \nYou can improve")