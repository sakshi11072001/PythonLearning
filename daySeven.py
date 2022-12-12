#Find the length of the set it_companies
it_companies = {'Google', 'Amazon', 'oracle', 'Microsoft'}
print(f"{len(it_companies)}")

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(f"{it_companies}")

#Insert multiple IT companies at once to the set it_companies
it_companies.update(['aaa', 'bbb', 'ccc'])
print(f"{it_companies}")
                     
#Remove one of the companies from the set it_companies
it_companies.remove('aaa')
print(f"{it_companies}")

#What is the difference between remove and discard
it_companies.discard('a')

#it_companies.remove(1) --Error
print(f"{it_companies}")
#--------------------------------------------------------------------------------------------------
#                  level 2
#Join A and B
a = {1, 2, 3}
b = {11, 22, 33}
print(f"{a.union(b)}")
#method 2
a.update(b)
print(f"{a}")

#Find A intersection B
print(f"{a.intersection(b)}")

#Is A subset of B
print(f"{b.issubset(a)}")

#Are A and B disjoint sets
print(f"{a.isdisjoint(b)}")

#Join A with B and B with A
print(f"{a.union(b)}{b.union(a)}")
#What is the symmetric difference between A and B
print(f"{a.symmetric_difference(b)}")
#Delete the sets completely
# a.clear() --> just deletes the values not the set
del a, b
#--------------------------------------------------------------------------------------------------------
                         #level 3
#age = [22, 19, 24, 25, 26, 24, 25, 24]                       
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print(age_set)
print(f"{type(age_set)}")
a = len(age)
b = len(age_set)
print(f"{(a>b)}")

#I am a teacher and I love to inspire and teach people. 
#How many unique words have been used in the sentence? Use the split methods and set to get the unique words
sentence = {"I am a teacher and I love to inspire and teach people"}
sentence_str = str(sentence)
sentence = sentence_str.split() 
sentence_set = set(sentence)
print(f"{sentence_set}")



