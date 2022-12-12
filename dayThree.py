import math
#Declare your age as integer variable

age = 21

#Declare your height as a float variable

height = 21.1

#Declare a variable that store a complex number
  
c_num = 2+3j

#Write a script that prompts the user to enter base and height of the
#triangle and calculate an area of this triangle (area = 0.5 x b x h).

base = float(input("Enter the base of triangle:"))
height = float(input("Enter the height of the triangle:"))
area = float(1/2 * base * height)
print("Area is :", + area)

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
#Calculate the perimeter of the triangle (perimeter = a + b + c).

a = float(input("Enter the side a:"))
b = float(input("Enter the side b:"))
c = float(input("Enter the side c:"))
perimeter = float(a + b + c)
print("Area of perimeter is:", + perimeter)

#Get length and width of a rectangle using prompt.
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width)).

length = int(input("Enter the length:"))
width = int(input("Enter the height: "))
arae_rect = int(length * width)
perimeter_rect = int(2 * (length + width))
print("Area is :", + arae_rect )
print("perimeter is: ",  + perimeter)

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) 
#and circumference (c = 2 x pi x r) where pi = 3.14.

radius = float(input("Enetr the radius:"))
area = float(math.pi * radius * radius)
print("Area:", + area)
circumference = 2 * math.pi * radius
print("circuference:", circumference)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2

x1 = 0 
m = 2
y1 = 2 * x1 - 2
print(y1)
x1 = 2 / 2
print(x1)
y2 = 0
x2 = 0
slope = ((y2 - y1) / (x2 - x1))
print(slope)

#Slope is (m = y2-y1/x2-x1). 
# Find the slope and Euclidean distance between point (2, 2) and point (6,10)

x1 = 2
x2 = 6
y1 = 2
y1 = 10
slope = ((y2 - y1) / (x2 - x1))
distances = math.sqrt(((x2 - x1)**2) + ((y1 - y1)**2))
print(slope)
print(distances)

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.

#python = len("python")
print(f"length of python", {len("python")})
print(f"length of dragon", {len("dragon")})
print(len("python") == len("dragon"))

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
a = "python"
b = "on"
print(a and b)

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
c = " hope this course is not full of jargon"
print("jargon" in c)

#There is no 'on' in both dragon and python
print(a != b)
print("jargon" != "on")

#Find the length of the text python and convert the value to float and convert it to string

lengths = len("python")
print("length:", lengths)
c = float(lengths)
print(type(c))
print(c)
d = str(c)
print(d)
print(type(d))

#Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?

number = input("Enter a number:")
num = number % 2
print (num == 0)

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

no = 7 // 3
numb = 2.7
print(no and numb)

#Check if type of '10' is equal to type of 10

print(type(10))
print(type('10'))

#Check if int('9.8') is equal to 10

integers = 9.8
n = 10
print(integers == n)

#Writ a script that prompts the user to enter hours and rate per hour. 
# Calculate pay of the person?
hours = int(input("enter the hours:"))
rate_per_hours = int(input("enter the rate per hour:"))
pay = hours * rate_per_hours
print("pay is :", pay)

#Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. Assume a person can live hundred years

year = int(input("Enter the number of years you lived:"))
seconds = year * 31,536,000
print("no of seconds:", seconds)

#Write a Python script that displays the following table
'''1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125'''
