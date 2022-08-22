'''
#1.what is a variable in and describe the role of variable in python memory management?

x = 20  
y = x   
if id(x) == id(y):   
    print("The variables x and y are referring  to the same object")  

output:
The variables x and y are referring  to the same object

Python removes those objects that are no longer in use or can say that it frees up the
memory space. This process of vanish the unnecessary object's memory space is called the
Garbage Collector. The Python garbage collectorinitiates its execution with the program and
is activated if the reference count falls to zero.

*******************************************************************************

#2.what are the advantages and disadvantages of type casting?
Advantage: More convenient
Disadvantages: More complex type system, source of bugs due to unexpected casts

**********************************************************************************

#3.what is the difference between while loop and for loop?

The major difference between for loop and while loop is that for loop is usedwhen the
number of iterations is known whereas, in the while loop, execution is done until the
statement in the program is proved wrong.

*******************************************************************************

#4.write 5 string method with example?

isalnum()	Checks whether all the characters in a given string is alphanumeric or not
isalpha()	Returns “True” if all characters in the string are alphabets
isdecimal()	Returns true if all characters in a string are decimal
isdigit()	Returns “True” if all characters in the string are digits
isidentifier()	Check whether a string is a valid identifier or not

****************************************************************************************

#5.write the Precedence rule of python with example?
The combination of values, variables, operators, and function calls is termed as an expression.
The Python interpreter can evaluate a valid expression.
example:
print((10 - 4) * 2)

12

****************************************************************************************

#problem statement:

Write a program to check whether the given password is valid or not .

conisder the password to be valid if it contain at least one digit ands one capital.



input:it will be a single line containng string

output: valid password or invalid password



ex:GJ22191gopi

ouput:valid password



password = input("enter the password: ")
number_pass = False
upper_pass = False
for i in password:
    if i.isupper():
        upper_pass = True
    elif i.isnumeric():
        number_pass = True
    if number_pass and upper_pass:
        print("valid password")
        break
else:
    print("not valid password")

output:
enter the password: GJ22191gopi
valid password

enter the password: gopi1996
not valid password

****************************************************************************************'''



































