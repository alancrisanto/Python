#number=7
#number_2=10
#print(f'my number is {number + number_2}')
#print('my number is ' + str(number + number_2))

print('Areas'.center(50))
print()

length=float(input('What is the length side of a square? '))
area_square=length**2
print(f'The area of the square is: {area_square}')
rectangle_length=float(input('What is the lenght of a rectangle? '))
rectangle_width=float(input('What is the width of a rectangle? '))
rectangle_area= rectangle_length*rectangle_width
print(f'The area of a rectangle is: {rectangle_area}')
radius=float(input('What is the radius of the circle? '))
import math
pi=math.pi
circle_area=(radius**2)*pi
print(f'The area of the circle is {circle_area:.2f}')

#Challenge #2
print()
print('Challenge #2'.center(50))
print()
value=float(input('Please enter a number: '))
print()
area_square_1=value**2
circle_area_1=(value**2)*pi
cube_area=value**3
sphere_area=(4/3)*(value**3)*pi
print(f'The area of the square is {area_square_1}')
print(f'The area of the circle is {circle_area_1:.2f}')
print(f'The area of the cube is {cube_area}')
print(f'The area of the sphere is {sphere_area:.2f}')
print()

#Challenge #3
print('Challenge #3'.center(50))
print()
value_centimeters=float(input('Please enter a value in centimeters: '))
area_square_2=value_centimeters**2
circle_area_2=(value_centimeters**2)*pi
print(f'The area of the square is {area_square_2} square centimeters and this is equal to {area_square_2/10000} m2')
print(f'The area of the circle is {circle_area_2:.2f} square centimeters, and this equal to {circle_area_2/10000:.2f} m2')
























