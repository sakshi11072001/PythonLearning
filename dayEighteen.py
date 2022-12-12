import re
"""Write a pattern which identifies if a string is a valid python variable
is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True"""

import re
s = input("Enter a string")
pattern = r'^[A-Za-z_][A-Za-z0-9_$]*'
if(re.search(pattern,s)):
    print("True")
else:
    print("False")
    
"""Clean the following text. After cleaning, count three most frequent words in the string."""

match = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; 
&as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. 
%Do@es thi%s mo@tivate yo@u to be a tea@cher!?"""
a = r"[^a-zA-Z\s]+"
strings = re.split(a, match)
print(strings)
set1=set()
for i in strings:
    set1.add((i,strings.count(i)))
print((set1))




import re
import os
b = os.listdir("C:/Users/SAKSHI JAIN/pythonLearning/backup2")

def funct(files):
    regx = r'[a-bA-B][_][0-9]{4}[_][0-9]{3}[.txt]'
    for i in files: 
        if regx:
            filess = str(i)[0:13]
            number = str(i)[-7:-3]
            files_even = int(number.replace('.', ''))
            # finding even numbered files
            if files_even % 2 == 0:
                files_even = str(files_even)
                file_name = filess + files_even + '.txt' 