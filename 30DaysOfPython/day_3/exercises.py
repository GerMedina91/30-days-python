age = 31
height = 1.75
complex_var = 3 + 1j

t_base = int(input('Hi, welcome to day 3. Enter the base of a triangle: '))
t_height = int(input('Now enter the height: '))
t_area = 0.5 * (t_base * t_height)
print(f'The area of the triangle is {t_area}')

print('-----------------------------------------------')

# Calculating the perimeter of a triangle.
side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
perimeter = side_a + side_b + side_c
print(f'The perimeter of the triangle is {perimeter}')

print('-----------------------------------------------')

# Calculating the area and perimeter of a rectangle.
r_length = int(input('Enter lenght: '))
r_width = int(input('Enter width: '))
r_area = r_length * r_width
r_perimeter = 2 * (r_length * r_width)
print(f'The area of the rectangle is {r_area}')
print(f'The perimeter of the rectangle is {r_perimeter}')

print('-----------------------------------------------')

# Calculating the area and circumference of a circle.
PI = 3.14
c_radius = int(input('Enter radius: '))
c_area = PI * c_radius * c_radius
c_circumference = 2 * PI * c_radius
print(f'The area of the circle is {c_area}')
print(f'The circumference of the circle is {c_circumference}')

print('-----------------------------------------------')

#Calculate the slope, x-intercept and y-intercept of y = 2x -2

def getXandYintercept(P, Q):
 
    a = P[1] - Q[1]
    b = P[0] - Q[0]
     
    # if line is parallel to y axis
    if b == 0:
        print(P[0])         # x - intercept will be p[0]
        print("infinity")   # y - intercept will be infinity
        return
     
    # if line is parallel to x axis
    if a == 0:
        print("infinity")     # x - intercept will be infinity
        print(P[1])           # y - intercept will be p[1]
        return
     
     
         
    # Slope of the line
    m = a / b
     
    # y = mx + c in where c is unknown
    # Use any of the given point to find c
    x = P[0]
    y = P[1]
    c = y-m * x
     
    # For finding the x-intercept put y = 0
    y = 0
    x =(y-c)/m
    print(x)
     
    # For finding the y-intercept put x = 0
    x = 0
    y = m * x + c
    print(y)
 
