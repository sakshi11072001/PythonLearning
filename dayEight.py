#Create an empty dictionary called dog
dog = {}

#Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'orio', 'color':'red', 'breed':'sitzoo', 'legs':4, 'age':12 }
print(f"{type(dog)}")
print(f"{dog}")

#Create a student dictionary and add first_name, last_name, gender, age, 
# marital status, skills, country, city and address as keys for the dictionary
student = {'first_name':'sakshi', 'last_name':'jain', 'gender':'female', 'age':23, 'marital status':'single',
'skills':'python', 'country':'India', 'city':'Bengaluru', 'address':'jpnagar'}

#Get the length of the student dictionary
print(f"{len(student)}")

#Get the value of skills and check the data type, it should be a list
print(f"{student['skills']} {type(student['skills'])}") #--> 'str'

#Modify the skills values by adding one or two skills
student['skills'] = 'java', 'cpp'
print(f"{student['skills']}")

#Get the dictionary keys as a list
keys = student.keys()
print(f"{keys}")

#Get the dictionary values as a list
values_dic = student.values()
print(f"{values_dic}")

#Change the dictionary to a list of tuples using items() method
print(f"{student.items()}")

#Delete one of the items in the dictionary
student.pop('address')

#Delete one of the dictionaries
del student
