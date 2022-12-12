#Open you python interactive shell and try all the examples covered in this section
#SYSTEMERROR 
'''a = ''Hello 
python This is 
Sakshi''
print(a)         -->SyntaxError: invalid syntax '''

# IDENTATIONERROR
'''for i in range(10):
print(i)         -->IndentationError: expected an indented block after 'for' statement on line 9'''

#INDEXERROR
'''l = [1, 2, 3]
print(l[6])       -->IndexError: list index out of range'''

#KEYERROR
'''dicc = {"name" : 'kkk', "rollno" : 56}
dicc["branch"]        -->KeyError: 'branch' '''

#NAMEERROR
'''a, b, c = 12, 30, 45
print(s)               -->NameError: name 's' is not defined'''

#TYPEERROR
'''a = "string"
b = 10
print(a + b)            -->TypeError: can only concatenate str (not "int") to str'''

#VALUEERROR
'''a = "string"
b = int(a)
print(b)  -->ValueError: invalid literal for int() with base 10: 'string'm '''

#ZERODIVISIONERROR
'''a = 10
b = 0
print(a / b)  -->ZeroDivisionError: division by zero '''

#MODULENOTFOUNDERROR
'''import randomin  -->ModuleNotFoundError: No module named 'randomin' '''

#ATTRIBUTEERROR
'''import math
print(math.PI)  -->AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?'''


