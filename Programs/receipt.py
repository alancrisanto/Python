import csv
from datetime import datetime

def main():
    PRODUCT_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2

    try:

        print("Products")
        print()
        products = read_products("products.csv", PRODUCT_INDEX)
        # # Printing the dictionary in order
        # for i in products:

        #     print(i, products[i])
        # # Printing the requested items
        # print()

        print("Inkom Emporium\n")
        request = process_request("request.csv", products )
        
        print(request)

        print("Thank you for shopping at the Inkom Emporium.")
        current_day = datetime.now()
        print(f"{current_day: %A %b %d %I:%M:%S %p}")

    # Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
    
    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.")
    
    except KeyError as key_error:
        print(f"Error: {key_error}")


def read_products(filename, key_column_index):

    dictionary = {}

    with open(filename, "rt") as product_list:

        read = csv.reader(product_list)
        next(read)
        # for the content row, get product, name and price
        for row in read:

            # product_id = row[0]
            name = row[1]
            price = float(row[2])

            # use the product_id as a key
            key = row[key_column_index]

            # store the data in the dictionary (name and price)

            dictionary[key] = [name, price]
    
    return dictionary

def process_request(filename, dictionary):

    PRODUCT_KEY = 0
    QUANTITY = 1
    
    with open(filename, "rt") as request:

        read_2 = csv.reader(request)

        next(read_2)

        number_items = 0
        sub_total = 0
        
        for id in read_2:

            product_key = id[PRODUCT_KEY]
            product_quantity = int(id[QUANTITY])
            value = dictionary[product_key]
            product_name = value[0]
            price = float(value[1])
            print(f"{product_name}: {product_quantity} @ {price}")

            number_items += product_quantity
            sub_total += price * product_quantity
            tax = sub_total * 0.06
            total = sub_total + tax

        print(f"\nNumber of items: {number_items}")   
        print(f"Subtotal: {sub_total}")
        print(f"Sales Tax: {tax:.2f}")
        print(f"Total: {total:.2f}")



    return ""
    

if __name__ == "__main__":
    main()