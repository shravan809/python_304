'''
#1.  Add a list of elements to a given set

set={10,11,20,66}

ls=[45,65,21,71]

for i in ls:
    set.add(i)
print('updated set is:',set)

output:
updated set is: {65, 66, 71, 10, 11, 45, 20, 21}

**************************************************************************************

#2. Return a set of identical items from a given two Python

set1={12,32,65,75,15,35,42}
set2={12,75,17,42,20,30,40}

print(set1&set2)

output:
{42, 75, 12}

*******************************************************************************************

#3.Returns a new set with all items from both sets by removing duplicates

set1={20,30,45,40,25,60,55}
set2={22,30,70,60,71,88,25}

set3=set1|set2

print(set3)
{70, 71, 40, 45, 20, 22, 55, 88, 25, 60, 30}

*******************************************************************************************

#4.Given two Python sets, update first set with items that exist only in the first set
#and not in the second set.

set1={20,30,40,70,14,12,32,44,16}
set2={20,30,14,22,55,26,98,16,75}

set3=set1-set2
print(set3)

output:
{32, 70, 40, 12, 44}

*************************************************************************************

#5.Remove 10, 20, 30 elements from a following set at once

set1={10,20,30,40,50,60}

set1.difference_update({10, 20, 30})
print(set1)

output:
{50, 40, 60}

****************************************************************************************

#6.Return a set of all elements in either A or B, but not both

set1={45,55,87,84,99,36,12}
set2={12,78,41,53,99,46,72}

print(set1^set2)

output:
{72, 78, 84, 87, 36, 41, 45, 46, 53, 55}

***************************************************************************************

#7.Determines whether or not the following two sets have any elements in common.
#If yes display the common elements

set1={20,78,45,65,55,40,77,61,12}
set2={45,21,65,55,87,95,22,63,49}

print(set1.isdisjoint(set2))

print(set1&set2)

output:
{65, 45, 55}

*******************************************************************************************

#8. Update set1 by adding items from set2, except common items

set1={45,12,78,95,63,17}
set2={81,45,12,96,76,8}

m=set1.symmetric_difference_update(set2)

print(set1)

output:
{8, 76, 78, 17, 81, 95, 96, 63}

***************************************************************************************

#9. Remove items from set1 that are not common to both set1 and set2

set1={45,12,78,95,63,17}
set2={81,45,12,96,76,8}

x=set1.intersection_update(set2)

print(set1)

output:
{12, 45}

***************************************************************************************

#10.Write a Python program to check if a given set is superset of itself and superset of another
#given set

set1={1,2,4,6,9,7}
set2={1,2,3,4}
set3={1,2,4}

print(set1.issuperset(set2))

print(set2.issuperset(set3))

print(set3.issuperset(set1))

print(set1.issuperset(set3))

output:

False
True
False
True

****************************************************************************************

#11.Write a Python program to check a given set has no elements in common with other given set

set1={1,5,4,8,9,3,2}
set2={12,45,78,98,63,3}
set3={6}

print(set1.isdisjoint(set2))

print(set1.isdisjoint(set3))

print(set3.isdisjoint(set2))

output:
False
True
True
******************************************************************************************

#12.Write a Python program to remove the intersection of a 2nd set from the 1st set.


set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

set1.difference_update(set2)

print(set1)
print(set2)

#or

#set1=set1-set2

#print(set1)
#print(set2)

output:

{1, 2, 3}
{4, 5, 6, 7, 8}
{1, 2, 3}
{4, 5, 6, 7, 8}

****************************************************************************************

#13. Perform all sets methods by taking an example of your own.

##add():	Adds an element to the set

flowers={'rose','lily','sunflower'}
flowers.add('black rose')
print(flowers)

output:
{'rose', 'sunflower', 'lily', 'black rose'}

**************************************************************************************

##clear()	Removes all the elements from the set

names={'kiran','ravi','dastagiri'}

names.clear()
print('Empty set: ',names)

output:

Empty set:  set()

***************************************************************************************

##copy()	Returns a copy of the set

cars={'benz','Audi','BMW','Honda City'}

copy_cars=cars.copy()
print(cars)
print('copied cars are :',copy_cars)

output:

{'Audi', 'benz', 'Honda City', 'BMW'}
copied cars are : {'Audi', 'benz', 'Honda City', 'BMW'}

***************************************************************************************

##difference()	Returns a set containing the difference between two or more sets

set1={1,2,45,7,8}
set2={1,8,4,6,98}

print(set1-set2)

output:

{2, 45, 7}

***************************************************************************************

##difference_update()	Removes the items in this set that are also included in another,
#specified set

set1={14,12,4,85,96,7,6}
set2={78,9,4,6,2,3,66,4}

set1.difference_update(set2)
print(set1)

output:
{96, 85, 7, 12, 14}

*****************************************************************************************

##discard()	Remove the specified item

fruits={"apple", "banana", "cherry"}

fruits.discard("cherry")
print(fruits)

output:
{'banana', 'apple'}

****************************************************************************************

##intersection()	Returns a set, that is the intersection of two or more sets

cars1={'benz','Audi','BMW','Honda City'}
cars2={'Alto 800','Audi','Breeza','Honda City'}

print(cars1&cars2)

output:

{'Honda City', 'Audi'}

******************************************************************************************

##intersection_update()	Removes the items in this set that are not present in other, specified set(s)

names1={'kiran','ravi','dastagiri','shravan'}
names2={'tagoor','charan','chiti','ravi'}

names1.intersection_update(names2)

print(names2)

output:

{'ravi'}

*******************************************************************************************

##isdisjoint()	Returns whether two sets have a intersection or not

set1={4,8,9,5,4,2,6,3,1}
set2={65,45,4,12,35,65}

print(set1.isdisjoint(set2))

output:
False

*******************************************************************************************

##issubset()	Returns whether another set contains this set or not

set1={1,4,5,8,9,6,7}
set2={4,8,6}

print(set2.issubset(set1))
print(set1.issubset(set2))

output:

True
False

******************************************************************************************

##issuperset()	Returns whether this set contains another set or not

set1={1,5,9,3,4,6,7}
set2={1,5}

print(set1.issuperset(set2))
print(set2.issuperset(set1))

output:
True
False

********************************************************************************************

##pop()	Removes an element from the set

flowers={'rose','lily','sunflower'}

flowers.pop()

print(flowers)

output:
{'sunflower', 'rose'}

******************************************************************************************

##remove()	Removes the specified element

flowers={'rose','lily','sunflower'}

flowers.remove('lily')

print(flowers)
{'rose', 'sunflower'}

***************************************************************************************

##symmetric_difference():Returns a set with the symmetric differences of two sets

set1={4,5,9,3,33,22,11,4}
set2={45,8,9,33,11,66,54,21,14}

print(set1.symmetric_difference(set2))

output:

{66, 3, 4, 5, 8, 45, 14, 21, 54, 22}

**************************************************************************************

##symmetric_difference_update()	inserts the symmetric differences from this set and another

set1={12,45,78,9,62,3,5,4,7}
set2={78,45,12,63,58,6,4,9,8}

set1.symmetric_difference_update(set2)

print(set1)

output:
{3, 5, 6, 7, 8, 58, 62, 63}

************************************************************************************

##union()	Return a set containing the union of sets

set1={1,5,8,6,54,65,6,56,1}
set2={465,87,543,54678,16,6798,4,6,65}

print(set1|set2)

output:
{65, 1, 4, 5, 6, 8, 6798, 16, 465, 54678, 87, 543, 54, 56}

*************************************************************************************

##update()	Update the set with another set, or any other iterable

set1={45,4,6,97,1,2}
set2={45,4,8,9,3,21,55,69}

set1.update(set2)
print(set1)

output:
{97, 2, 1, 4, 3, 6, 69, 8, 9, 45, 21, 55}


***************************************************************************************'''

































