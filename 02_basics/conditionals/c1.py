
import datetime

age = int(input("Enter the age : "))

day = datetime.datetime.now().strftime("%A")
catogery = "Adult"
ticket = 0;
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")

if age < 18:
    catogery = "Children"
    ticket = 8.00
else:
    catogery = "Adults"
    ticket = 12.00

if day == "Wednesday":
       ticket = ticket - 2

print("Your Catoegory :", catogery )
print("Your Ticket Price :", ticket )
