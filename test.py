'''Declare a function named capitalize_list_items. 
It takes a list as a parameter and it returns a capitalized list of items'''
def capitalize_list_items (items):
    item = []
    for i in items:
     item.append(i.upper())
    print(item)
capitalize_list_items(['yyyy', 'sss'])


'''Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))     [2, 3, 7, 9, 5]'''

def add_items(list,element):
    list.append(element)
    return list
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_items(food_staff, 'Meat'))

'''Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050'''
def sum_of_numbers(number):
    addition = sum(range(number + 1))
    print(addition)
sum_of_numbers(5)

'''Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.'''
def sum_of_odds(number):
    a = sum(range(1, number + 1, 2))
    print(a)
sum_of_odds(5)

'''Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.'''
def sum_of_even(number):
   b = sum(range(0, number + 1, 2))
   print(b)
sum_of_even(5)
#------------------------------------------------------------------------------------------------
#                       levl 2
'''Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.'''
def evens_and_odds(number):
    even_list = []
    odd_list = []
    for x_2 in range(0, number + 1, 2):
                even_list.append(x_2)
    for x in range (1, number + 1, 2):
           odd_list.append(x_2)
    print(len(even_list))
    print(len(odd_list))
evens_and_odds(0)

'''Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number'''
def factorial(number):
    fact = 1
    for i in range(1, number + 1):
     fact = fact * i
    print(fact)
factorial(5)
'''Call your function is_empty, it takes a parameter and it checks if it is empty or not'''
def is_empty(name = None):
    if name == None:
     print("empty")
    else:
     print("full")
is_empty(4)
'''Write different functions which take lists. 
They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).'''
def calculate_mean(lists):
    n = len(lists)
    addition = sum(lists)
    mean = addition / n
    return mean
print(calculate_mean([1, 2, 3, 4, 5]))