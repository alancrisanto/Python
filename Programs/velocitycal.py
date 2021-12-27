import math


print("Welcome to the velocity calculator. Please enter the following:")
print()

m = float(input("Mass (in Kg): "))
g = float(input("Gravity (in m/s^2. 9.8 for earth. 24 for jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3 , 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

c= (1/2)* p * A * C
v_t = math.sqrt((m*g)/c) * (1-math.exp((- math.sqrt(m*g*c)/m)* t))

print(f"The inner value of c is: {c:.3f}")
print(f"The velicity after {t} seconds is: {v_t:.3f} m/s")

jupiter = math.sqrt((m*24)/c) * (1-math.exp((- math.sqrt(m*24*c)/m) * t))
print(f"In Jupiter the velocity is {jupiter:.3f}")                                                                                  