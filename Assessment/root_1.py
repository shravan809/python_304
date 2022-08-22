
'''
#1.Write a program to swap given two numbers without temporary variable.

a=10
b=20

a,b=b,a

print('swaping given two numbers are:',a,b)

output:

swaping given two numbers are: 20 10

***************************************************************************************

#2.Write a program to accept 4 numbers from command prompt add them using two variables. 

sum=0
for i in range(4):
    n=int(input('Enter the number:'))
    sum=sum+n
print('addition :', sum)

output:
Enter the number:45
Enter the number:65
Enter the number:58
Enter the number:91
addition : 259

****************************************************************************

#3. Write a program which accepts an int values as command line argument and
#print the next multiple of 100.
#    Ex: Input: 35
#    Output: 100
#    Input: 435
#    Output: 500


num =int(input('Enter the num value:'))

for i in range(1000):
    if num%100==0:
        break
    print(100*i)
    
**********************************************************************************    
#5. Write a python program for printing Fibonacci series.   

a=0
b=1

num=int(input('Enter the number for series:'))



if num==1:
    print('Fibonacci series of 1 is',a)
else:
    print('Fibonacci series are:')
    print(a,b,end=' ')
    for i in range(2,num):
        c=a+b
        a=b
        b=c
        print(c,end=' ')

output:
Enter the number for series:10
Fibonacci series are:
0 1 1 2 3 5 8 13 21 34 

***************************************************************************************

#6.Python Program to Find Armstrong Number in an Interval 


num = 100000
sum=0

order = len(num)

for i in range(1,num):
    while i>0:
        rem=i%10
        sum=(sum+rem)**order
        i=i//10
    print(sum)            
    
             
***********************************************************************************
#7. Write a python  program on SumOfDigits, which accepts a two digit number as command line argument and prints the sum of its digits. 
#Ex: Input: 35 
#Output: 8 
#Input: 88 
#Output: 16 


num=int(input('enter the number:'))
sum=0

while num==0:
    rem=num%10
    sum=sum+rem
    num=num//10
print(sum)

****************************************************************************************
#8. Write a python program EvenOrOdd, which accepts a whole number as command
#line argument and prints “Even Number” if the number is Even and prints “Odd Number”
#if the number is Odd. If the input is not a number, print “Error”. 

num=int(input('enter the number:'))

if num%2==0:
    print(num,'is even number')
elif num%2!=0:
    print(num,'is odd number')
else:
    print('Error')
output:
enter the number:546
546 is even number

*********************************************************************************

#12.  Write a python program StarPattern, which accepts a number as command line argument and prints the following output: 
#Input: 4 
#Output: 
#*  
#*  *  
#*  *  *  
#*  *  *  * 

n= int(input('Enter the number of rows:'))

if n>0:
    for rows in range(1,n+1):
        for cols in range(1,rows+1):
            print('*',end=' ')
        print()
else:
    print('Error')

output:
Enter the number of rows:5
* 
* * 
* * * 
* * * * 
* * * * * 


*************************************************************************************

#13. Write a python program NumberPattern4, which accepts a number as command line argument and prints the following output: 
#Input: 5 
#Output: 
#1 
#2 4 
#3 6 9 
#4 8 12 16 
#5 10 15 20 25 

n= int(input('Enter the number of rows:'))

if n>0:
    for rows in range(1,n+1):
        for cols in range(1,rows+1):
            print(rows*2,end=' ')
        n=n+1
        print()
else:
    print('Error')

output:
Enter the number of rows:5
2 
4 4 
6 6 6 
8 8 8 8 
10 10 10 10 10 

    
*****************************************************************************************

#14.Write a python  program on Prime numbers

num=int(input('enter the number:'))

for i in range(2,num):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

output:
enter the number:100
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97

************************************************************************


#16. write a python program on finding a Strong number.

num=int(input('enter the number:'))

temp=num
sum=0

while num:
    i=1
    fact=1
    rem=num%10
    while i<=rem:
        fact=fact*i
        i=i+1
    sum=sum+fact
    num=num//10
if sum==temp:
    print(temp,'is strong number')
else:
    print(temp,'is not a strong number')

output:
enter the number:123
123 is not a strong number

enter the number:145
145 is strong number

************************************************************************

#17.Python Program to Convert Kilometres to Miles


km= float(input('Enter the Kilometres in km:'))


con_factor=0.631

km_to_m = km*con_factor

print(km_to_m)

output:
Enter the Kilometres in km:5.5
3.4705


****************************************************************'''




























