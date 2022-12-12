import math
'''Declare a function add_two_numbers. It takes two parameters and it returns a sum.'''
def add_two_numbers(x, y):
    add = x + y
    return add
print(f"{add_two_numbers('30.0', '20.7')}")

'''Area of a circle is calculated as follows: area = π x r x r.
Write a function that calculates area_of_circle.'''
def area_circle(radius):
    area = math.pi * radius * radius
    return area
print(f"{area_circle(2)}")

'''Write a function called add_all_nums which takes arbitrary number of arguments and
sums all the arguments. Check if all the list items are number types.
If not do give a reasonable feedback.'''
def add_all_nums(*nums):
    total = 0
    for num in nums:
     if type(num) == int:
      total += num  
     else:
         print("wrong type")   
    return total
print(add_all_nums(2, 3, 'a'))

'''Temperature in °C can be converted to °F using this formula: 
°F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit '''

def temprature(celsius):
    fahrenheit = (celsius * int(9 / 5) + 32)
    print(fahrenheit)
temprature(20.2)

'''Write a function called check-season, 
it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.'''

def check_season(month):
    if month in ('January', 'February', 'March'):
     print('winter')
    elif month in ('April', 'May', 'June'):
     print('spring')
    elif month in ('July', 'August', 'September'):
     print('summer')
    else:
     print('autumn')
check_season('January')

'''Write a function called calculate_slope which return the slope of a linear equation'''
def calculate_slope(y):
    x_value = y / 2
    return x_value
print(calculate_slope(20))

'''Quadratic equation is calculated as follows: ax² + bx + c = 0.
Write a function which calculates solution set of a quadratic equation, solve_quadratic_eq'''
def solve_quadratic_eq(a, b, c, x):
    equation = 0
    equation = (a * x**2) + (b * x) + c
    print(equation)
solve_quadratic_eq(2, 2, 2, 2)
'''Declare a function named print_list. 
It takes a list as a parameter and it prints out each element of the list.'''
def print_list(num = []):
    for nums in num:
     print(nums)
print_list([2, 3, 4])
'''Declare a function named reverse_list. It takes an array as a parameter
and it returns the reverse of the array (use loops).'''
def  reverse_list(number = []):
    for num in reversed(number):
     print(num)    
reverse_list([33, 44])
