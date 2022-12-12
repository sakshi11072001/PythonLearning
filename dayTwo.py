#Declare a first name variable and assign a value to it
from itertools import product
from math import remainder
from pickletools import read_unicodestring1


FirstName = "Sakshi"
print(FirstName)

#Declare a last name variable and assign a value to it
LastName = "Jain"
print(LastName)

#Declare a full name variable and assign a value to it
FullName = "Sakshi Jain"
print(FullName)

#Declare a country variable and assign a value to it
country = "India"
print(country)

#Declare a city variable and assign a value to it
city = "Bengaluru"
print(city)

#Declare an age variable and assign a value to it
age = 21
print(age)

#Declare a year variable and assign a value to it
year = 2022
print(year)

#Declare a variable is_married and assign a value to it
is_married = False
print(is_married) 

#Declare a variable is_true and assign a value to it
is_true = True
print(is_true)

#Declare a variable is_light_on and assign a value to it
is_light_on = "on"
print(is_light_on)

#Declare multiple variable on one line
college = '''an educational institution or 
establishment, in particular 
one providing higher education or 
specialized professional or vocational training.'''
print(college)

#Check the data type of all your variables using type() built-in function
print(type(5))
print(type({" sak " , " jsjn "}))
print(type([1,2,3]))
print(type({" Name ": " sakshi "}))

#Using the len() built-in function, find the length of your first name
print(len(FirstName))

#Compare the length of your first name and your last name
a = len(FirstName)
print("length of firstName")
print(a)
b = len(LastName)
print("and length of LastName")
print(b)

'''Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division''' 

num_one = 5
num_two = 4
totatl = num_one + num_two
print(totatl)

product = num_one * num_two
print(product)

division = num_one % num_two
print(division)

remainder = num_one / num_two
print(remainder)

exp = num_one ** num_two
print(exp)

floor_divison = num_one // num_two
print(floor_divison)

'''The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.'''

radius = 30

area_of_circle = 3.14159 * radius
print(area_of_circle)

circum_of_circle = 2 * 3.14159 * radius
print(circum_of_circle)

'''Use the built-in input function to get first name, last name, country and 
age from a user and store the value to their corresponding variable names'''
 
print("Enter your First name:")
x = input()
print("Hello, " + x)

print("Enter your last name:")
y = input()
print("hello" + " " +y)

print("Enter your age:")
z = input()
print(z)

print("Enter your country name:")
w = imput()
print(w)

'''Run help('keywords') in Python shell or in your file 
to check for the Python reserved words or keywords'''

help(True)
help(while)
help(try)
