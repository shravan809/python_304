'''
#1. How would you confirm that 2 strings have the same identity?


fruits=['banana','apple']
flowers=fruits

print(fruits==flowers)
print(fruits is flowers)

fruits1=['banana','apple']

print()
print(fruits1==flowers)
print(fruits1 is flowers)

print(id(fruits))
print(id(fruits1))
print(id(flowers))

output:
True
True

True
False
2158822960256
2158822959488
2158822960256

*********************************************************************************

#2. How would you check if each word in a string begins with a capital letter?


st = 'We are good boys'
st2='We Are Good Boys'
print(st.istitle())
print(st2.istitle())

output:

False
True
******************************************************************************

#3. Check if a string contains a specific substring

print( 'banana' in 'he is eating banana' )
print( 'apple' in 'he is eating banana' )

output:
True
False

*********************************************************************

#4. Find the index of the first occurrence of a substring in a string

print('we are learing python'.find('python'))

print('we are learing python'.find('java'))

print('we are learing python'.find('are'))

output:
15
-1
3

**************************************************************************

#5. Count the total number of characters in a string

st = 'welcome to OJAS Family'

print('length of the string is:',len(st))

output:
length of the string is: 22

**************************************************************************

#6. Count the number of a specific character in a string

st = 'hi...! '

print('count of '.' is:',st.count('.'))

output:
count of '.' is: 3

***********************************************************************

#7. Capitalize the first character of a string.

st='shravan kumar dasari'

print(st.capitalize())

output:
Shravan kumar dasari

*************************************************************************

#8. What is an f-string and how do you use it?

#ANS: Using f-strings is similar to using format().

#F-strings are denoted by an f before the opening quote.

course='Python'

print(f'I like to learn {course} and I love {course}.')

output:
I like to learn Python and I love Python.

******************************************************************

#9. Search a specific part of a string for a substring

st='shravan can like apple and orange'

print('can found at:',st.index('can'))

print('apple found at:',st.index('apple'))

output:
can found at: 8
apple found at: 17

********************************************************************

#10. Interpolate a variable into a string using format()

name = 'shravan'
place = 'hderabad'

print('A {} visit all places in {}.!'.format(name,place))

output:
A shravan visit all places in hderabad.!

******************************************************************

#11.Check if a string contains only numbers

n = '50000'
n2= 'shravan'

print(n.isnumeric())
print(n2.isnumeric())

output:

True
False

**********************************************************************

#12.Split a string on a specific character

st= 'ravi going to collage...!'
st1 = 'sita-learns-music...!'

print(st.split(' '))
print(st1.split('-'))

output:
['ravi', 'going', 'to', 'collage...!']
['sita', 'learns', 'music...!']

***********************************************************************

#13.Check if a string is composed of all lower case characters

st = 'She went On Holiday Today'
st1 = 'she went on holiday today'

print(st.islower())
print(st1.islower())

output:
False
True

***********************************************************************

#14.Check if the first character in a string is lowercase

print('hYDERABAD'[0].islower())
print('HyDErabad'[0].islower())

output:
True
False

***********************************************************************

#15. Can an integer be added to a string in Python?

#ANS: No. It throws an Type erorr

print('twenty'+20)

output:

 print('twenty'+20)
TypeError: can only concatenate str (not "int") to str

***********************************************************************

#16. Reverse the string “hello world”

print(''.join(reversed('hello world')))

print(','.join(reversed('hello world')))

output:

dlrow olleh
d,l,r,o,w, ,o,l,l,e,h

******************************************************************************

#17. Join a list of strings into a single string, delimited by hyphens

print('_'.join(['python','Java','C']))

output:
python_Java_C

**************************************************************************
#18. Check if all characters in a string conform to ASCI

print('A'.isascii())

print('~'.isascii())

output:

True
True
***********************************************************************

#19. Uppercase or lowercase an entire string

st = 'There's an important presentation starting noon'

print(st.upper())
print(st.lower())

output:

THERE'S AN IMPORTANT PRESENTATION STARTING NOON
there's an important presentation starting noon

**************************************************************************

#20. Uppercase first and last character of a string

st = 'dheli'

print(st[0].upper()+st[1:4].lower()+st[-1].upper())

output:
DhelI
******************************************************************************

#21. Check if a string is all uppercase

name = 'Shravan kumar'
surname= 'DASARI'

print(name.isupper())
print(surname.isupper())

output:

False
True

***************************************************************************

#22.When would you use splitlines()?

st = 'The shop closes at midnight\n I have a meeting at 9am.\n Do you work on Mondays?'

print(st.splitlines())

output:
['The shop closes at midnight', ' I have a meeting at 9am.', ' Do you work on Mondays?']

****************************************************************************

#23. Give an example of string slicing


st = 'I went to London last June.'

print(st[:5])
print(st[:10])
print(st[5:10])
print(st[5:15:2])

output:
I wen
I went to 
t to 
tt od

**************************************************************************

#24.Convert an integer to a string

num =4656

st = str(num)

print(type(num))
print(type(st))
print(st)

output:
<class 'int'>
<class 'str'>
4656

**************************************************************************

#25. Check if a string contains only characters of the alphabet

st = 'SHRAVAN kumar'

print(st.isalpha())

print('SHRAVAN1234'.isalphanumeric())


output:

False
True

************************************************************************* 

#26. Replace all instances of a substring in a string

st='Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair. Fuzzy Wuzzy wasn’t fuzzy, was he'

print(st.replace('Fuzzy','Wuzzy'))

output:
Wuzzy Wuzzy was a bear. Wuzzy Wuzzy had no hair. Wuzzy Wuzzy wasn’t fuzzy, was he

*************************************************************************************

#27. Return the minimum character in a string

print(min('shravan'))

output:

a

***************************************************************************************

#28. Check if all characters in a string are alphanumeric

print('shravan8099917'.isalnum())
print('shravan.8*'.isalnum())

output:

True
False

***************************************************************************************

#29. Remove whitespace from the left, right or both sides of a string

st='  Betty Botter bought some butter  '

print(st.strip())

print(st.rstrip())

print(st.lstrip())

output:

Betty Botter bought some butter
  Betty Botter bought some butter
Betty Botter bought some butter

*************************************************************************************

#30. Check if a string begins with or ends with a specific character?

city = 'New Dheli'
print(city.startswith('New'))
print(city.endswith('N'))

output:
True
False

*************************************************************************'''



































