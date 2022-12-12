#Filter only negative and zero in the list using list comprehension
#numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [i for i in range(-10,11) if i > 0]
print(numbers)

#Flatten the following list of lists of lists to a one dimensional list :
#list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
#output
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
list_of = [i for items in list_of_lists for item in items for i in item]
print(list_of)
'''Using list comprehension create the following list of tuples:'''
x = [tuple(x ** abs(i) for i in range(-1, 6)) for x in range(10)]
print(x)

'''Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]'''

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
res = [list(ele) for i in countries for ele in i]
print(res)
 
'''Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']'''

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
res = [''.join(i) for ele in names for i in ele]
print(res)

"Write a lambda function which can solve a slope or y-intercept of linear functions."
slope_of = lambda x, y, a, b: b - y / a - x
y_intercept = lambda slope_line, a, b: - slope_line * a + b
print(slope_of(2,5,6,7))
print(y_intercept(4, 5, 6))

