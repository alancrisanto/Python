import math

number_items = int(input("Enter the number if items: "))
items_perbox = int(input("Enter the number of items per box: "))

boxes = math.ceil(number_items / items_perbox)

print(f"For {number_items}, packing {items_perbox} items in each box, you will need {boxes} boxes.")