# nested if 

age = int(input("Enter your age:"))

subscribe = input("Do you have a subscription? (yes/no):")

if age >= 18:
    if subscribe == "yes":
        print ("You have full access")
elif age < 18:
    if subscribe.lower() == "yes":
        print ("you have limited access")
elif subscribe.lower() == "no":
    print ("you have no access, get scubscription")
else:

    print ("you have not allowed to access")