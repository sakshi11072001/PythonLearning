#Create an empty tuple
empty_tuple = ()
print(f"{type(empty_tuple)}")

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brother_tuple = ('aaaa', 'bbbbb', 'cccc')
sister_tuple = ('zzz', 'xxxx' , 'yyyyy')
print(f"{type(brother_tuple)}")
print(f"{type(sister_tuple)}")

#Join brothers and sisters tuples and assign it to siblings
siblings_tuple = sister_tuple + brother_tuple
print(f"{type(siblings_tuple)}")

#method 2 
sss = (*sister_tuple, *brother_tuple)
print(f"{sss}")

#How many siblings do you have?
print(f"{len(siblings_tuple)}")

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('kkkk', 'ssss')
family_members = siblings_tuple + parents
print(family_members)

#method 2 
family_members = (*siblings_tuple, *parents)

#----------------------------------------------------------------------------------
                                 #level 2
#Unpack siblings and parents from family_members
#('sibling', 'siblings', 'siblings', 'siblings', 'siblings', 'siblings', 'parents', 'parents')
family_members = *siblings_tuple, parents, parents
print(siblings_tuple)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to 
# a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'strawberry')
vegetables = ('cucumber', 'potato', 'carrot', 'cabbage')
animal = ('cat', 'dog')
food_stuff_tp = fruits + vegetables + animal
print(f"{food_stuff_tp}")

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(f"{type(food_stuff_lt)}")

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = int(len(food_stuff_lt) / 2)
print(f"{food_stuff_lt[middle]}")

#Slice out the first three items and the last three items from food_staff_lt list
print(f"{food_stuff_lt[0:3]}")
print(f"{food_stuff_lt[-3:]}")

#Delete the food_staff_tp tuple completely
#food_stuff_tp.pop()  ==> tuple cant be poped
del food_stuff_tp

#Check if an item exists in tuple:
#nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f"{'Estonia' in nordic_countries}")

#Check if 'Iceland' is a nordic country
print(f"{'Iceland' in nordic_countries}")