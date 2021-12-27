import math

w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

v = (math.pi * (w**2) * a * (w * a + 2540 * d)) / 10000000
galons = v / 3785
liters = v / 1000

print((f"The approximate volume is {v:.1f} milliliters. "))
print((f"The approximate volume is {galons:.1f} in galons and {liters:.1f} in liters. "))

# --------------------------------------------------------------

answer = str(input("Would you like to buy the tires with the specify dimensions? "))

if answer.lower() == "yes":
    number = input("Please enter your phone number: ")
    print("Your order has been confirmed, thank you!")
else:
    print("Have a nice day!")
    number = None

# --------------------------------------------------------------
from datetime import datetime

now = datetime.now()

current_date = now.strftime("%Y-%m-%d")


with open("volume.txt", "at") as data_volume:
    print(f"{current_date}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.1f}, {number}", file=data_volume)



    
    
    
