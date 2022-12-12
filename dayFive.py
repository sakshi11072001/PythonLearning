#Declare an empty list

empty_lists = []
print(type(empty_lists))

#Declare a list with more than 5 items
empty_lists = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff']
print(empty_lists)

#Find the length of your list
print(f"{len(empty_lists)}")

#Get the first item, the middle item and the last item of the list
print(f"{empty_lists[0]}" )
last_index = len(empty_lists) - 1
print(f"{empty_lists[last_index]}")
middle_index = int(len(empty_lists) / 2)
print(f"{empty_lists[middle_index]}")

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['sakshi', 21, 116, 'single', 'India']
print(f"{type(mixed_data_types)}")

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft,
# Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#Print the list using print()
print(f"{it_companies}")

#Print the number of companies in the list
print(f"{len(it_companies)}")

#Print the first, middle and last company
print(it_companies[0])
middle_it_companies = int(len(it_companies) / 2)
print(it_companies[middle_index])
last_it_companies = len(it_companies) - 1
print(it_companies[last_it_companies])

#Print the list after modifying one of the companies
it_companies[1] = 'crowdstaffing'
print(f"{it_companies}")

#Add an IT company to it_companies
it_companies.insert(2, 'prosperix')
print(f"{it_companies}")

#Insert an IT company in the middle of the companies list
mid_it_companies = int(len(it_companies) / 2)
print(f"{mid_it_companies}")

#Change one of the it_companies names to uppercase (IBM excluded!)
print(f"{it_companies[3].upper()}")

#Join the it_companies with a string '#;  '
joiner = '#; '
print(f"{joiner.join(it_companies)}")

#Check if a certain company exists in the it_companies list.
print(f"{'Facebook' in it_companies}")

#Sort the list using sort() method
it_companies.sort()
print(it_companies)

#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(f"{it_companies}")

#Slice out the first 3 companies from the list
print(f"{it_companies[:3]}")

#Slice out the last 3 companies from the list
print(f"{it_companies[-3:]}")

#Slice out the middle IT company or companies from the list
slice_mid =int(len(it_companies) / 2)
mid = it_companies[slice_mid : ]

#Remove the first IT company from the list
del it_companies[0]
print(f"{it_companies}")

#Remove the middle IT company or companies from the list
remove_mid = int(len(it_companies) / 2)
del it_companies[remove_mid]
print(f"{it_companies}")

#Remove the last IT company from the list
remove_last = int(len(it_companies) - 1)
del it_companies[remove_last]
print(f"{it_companies}")

#Remove all IT companies from the list
'''del it_companies
print(f"{it_companies}")   # Error'''

#Destroy the IT companies list
it_companies.clear()
print(it_companies)

'''join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB'] '''

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB'] 
front_end.extend(back_end)
print(f"{front_end}")
#method 2
'''print(f"{front_end + back_end}")'''

#After joining the lists in question 26. Copy the joined list 
#and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end.copy()
print(full_stack)
index_of_Redux = int(full_stack.index('Redux') + 1)
full_stack.insert(index_of_Redux, 'python' )
print(full_stack)
index_of_python = int(full_stack.index('python') + 1)
full_stack.insert(index_of_python, 'SQL')
print(full_stack)

# -------------------------------------------------------------------------------------- 
'''                                level -2                                            '''
'''The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]'''

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
ages.sort()
print(f"{ages}")

#Add the min age and the max age again to the list
a = min(ages)
b = max(ages)
print(f"{a + b}")

#Find the median age (one middle item or two middle items divided by two)
middle_age = int(len(ages) / 2)
print(f"{ages[middle_age]}")

#Find the average age (sum of all items divided by their number ) 
sum_age = sum(ages)
total = len(ages) - 1
average_value= sum_age / total
print(f"{sum_age / total}")

#Find the range of the ages (max minus min)
print(f"{b - a}") 

#Compare the value of (min - average) and (max - average), use abs() method
c = abs(a - average_value)
print(c)
d = abs(b - average_value)
print(d)
#Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
index_mid_country = int(len(countries) / 2)
mid_country = countries[index_mid_country]
print(f"{mid_country}")

#Divide the countries list into two equal lists if it is even if not 
# one more country for the first half.
#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'].
floor_index_mid_country = int(len(countries) // 2) 
print(f"{countries[floor_index_mid_country : ]}")
print(f"{countries[: floor_index_mid_country]}")
