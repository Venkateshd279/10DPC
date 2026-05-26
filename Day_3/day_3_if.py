# if condition 

score = int(input("Enter your score:"))

if score >= 90 and score <= 100:
        print("Your grade is A+")
elif score >= 80 and score < 90:
        print("your grade is B+")
elif score >= 70 and score < 80:
        print("your grade is C+")
elif score <= 70 and score >= 0:
        print("FAIL")
else:
        print("Invalid score")