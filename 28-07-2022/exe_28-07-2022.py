
'''

##1.WAP in python arrange string characters such that lowercase letters should come first

st ='Shrvan Kumar Learns PythoN'

sl=''
su=''
for i in st:
    if i.islower()==True:
        sl+=i
    else:
        su+=i
print('The Results are:',sl,su)

output:

The Results are: hrvanumarearnsytho S K L PN

*************************************************************************************

#2.WAP to print sum of prime numbers in given list input :- 2 4 5 6 7 3 8 output :- 17

ls=[2,4,5,6,7,3,8]

sum=0
for i in ls:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum=sum+i
print('sum of prime numbers in given list are:',sum)
            
output:

sum of prime numbers in given list are: 17        

*****************************************************************************************

#3.when do we use nested for loop.Write an example.

ANS: The for loop is used to iterate over a sequence such as a
 list, string, tuple, other iterable objects such as range.

Syntax of using a nested for loop in Python
# outer for loop
for element in sequence 
   # inner for loop
   for element in sequence:
       body of inner for loop
   body of outer for loop

Example:
    
Display Prime Numbers in the given range using nested for loops 

for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=' ')
output:
    
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

*************************************************************************************

#4.WAP in python remove all characters from a string except
#integers(ex:- STR="H56U1E9JIG3l4w2" ,o/p:-5619342(only display integers) )


st = input('Enter the string:')

for i in st:
    if i.isdigit():
        print(i,end='')

output:
Enter the string:shravan46846846545
46846846545

****************************************************************************

#5.WAP to take a list and find the possition of the item .
#(eg=  [45,12,66,2,33] if i take 66 then it shows the index 2)

ls=[12,45,48,75,69,32,4]
ind=int(input('Enter the index point:'))
for i in ls:
    if ind==i:
        print('index point is:',ls.index(i))

output:
Enter the index point:12
index point is: 0

***************************************************************************

problem statement:

Python Program to accept three distinct digits and print all possible combinations from
the digits.

Case 1:

Enter first number:1
Enter second number:2
Enter third number:3
                    1 2 3
                    1 3 2
                    2 1 3
                    2 3 1
                    3 1 2
                    3 2 1

Case 2:

Enter first number:5
Enter second number:7
Enter third number:3
                    5 7 3
                    5 3 7
                    7 5 3
                    7 3 5
                    3 5 7
                    3 7 5      



a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])
  

output:
Enter first number:1
Enter second number:2
Enter third number:3
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

****************************************************************************************'''







































































