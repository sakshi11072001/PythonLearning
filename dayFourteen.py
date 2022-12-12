from functools import reduce
from operator import itemgetter
import string
#Explain the difference between map, filter, and reduce.
num = [22, 33, 44, 55]
map_grt = list(map(lambda x : x < 55, num))
print(map_grt)
filter_grt = list(filter(lambda x : x < 44, num))
print(filter_grt)
reduce_grt = reduce(lambda x, y : x * y, num)
print(reduce_grt)

#Define a call function before map, filter or reduce, see examples.
def square(a):
    return a * a
print(square(9))

l = [1, 2, 3, 4]
map_fun = list(map(square, l))
print(map_fun)

filter_fun = list(filter(lambda n: n > 1, l))
print(filter_fun)

reduce_fun = reduce(lambda x, y: x * x, l)
print(reduce_fun)

#Use for loop to print each country in the countries list.
# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for i in countries:
    print(i)
    
#Use for to print each name in the names list.
#names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for i in names:
    print(i)

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print(i)
#-----------------------------level 2-------------------------------------
#Use map to create a new list by changing each country to uppercase in the countries list
map_upper = list(map(lambda country : country.upper(), countries))
print(map_upper)

#Use map to create a new list by changing each number to its square in the numbers list
map_num = list(map(lambda a : a * a, numbers))
print(map_num)

#Use map to change each name to uppercase in the names list
map_names = list(map(lambda names : names.upper(), names))
print(map_names)

#Use filter to filter out countries containing 'land'.
'''def land(countries):
    if 'land' in countries:
        print(countries)
land(countries)'''

filter_country = list(filter(lambda countries : 'land' in countries, countries))
print(filter_country)

#Use filter to filter out countries having exactly six characters.
filter_char = list(filter(lambda country : len(country) == 6, countries))
print(filter_char)

#Use filter to filter out countries containing six letters and more in the country list.
filter_six_more = list(filter(lambda country : len(country) >= 6, countries))
print(filter_six_more)

#Use filter to filter out countries starting with an 'E'
filter_e = list(filter(lambda item : item.startswith('E'), countries))
print(filter_e)

#Declare a function called get_int_lists which takes
# a list as a parameter and then returns a list containing only int items.
l = list(filter(lambda get_int_lists : type(get_int_lists) == int, numbers))
print(l)

#Use reduce to sum all the numbers in the numbers list.
reduce_func = reduce(lambda a, b : a + b, numbers)
print(reduce_func)

#Use reduce to concatenate all the countries and to produce this sentence: 
reduce_str = reduce(lambda a, b : a + b, countries)
print(reduce_str)
