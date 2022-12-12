#Open you python interactive shell and try all the examples covered in this section


#SYNTAXERROR 
#WRONG WAY:-
'''
a = ''Hello python!!
    This is Sakshi''
print(a)         -->SyntaxError: invalid syntax 
'''

#CORRECT WAY:-
a = '''Hello python!!
    This is Sakshi'''
print(a)

#---------------------------------------------------------------------------------------------------


# IDENTATIONERROR
#WRONG WAY:-
'''
for i in range(10):
print(i)         -->IndentationError: expected an indented block after 'for' statement on line 9

'''

#CORRECT WAY:-
for i in range(10):
    print(i)   

#-----------------------------------------------------------------------------------------------

#INDEXERROR

#WRONG WAY:-
'''
l = [1, 2, 3]
print(l[6])       -->IndexError: list index out of range

'''

#CORRECT WAY:-
l = [1, 2, 3]
print(l[2])  

#------------------------------------------------------------------------

#KEYERROR

#WRONG WAY:-
'''
dicc = {"name" : 'kkk', "rollno" : 56}
dicc["branch"]        -->KeyError: 'branch'

'''

#CORRECT WAY:-
dicc = {"name" : 'kkk', "rollno" : 56}
dicc["name"]  

#---------------------------------------------------------------------------

#NAMEERROR

#WRONG WAY:-
'''
a, b, c = 12, 30, 45
print(s)               -->NameError: name 's' is not defined

'''

#CORRECT WAY:-
a, b, c = 12, 30, 45
print(a) 

#---------------------------------------------------------------------------------

#TYPEERROR

#WRONG WAY:-
'''
a = "string"
b = 10
print(a + b)            -->TypeError: can only concatenate str (not "int") to str

'''

#CORRECT WAY:-
a = 20
b = 10
print(a + b)

#----------------------------------------------------------------------------------

#VALUEERROR

#WRONG WAY:-
'''
a = "string"
b = int(a)
print(b)  -->ValueError: invalid literal for int() with base 10: 'string'm 

'''
#CORRECT WAY:-
a = 10.7
b = int(a)
print(b)

#----------------------------------------------------------------------------------------------

#ZERODIVISIONERROR

#WRONG WAY:-
'''
a = 10
b = 0
print(a / b)  -->ZeroDivisionError: division by zero 
'''

#MODULENOTFOUNDERROR

#WRONG WAY:-
'''
# import randomin  -->ModuleNotFoundError: No module named 'randomin'
'''
#CORRECT WAY:-
import random 
 
#-----------------------------------------------------------------------------

#ATTRIBUTEERROR

#WRONG WAY:-
'''
import math
print(math.PI)  -->AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?

'''
#CORRECT WAY:-
import math
print(math.pi)

#-----------------------------------------------------------------------