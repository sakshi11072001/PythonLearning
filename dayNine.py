#Get user input using input(“Enter your age: ”).If user is 18 or older,give feedback: You are 
# old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
#Enter your age: 30
#You are old enough to learn to drive.
#Output:
#Enter your age: 15
#You need 3 more years to learn to drive.

my_age = int(input('Enter age:'))
if my_age >= 18:
   print("You are old enough to drive")
else :
    print(f"{'wait for the missing amount of years'}")

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use 
# input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year'
# for 1 year difference in age, 'years' for bigger differences, and a custom text if 
# my_age = your_age. Output:
#Enter your age: 30
#You are 5 years older than me.
your_age = int(input("Enter your age:"))
if my_age > your_age:
    gap = my_age - your_age
    if gap >= 1:
        print(f"{'I m'} {gap} {'younger years than you'}")
    else: 
        print(f"{'I m'} {gap} {'younger year older than you'}")
else:
    gap = your_age - my_age
    if gap >= 1:
        print(f"{'your'} {gap} {'older years than me'}")
    else: 
        print(f"{'your'} {gap} {'older year older than me'}")
        
#Get two numbers from the user using input prompt.If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b. Output:
#Enter number one: 4
#Enter number two: 3
#4 is greater than 3

a = int(input("Enter first number"))
b = int(input("Enter second number"))
if a > b:
    print(f"{'a is greater than b'}")
elif b > a:
    print(f"{'b is greater than a'}")
else:
    print(f"{'both are equal'}")
    
#--------------------------------------------------------------
#                 level 2
#Write a code which gives grade to students according to theirs scores:
#80-100, A
#70-89, B
#60-69, C
#50-59, D
#0-49, F

marks = int(input("enter the marks:"))
if marks == 0 or marks <= 49:
    print(f"{'grade: F'}")  
elif marks == 50 or marks <= 59:
    print(f"{'grade : D'}")
elif marks == 60 or marks <= 69:
    print(f"{'grade : C'}")
elif marks == 70 or marks <= 89:
    print(f"{'grade : B'}")
elif marks == 80 or marks <= 100:
    print(f"{'grade : A'}")
else:
    print(f"{'invalid marks'}")
    
#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September,
# October or November, the season is Autumn. December, January or February, the season is 
# Winter. March, April or May, the season is Spring June, July or August, the season is Summer

season = input("Enter the month:")
if season == 'September' or season == 'October'  or season == 'November':
    print(f"{'its autum'}")
elif season == 'December' or season == 'January' or season == 'February':
    print(f"{'its winter'}")
elif season == 'March' or season == 'April'  or season == 'May':
    print(f"{'its spring'}")
elif season == 'June' or season == 'July'  or season == 'August':
    print(f"{'its summer'}")
    
#The following list contains some fruits:
#fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
#If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
input_fruit = input('Enter the fruit:')
if input_fruit in fruits:
    print(f"{'fruit exist'}")
else:
    fruits.append(input_fruit)
    print(f"{fruits}")
#--------------------------------------------------------------------------------------
#                         level 3

#Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#* Check if the person dictionary has skills key, if so print out the middle skill in the 
# skills list.
if person['skills']:
    skill = person['skills']
    middle = int(len(skill)/2)
    print(f"{'middle element is:'}{skill[middle]}")
    
#check if the person has 'Python' skill and print out the result.   
if 'Python' in person['skills']:
    print(f"{'Python' in person['skills']}")

#* If a person skills has only JavaScript and React, print('He is a front end developer')
#if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
# else print('unknown title') - for more accurate results more conditions can be nested!

if 'JavaScript' and 'React' in person['skills']:
    print(f"{'He is a front end developer'}")
elif 'Node' and 'Python' and 'MongoDB' in person['skills']:
    print("{'He is a backend developer'}")
elif 'Node' and 'Python' and 'MongoDB' in person['skills']:
    print(f"{'He is a fullstack developer'}")
else:
    print(f"{'umknown title'}")

#If the person is married and if he lives in Finland, 
# print the information in the following format:
if person['is_marred'] == True:
    if person['country'] =='Finland':
     print(f"{person['first_name']} {'lives in'} {person['country']}")
    
