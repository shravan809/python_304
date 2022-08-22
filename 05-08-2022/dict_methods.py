#dict methods:-
'''
#clear():Removes all the elements from the dictionary

dic={1:'Rajesh',2:'shravan',3:'ravi'}

dic.clear()

print('empty:',dic)

output:
empty: {}

************************************************************************************

#copy()	Returns a copy of the dictionary

dic={1:'python',2:'JAva',3:'Ruby'}

dic.copy()

print('copied dict is:',dic)

output:
copied dict is: {1: 'python', 2: 'JAva', 3: 'Ruby'}

*************************************************************************************

#fromkeys():Returns a dictionary with the specified keys and value

num=(1,2)
frameworks=('Django')

dic=dict.fromkeys(num,frameworks)

print(dic)

output:
{1: 'Django', 2: 'Django'}

***************************************************************************************

#get():	Returns the value of the specified key

dic={1:'Python',2:'Java',3:'C++'}

x=dic.get(2)
print(x)

output:
Java

**********************************************************************************

#items():Returns a list containing a tuple for each key value pair

dic={1:'ravi',2:'kavya',3:'Mahi'}

x=dic.items()

print(x)

output:
dict_items([(1, 'ravi'), (2, 'kavya'), (3, 'Mahi')])
***************************************************************************************

#keys():Returns a list containing the dictionary's keys


dic={1:'LUCKY',2:'kavya',3:'Bunny'}

x=dic.keys()
print(x)

output:
dict_keys([1, 2, 3])

*************************************************************************************

#pop():Removes the element with the specified key

dic={1:('honda','kia'),'company':('city','nexa')}

dic.pop('company')

print(dic)

output:

{1: ('honda', 'kia')}

*************************************************************************************

#popitem():Removes the last inserted key-value pair

dic={1:'krian',2:'raju'}

dic.popitem()

print(dic)

output:
{1: 'krian'}

*************************************************************************************

#setdefault():Returns the value of the specified key. If the key does not exist: insert the key,
#with the specified value

dic={1:'sunday',2:'monday'}

x=dic.setdefault(2)

print(x)

output:
monday

******************************************************************************************

#update():Updates the dictionary with the specified key-value pairs

dic={1:'jan',2:'feb',3:'march'}

dic.update({4:'april'})
print(dic)

output:

{1: 'jan', 2: 'feb', 3: 'march', 4: 'april'}

*****************************************************************************************

#values():Returns a list of all the values in the dictionary

dic={1:'good',2:'very good',3:'bad'}

x=dic.values()
print(x)

output:
dict_values(['good', 'very good', 'bad'])

***************************************************************************************

#tuple_methods:-

#count():Returns the number of times a specified value occurs in a tuple

tup=(1223,46,98,852,'qwerty',46,98,46)

x=tup.count(46)
print(x)

output:
3

***************************************************************************************

#index():Searches the tuple for a specified value and returns the position of where
#it was found

tup=(897,465,321,'qwerty','asdfg')

x=tup.index(321)

print(x)

output:
2

****************************************************************************************'''




















