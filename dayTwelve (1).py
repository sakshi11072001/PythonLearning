#import sys
#sys.path.insert(1, r'C:\Users\SAKSHI JAIN\pythons.py\random_values.py')
#sys.path.insert(1, r'C:\Users\SAKSHI JAIN\pythons.py\rgb.py')
from my_pack.random_values import ran as rv
from my_pack.random_values import print_id as rv
from my_pack.rgb import rgb 

#import rgb
'''Writ a function which generates a six digit/character random_user_id'''
random_num = rv.ran()
print(random_num)

'''Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input().
One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.'''
print(rv.print_id())

'''Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).'''
print(rgb.rgb_color_gen()) 