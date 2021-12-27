#Unit Conversion C° to F 
# F° to C°
fahrenheit = float(input("What is the temperature in fahrenheit? "))
formula_f = (fahrenheit - 32 ) * 5/9

print(f"The temperature in celsius is: {formula_f:.1f} degrees.")

# C° to F°
celsius = float(input("What is the temperature is Celsius? "))
formula_c = (celsius * 9/5) + 32

print(f"The temperature in fahrenheit is: {formula_c:.1f} degrees")