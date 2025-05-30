import math

pi = math.pi

print ("Which shape would you like to find the area of. Please enter the numeric value of the options below:")
print ("""1) Square
2) Rectangle
3) Triangle
4) Circle""")
shape = int(input("Please choose a shape:    "))

if shape == 1:
    side = int(input("Please enter the length of the square side.   "))
    
    area = side ** 2
    print ("The area of the square is " + str(area))
elif shape == 2:
    length = int(input("Please enter the length of the rectangle."))
    width = int(input("Please enter the width of the rectangle."))

    area = length * width
    print ("The area of the rectangle is " + str(area))
elif shape == 3:
    height = int(input("Please enter the height of the triangle."))
    base = int(input("Please enter the base length of the triangle."))

    area = (height * base) / 2
    print ("The area of the triangle is " + str(area))
elif shape == 4:
    radius = int(input("Please enter the radius of the circle."))

    area = pi * radius ** 2
    print ("The area of the circle is " + str(area))
else:
    print (("Please enter the numeric value of the shape you want to calculate."))
