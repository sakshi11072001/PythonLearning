import random
import string
def ran():
    ran_num = random . random()
    return ran_num
print(ran()) 

def print_id():
    num_characters = int(input("Enter the number of characters:"))
    num_ids = int(input("Enter the number of ids:"))
    for i in range(num_ids):
        letters_and_digits = string.ascii_letters + string.digits
        result_is = ''.join((random.choice(letters_and_digits) for j in range(num_characters)))
        print(result_is)  
print_id()