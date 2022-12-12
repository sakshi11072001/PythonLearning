#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a = 'Thirty'
b = 'Days' 
c = 'Of'
d = 'Python'
print(f"{a + ' ' + b + ' ' + c + ' ' + d}")

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
e = 'Coding'
f = 'For' 
g = 'All'
print(f"{e + ' ' + f + ' ' + g}")

#Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print().
print(f"{len(company)}")

#Change all the characters to uppercase letters using upper() method.
print(company.upper()) 

#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
print(f"{company[6:]}")

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(f"{company.find('Coding')}")

#Replace the word coding in the string 'Coding For All' to Python.
print(f"{company.replace('Coding', 'python')}")

#Change Python for Everyone to Python for All using the replace method or other methods.
change_string = 'Python for Everyone'
print(f"{change_string.replace('Everyone', 'All')}")

#Split the string 'Coding For All' using space as the separator (split()) .
print(f"{company.split()}")                                           
                                                                
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
spliting_strings = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(f"{spliting_strings.split(', ')}")

#What is the character at index 0 in the string Coding For All.
print(f"{company[0]}")

#What is the last index of the string Coding For All.
print(f"{(len(company) - 1)}")

#What character is at index 10 in "Coding For All" string.
print(f"{company[10]}")

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
print(f"{change_string.replace('on', '_')}")

#Create an acronym or an abbreviation for the name 'Coding For All'.
print(f"{company.replace(' ', '_')}")

#Use index to determine the position of the first occurrence of C in Coding For All.
print(f"{company.index('C')}")

#Use index to determine the position of the first occurrence of F in Coding For All.
print(f"{company.index('F')}")

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(f"{company.rindex('l')}")

#Use index or find to find the position of the first occurrence of the word 'because' in the 
# following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentences = 'You cannot end a sentence with because because because is a conjunction'
#method1
print(f"{sentences.index('because')}")
#method2
print(f"{sentences.find('because')}")

#Use rindex to find the position of the last occurrence of the word because in the following
# sentence: 'You cannot end a sentence with because because because is a conjunction'
print(f"{sentences.rindex('because')}")

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence
# with because because because is a conjunction'
print(f"{sentences[31:54]}")

#Find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print(f"{sentences.index('because')}")

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence 
# with because because because is a conjunction'
print(f"{sentences[31:54]}")

#Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
remove_space = '   Coding For All      '
print(f"{remove_space.strip()}")

'''Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python'''
print(f"{'thirty_days_of_python'.isidentifier()}")  #True
print(f"{'30DaysOfPython'.isidentifier()}")

#The following list contains the names of some of python libraries: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_librarys = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(f"{'#'.join(python_librarys)}")

#Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')

'''Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki'''
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

'''Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.'''
print('radius = 10\narea = 3.14 * radius **2\nThe area of a circle with radius is 314 meters square.')


'''Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144'''
print( '8 + 6 = 14\n8 - 6 = 2\n8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144')
