child_price = float(input('What is the price of a child meal? '))
adults_price = float(input('What is the price of an adult meal? '))
number_children = int(input('How many children are there? '))
number_adults = int(input('How many adults are there? '))
tax = float(input('What is the sales tax rate? '))
tip = float(input(f'Tip percent %: '))
print()

# meal subtotal = #children * price + #adults * price
# sales tax = (subtotal * tax rate)/100
#bill_amount = subtotal + tax
#tip_amount = (bill_amount*tip)/100
#total=bill_amount + tip

subtotal_children = float(number_children * child_price)
subtotal_adults = float(number_adults * adults_price)
subtotal = subtotal_children + subtotal_adults
sales_tax = (subtotal * tax) / 100
bill_amount = subtotal + sales_tax
tip_amount = (bill_amount * tip) / 100
total = bill_amount + tip_amount

print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Bill Amount: ${bill_amount:.2f}')
print(f'Tip percent: {tip:.2f} %')
print(f'Total tip: ${tip_amount:.2f}')
print(f'Total: ${total:.2f}')
print()

payment = float(input('What is the amount? '))
change = payment - total
print(f'Change: ${change:.2f}')