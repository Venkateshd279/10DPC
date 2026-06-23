# Nested if statement means putting one if statement inside another if statement. 
# Real-life example of nested if statement in Python using hotel concept 

room_type = "deluxe"
booking_status = "confirmed"

if booking_status == "confirmed":
    if room_type == "deluxe":
        print("You have booked a deluxe room.")
    elif room_type == "standard":
        print("You have booked a standard room.")
    else:
        print("Invalid room type.")
else:
    print("Your booking is not confirmed.")