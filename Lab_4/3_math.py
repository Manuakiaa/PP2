import math

degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
print("Output radian:", round(radian, 6))

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
area_trapezoid = (base1 + base2) * height / 2
print("Expected Output:", area_trapezoid)

sides = int(input("Input number of sides: "))
side_len = float(input("Input the length of a side: "))
area_polygon = (sides * side_len ** 2) / (4 * math.tan(math.pi / sides))
print("The area of the polygon is:", round(area_polygon, 3))

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area_parallelogram = base * height
print("Expected Output:", area_parallelogram)
