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
print('Slope is : '+ str(2))
print('x-intercept is '+ str(0))
print('y-intercept is '+ str(-2))

print('-----------------------------------------------')

#Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point (6,10)
def slope(x1, y1, x2, y2):
    """
    It takes four numbers as input and returns the slope of the line that passes through the points
    (x_1, y_1)$ and (x_2, y_2)
    
    :param x1: x-coordinate of the first point
    :param y1: y-coordinate of the first point
    :param x2: x-coordinate of the second point
    :param y2: the y-coordinate of the second point
    :return: The slope of the line between the two points.
    """
    return (y2-y1)/(x2-x1)
print(f'The slope is {slope(2,2,6,10)}')

print('-----------------------------------------------')

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.
def calculo(x = 0):
    return x**2 + 6*x + 9

print(f'Calc x**2 + 6*x + 9 when x is 0: {calculo(0)}')

print('-----------------------------------------------')

#Use and operator to check if 'on' is found in both 'python' and 'jargon'
py = len('python')
jar = len('jargon')
print(py < jar)

print('-----------------------------------------------')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon'
print('jargon' in sentence)

print('-----------------------------------------------')

#There is no 'on' in both dragon and python
print('on' in 'dragon' and 'on' in 'python')

print('-----------------------------------------------')

#Find the length of the text python and convert the value to float and convert it to string
len_py = str(float(len('python')))
print(len_py)

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?


