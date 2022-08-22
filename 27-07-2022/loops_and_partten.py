
'''
#1. Write a program to print the following Patterns
#  1 2 3 4 5 
#  1 2 3 4 5  
#  1 2 3 4 5 
#  1 2 3 4 5 
#  1 2 3 4 5

n= 5

for rows in range(1,n+1):
    for cols in range(1,n+1):
        print(cols,end = ' ')
    print()

output:

1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5

*****************************************************************************

#2.Write a program to print the following Pattern
#  5 4 3 2 1 
#  5 4 3 2 1
#  5 4 3 2 1
#  5 4 3 2 1
#  5 4 3 2 1

n= 5

for rows in range(1,n+1):
    for cols in range(n,0,-1):
        print(cols,end = ' ')
    print()
output:

5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1

******************************************************************************

#3.Write a program to print the following Pattern
#  5 5 5 5 5 
#  4 4 4 4 4 
#  3 3 3 3 3 
#  2 2 2 2 2 
#  1 1 1 1 1

n= 5

for rows in range(n,0,-1):
    for cols in range(n,0,-1):
        print(rows,end = ' ')
    print()

output:

5 5 5 5 5 
4 4 4 4 4 
3 3 3 3 3 
2 2 2 2 2 
1 1 1 1 1

*********************************************************************************

#4.Write a program to print the following Pattern
#  1
#  1 2
#  1 2 3
#  1 2 3 4
#  1 2 3 4 5

n= 5

for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(cols,end = ' ')
    print()

output:

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

******************************************************************************

#5.Write a program to print the following Pattern
#  1 
#  2 2 
#  3 3 3 
#  4 4 4 4 
#  5 5 5 5 5

n= 5

for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(rows,end = ' ')
    print()

output:
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

******************************************************************************

#6.Write a program to print the following Pattern
#  1 
#  2 3  
#  4 5 6 
#  7 8 9 10 
#  11 12 13 14 15


n= 1
rows=5
for i in range(0,rows):
    for cols in range(0,i+1):
        print(n,end = ' ')
        n=n+1
    print()
    
output:    
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 

***************************************************************************************

#7.Write a program to print the following Pattern
#  5 
#  4 4 
#  3 3 3 
#  2 2 2 2 
#  1 1 1 1 1
num=1
n= 5

for rows in range(1,5+1):
    for cols in range(1,rows+1):
        print(n,end = ' ')
    n=n-1
    print()

output:
5 
4 4 
3 3 3 
2 2 2 2 
1 1 1 1 1

********************************************************************************

#8.Write a program to print the following Pattern

#  1 
#  2 3 
#  3 4 5 
#  4 5 6 7 
#  5 6 7 8 9

n = 5

for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(rows,end=' ')
        rows=rows+1
    print()
    
output:
1 
2 3 
3 4 5 
4 5 6 7 
5 6 7 8 9

******************************************************************************

#9.Write a program to print the following Pattern

#  A 
#  B C
#  D E F
#  G H I J
#  K L M N O

ch=65

for rows in range(ch,ch+5):
    for cols in range(65,rows+1):
        print(chr(ch),end=' ')
        ch=ch+1
    print()

output:
A 
B C 
D E F 
G H I J 
K L M N O 

******************************************************************************************

#10.Write a program to print the following Pattern

#   * * * * * 
#   * * * * * 
#   * * * * * 
#   * * * * * 
#   * * * * *

n= 5

for rows in range(1,n+1):
    for cols in range(1,n+1):
        print('*',end = ' ')
    print()

output:
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *

*****************************************************************************************

#11.Write a program to print the following Pattern

#   * 
#   * * 
#   * * * 
#   * * * * 
#   * * * * *

n= 5

for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print('*',end = ' ')
    print()

output:
* 
* * 
* * * 
* * * * 
* * * * * 

*********************************************************************************************

#12.Write a program to print the following Pattern
#    * * * * * 
#    *       * 
#    *       * 
#    *       * 
#    * * * * * 

n=5

for rows in range(0,n):          
  for cols in range(0,n):        
    if (rows==0 or rows==4) or (cols==0 or cols==4):
      print('*',end = ' ')
    else:
      print(' ',end = ' ')
  print()

output:
* * * * * 
*       * 
*       * 
*       * 
* * * * *

*************************************************************************************

#13.Write a program to print the following Pattern
#####      * 
#        * * * 
#      * * * * * 
#    * * * * * * * 


n = 4
for rows in range(n):
    for cols in range(n - rows - 1):
        print(' ', end=' ')
    for k in range(2 * rows +1):
        print(' *', end='')
    print()

    
output:
       *
     * * *
   * * * * *
 * * * * * * *

***************************************************************************

#14.Display Multiplication Table in given range using Nested for loops

n= int(input('Enter the Multiplication Table range :'))
for i in range(1,n+1):
    for j in range(1,10+1):
        print(i,"*",j,"=",i*j)
    print()
    print()

output:
Enter the Multiplication Table range :2
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10


2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20

*******************************************************************************

#15.Display Prime Numbers in the given range using nested for loops 

for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=' ')
output:
    
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

******************************************************************************

#16.Write a program to print the following Pattern
###	1
              3  2
       6   5   4
10  9   8   7       




*************************************************************************


#17.Write a program to print the following Pattern

#10  9  8   7
#      6   5  4
#           3  2
#               1 






***********************************************************************

#Loops:



#1.Accept 10 numbers from the user and display their average. 
sum = 0

for i in range(10):
    n=int(input('Enter the value of n'))
    sum = sum+n
avg=sum/10
print(avg)
    
output:
Enter the value of n45
Enter the value of n12
Enter the value of n45
Enter the value of n65
Enter the value of n24
Enter the value of n12
Enter the value of n89
Enter the value of n78
Enter the value of n45
Enter the value of n54
46.9

*********************************************************************

#2.Write a program to display sum of odd numbers and even numbers that fall between 12 and 37

min = 12
max = 37
even_sum = 0
odd_sum = 0
 
for i in range(min, max + 1):
    if(i%2==0):
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
 
print(even_sum,'is sum of even numbers')
print(odd_sum,'is sum of odd number')
output:
312 is sum of even numbers
325 is sum of odd number

*************************************************************

#3.Write a program to display all the numbers which are divisible by 11 but not by 2
#between 100 and 500. 


min = 100
max = 500
print('numbers divisible by 11 but not by 2 are')
for i in range(min,max):
    if i%11==0 and i%2!=0:
        print(i,end=' ')

output:

numbers divisible by 11 but not by 2 are
121 143 165 187 209 231 253 275 297 319 341 363 385 407 429 451 473 495

***************************************************************************

#4.Write a program to print numbers from 1 to 20 except multiple of 2 & 3 

print('not a multiple of 2 & 3 are:')
for i in range(1,20):
    if i%2!=0 and i%3!=0:
        print(i,end=' ')
output:

not a multiple of 2 & 3 are:
1 5 7 11 13 17 19

****************************************************************************

#5.Write a program that keep on accepting number from the user until user enters Zero.
#Display the sum and average of all the numbers. 

sum = 0
for i in range(10):
    n=int(input('Enter the value of n:'))
    if n==0:
       break
    sum = sum+n
avg=sum/i
print(avg)

output:
Enter the value of n:10
Enter the value of n:10
Enter the value of n:20
Enter the value of n:20
Enter the value of n:0
15.0

*********************************************************************************

#6.Write a program to accept decimal number and display its binary number. 

dec =int(input('Enter the  decimal number:'))
l=[]
r=0
while dec>0:
    r=dec%2
    if (r==1):
        l.append(1)
    if (r!=1):
        l.append(0)
    dec=dec//2
print(l[::-1])

output:

Enter the  decimal number:10
[1, 0, 1, 0]

*********************************************************************

#7.Convert the following loop into for loop : 

#x = 4 

#while(x<=8): 

#   print(x*10) 

#   x+=2 

for x in range(4,8+1,2):
    print(x*10)

output:

40
60
80

********************************************************************

#8.What is nested loop? 

A nested loop is a loop inside the body of the outer loop.
The inner or outer loop can be any type, such as a while loop or for loop.
For example, the outer for loop can contain a while loop and vice versa.

syntax:
    
for element in sequence 
   # inner for loop
   for element in sequence:
       body of inner for loop
   body of outer for loop

*************************************************************************

#9.Write a program to convert temperature in Fahrenheit to Celsius. 

temp=int(input("Enter temperature in Fahrenheit:"))

cel=((temp-32)*5/9)
print("convert temperature in Fahrenheit to Celsius:",cel)

output:
    
Enter temperature in Fahrenheit:100
convert temperature in Fahrenheit to Celsius: 37.77777777777778

*****************************************************************************

#10.Write a Python program to get the Fibonacci series between 0 to 50.

n=10
a=0
b=1
print(a,b,end=' ')

for i in range(2,n):
    c= a+b
    a=b
    b=c
    print(c,end=' ')

output:
0 1 1 2 3 5 8 13 21 34 
    
*****************************************************************************

Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "Fizz Buzz". 

Sample Output : 

fizzbuzz 

1 

2 

fizz 

4 

Buzz              

n= 50

for i in range(1,n+1):
    if i%3==0 and i%5!=0:
        print('fizz')
    elif i%5==0 and i%3!=0:
        print('Buzz')
    elif i%3==0 and i%5==0:
        print('fizzBuzz')
    else:
        print(i)

output:

1
2
fizz
4
Buzz
fizz
7
8
fizz
Buzz
11
fizz
13
14
fizzBuzz
16
17
fizz
19
Buzz
fizz
22
23
fizz
Buzz
26
fizz
28
29
fizzBuzz
31
32
fizz
34
Buzz
fizz
37
38
fizz
Buzz
41
fizz
43
44
fizzBuzz
46
47
fizz
49
Buzz

************************************************************************************

#12.Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 

#Note : Use 'continue' statement. 

#Expected Output : 0 1 2 4 5 


n= 6

for i in range(n+1):
    if i==3 or i==6:
        continue
    else:
        print(i,end = ' ')


output:
0 1 2 4 5 

***********************************************************************************'''
















































