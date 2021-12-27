options = ["Add item", "View Cart", "Remove item", "Compute total", "Quit"]
items = [] 
prices = []

print("Welcome to the Shopping Cart Program!")

answer = 0

while answer != 5:

    print("\nPlease select one of the following:")
    print()

    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")

    answer = int(input("\nPlease enter an action: "))

    if answer == 1:
        item = ""
        while item.lower() != "quit":

            item = str(input("\nWhat item would you like to add? (Type QUIT to finish) "))
            
            if item.lower() != "quit":

                price = float(input(f"What is the price of {item.capitalize()} "))
                
                items.append(item)
                prices.append(price)

                print(f"\n{item.capitalize()} has been added to the cart.")
                print()

    elif answer == 2:

        print("\nThe contents of the shopping cart are:")
        
        for i in range(len(items)):
            print(f"{i + 1}. {items[i].capitalize():13}{('.')*9} ${prices[i]:8.2f}")
        # for i,(a,b) in enumerate(zip(items,prices),1):
        #     print(f'{i}. {a.capitalize():10} ${b:.2f}', end="\n") ....../line 29 and 30 is another way of how to show the 2 lists
        print()

    elif  answer == 3:

        delete = int(input("Which item would you like to remove? "))
        print("\nItem removed.")
        items.pop(delete - 1)
        prices.pop(delete - 1)
        
    elif answer == 4:
        
        total = 0
        for i in range(len(items)):
            total += prices[i]
        
        print(f"\nThe total price of the items is ${total:.2f}")
        print()

    elif answer == 5:

        print("\nThank you. Goodbye.")
        print()

    else:
        print("\nInvalid answer, try again!")
        print()