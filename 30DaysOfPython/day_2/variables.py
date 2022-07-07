#Day 2: 30 Days of python programming

first_name = 'German'
last_name = 'Medina'
full_name = first_name + '' + last_name
country = 'Argentina'
city = "Buenos Aires"
age = 31
year = 2022
is_married = True
is_true = True
is_light_on = False
var_1, var_2, var_3, var_4 = 'var1', 'var2', 'var3', 'var4'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))

print(len(first_name))

print(f'The length of me first name is {len(first_name)} and the lastname is {len(last_name)}')

num_one = 5
num_two = 4
_total = num_one + num_two
_diff = num_one - num_two
_product = num_one * num_two
_division = num_one / num_two
_remainder = num_two % num_one
_exp = num_one ** num_two
_floor_division = num_one // num_two

PI = 3.14159265359
RADIO = 30

area_of_circle = PI * RADIO**2
circum_of_circle = 2 * PI * RADIO

input_radio = int(input('Give me a number: )'))

print(PI * input_radio**2)

first_name = input('Hi!, whats is your name?: ')
last_name = input('And lastname?: ')
country = input('Where are you from?: ')
age = int(input('Whats your Age?: '))

print(help('keywords'))