def main():

    start_miles = float(input("Enter inicial odometer: "))

    end_miles = float(input("Eneter final odometer: "))

    amount_gallons = float(input("Enter gallons: "))

    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    lp100k = lp100k_from_mpg(mpg)

    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.2f} liter per 100 kilometers") 

def miles_per_gallon(start_miles, end_miles, amount_gallons):

    mpg = (end_miles - start_miles) / amount_gallons
    
    return mpg

def lp100k_from_mpg(mpg):

    lp100k = 235.215 / mpg

    return lp100k

main()

