'''
1.Print First 10 natural numbers using while loop 

num = 1

while num<=10:
    print(num)
    num=num+1

output:
1
2
3
4
5
6
7
8
9
10

************************************************************************


#2.Calculate the sum of all numbers from 1 to a given number 
num = int(input('Enter the number to sum:'))
sum = 0

for i in range(1,num+1):
    sum = sum+i
print(sum)

output:
Enter the number to sum:10
55

***********************************************************************

3.Write a program to print multiplication table of a given number 

num = int(input('Enter the value of num:'))

for i in range(1,11):
    mul=num*i
    print(num,'x',i,'=',mul)

output:
    
Enter the value of num7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70

*********************************************************************

#4.Display numbers from a list using loop 

ls = [1,5,3,4,7,5,4,8,10]

for i in ls:
    print(i)

output:
1
5
3
4
7
5
4
8
10

******************************************************************

#5.Count the total number of digits in a number 

num = 4546545
count = 0

while num!=0:
    num = num//10
    count=count+1
    
print('digits of number is:', count)

output:
digits of number is: 7    

***************************************************************

#6.Count the total number of digits in a number 

ls = [1,5,4,8,36,5,5,6]

print('reversed list of elements:')

ls1 = len(ls)-1
for i in range(ls1,-1,-1):
    print(ls[i],end=' ')

output:

reversed list of elements:
6 5 5 36 8 4 5 1 

***************************************************************

#7.numbers from -10 to -1 using for loopDisplay 
print('numbers from -10 to -1 are:')
for i in range(-10,-0):
    print(i,end = ' ')

output:
numbers from -10 to -1 are:
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1    

********************************************************************

#8.Use else block to display a message “Done” after successful execution of for loop 

string = 'hi shravan kumar'

for i in string:
    print(i,end = ' ')
else:
    print('done',end = ' ')

output:
h i   s h r a v a n   k u m a r done

**************************************************************

#9.Write a program to display all prime numbers within a range 

num =int(input('Enter the range of prime number:'))

for i in range(2,num+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

output:
Enter the range of prime number:20
2
3
5
7
11
13
17
19

*******************************************************

Enter the units:350
price = 2000#10.Display Fibonacci series up to 10 terms 

num = 10
a = 0
b = 1
print('Fibonacci series up to 10 terms are:')
print(a,b,end=' ')

for i in range(2,num):
    if num>0:
        c= a+b
        a=b
        b=c
    print(c,end= ' ')

output:

Fibonacci series up to 10 terms are:
0 1 1 2 3 5 8 13 21 34

*************************************************************

#11.Find the factorial of a given number 

num = int(input('Enter the n vaule:'))

fact = 1

for i in range(1,num+1):
    fact = fact*i
print('factorial of given number is:',fact)

output:
Enter the n vaule:5
factorial of given number is: 120

************************************************************

#12.Reverse a given integer number 

num = int(input('Enter the n vaule:'))

rev = 0

while num>0:
    rem=num%10
    rev = (rev*10)+rem
    num = num//10

print('after reversed :',rev)

output:
Enter the n vaule:1234
after reversed : 4321

**********************************************************

#13.Find the sum of the series upto n terms

n = int(input('Enter the n vaule:')) 

sum = 0

for i in range(1,n+1):
    sum = sum+i
    print(sum,end=' ')
output:
Enter the n vaule:10
1 3 6 10 15 21 28 36 45 55 

************************************************************

#14.Calculate the cube of all numbers from 1 to a given number 

n = int(input('Enter the n vaule:'))
print('The cube of all numbers from 1 to a given number is:')
cube = 1
for i in range(1,n+1):
    cube = i**3
    print(cube,end = ' ')
output:
Enter the n vaule:10
The cube of all numbers from 1 to a given number is:
1 8 27 64 125 216 343 512 729 1000

******************************************************************

#15.Use a loop to display elements from a given list present at odd index positions 

ls = [1,5,4,8,6,7,4,58,21]
print('odd elements are:')
for i in ls[1::2]:
    print(i,end = ' ')
output:
odd elements are:
5 8 7 58 

***********************************************************

#16.Name the keyword which helps in writing code involves condition.  

ANS:The if keyword is used to start a conditional statemen


**********************************************************

#17.Write the syntax of simple if statement.

if test expression:
    statement(s)


**********************************************************

#18.Is there any limit of statement that can appear under an if block. 

ANS:There is no limit on the number of statements that can appear under the two clauses of an
if statement, but there has to be at least one statement in each block

***************************************************************

#19.Write a program to check whether a person is eligible for voting or not.
#(accept age from user) 

age = int(input('Enter the age of canditate:'))

if age>=18:
  if age<=80:
    print(age,'is age which canditate is eligible for voter_id')
else:
  print(age,'is age which canditate is not eligibe for voter_id')

output:
Enter the age of canditate:45
45 canditate is eligible for voter_id

***************************************************************

#20.Write a program to check whether a number entered by user is even or odd.

n = int(input('Enter the n vaule:'))

if n%2==0:
    print(n,'is even')
else:
    print(n,'is odd')
        
output:
Enter the n vaule:5
5 is odd

***************************************************************

#21.program Write to check whether a number is divisible by 7 or not. 

n = int(input('Enter the n vaule:'))

if n%7==0:
  print(n, 'is divisible by 7')
else:
  print(n, 'is not divisble by 7')

output:

Enter the n vaule:14
14 is divisible by 7

Enter the n vaule:15
15 is not divisble by 7

**************************************************************************

#22.Write a program to display "Hello" if a number entered by user is a
#multiple of five ,otherwise print "Bye"

num = int(input("Enter the number : "))

if num % 5 == 0:
    print("Hello")
else:
    print("Bye")
output:
Enter the number : 10
Hello

***********************************************************************

#23.Write a program to calculate the electricity bill.

units = int(input('Enter the units:'))
mul = 1
if units<=100:
    mul = mul*0
elif units<=200:
    mul = (100*0)+(units-100)*5
elif units>200:
    mul = (100*5)+(units-200)*10
print('price =',mul)

#output:
Enter the units:350
price = 2000

**********************************************************************

#24.Write a program to display the last digit of a number.

num = int(input('enter the num value:'))

last = num%10

print(last)

output:
enter the num value:465465
5

************************************************************************

#25.Write a program to check whether the last digit of a number( entered by user ) is  

#divisible by 3 or not

n = int(input('Enter the value of n:'))

if n%3==0:
    print(n,'is divisible by 3')
else:
    print(n,'is not divisible by 3')
output:
Enter the value of n:10
10 is not divisible by 3

*********************************************************************

#26.Write a program to accept percentage from the user and display the grade according to the following criteria: 

 

       #  Marks                                      Grade 

       #  > 90                                         A 

        # > 80 and <= 90                               B 

       # >= 60 and <= 80                               C 

        # below 60                                     D 



percentage = int(input('enter the percentage :'))

if percentage>90:
    print('Grade A')
elif percentage>80 and percentage<=90:
    print('Grade B')
elif percentage>=60 and percentage<=80:
    print('Grade C')
else:
    print('Grade D')

output:
enter the percentage :85
Grade B

*************************************************************************

#27.Write a program to accept the cost price of a bike and display the road tax to be paid
#according to the following criteria : 

     

      #  Cost price (in Rs)                                       Tax 

      #  > 100000                                                  15 % 

      #   > 50000 and <= 100000                                    10% 

      #   <= 50000                                                  5% 


cost = int(input('Enter the cost of the bike:'))

if cost>100000:
    print('Tax:15%')
elif cost>50000 and cost<=100000:
    print('Tax:10%')
else:
    print('Tax:5%')
    
output:
Enter the cost of the bike:70000
Tax:10%

****************************************************************************

#28.Write a program to check whether an years is leap year or not. 


year = int(input("Enter a year: "))

if (year%400==0) and (year%100!= 0) or (year%4==0):
    print(year,' is a leap year')
else:
    print(year,'is not a leap year')

output:

Enter a year: 1998
1998 is not a leap year

Enter a year: 2000
2000 is a leap year

***********************************************************************

#29.Write a program to accept a number from 1 to 7 and display the name of
#the day like 1 for Sunday , 2 for Monday and so on. 

num = int(input('enter the number from 1 to7:'))

if num<8:
    if num==1:
        print('SUNDAY')
    elif num==2:
        print('MONDAY')
    elif num==3:
        print('TUSEDAY')
    elif num==4:
        print('WEDNESDAY')
    elif num==5:
        print('THURSDAY')
    elif num==6:
        print('FRIDAY')
    else:
        print('SATARDAY')
else:
    print('Invalid number')

output:
enter the number from 1 to7:6
FRIDAY
**************************************************************************


#30.Write a program to accept a number from 1 to 12 and display name of the month and
#days in that month like 1 for January and number of days 31 and so on 

num = int(input('enter the number from 1 to 12:'))

if num<13:
    if num==1:
        print('January and number of days 31')
    if num==2:
        print('February and number of days 28')
    if num==3:
        print('March and number of days 31')
    if num==4:
        print('April and number of days 30')
    if num==5:
        print('May and number of days 31')
    if num==6:
        print('June and number of days 30')
    if num==7:
        print('July and number of days 31')
    if num==8:
        print('Augsut and number of days 31')
    if num==9:
        print('September and number of days 30')
    if num==10:
        print('October and number of days 31')
    if num==11:
        print('november and number of days 30')
    if num==12:
        print('December and number of days 31')
else:
    print('Invaid number')
        
output:
enter the number from 1 to 12:1
January and number of days 31

**************************************************************************

#31.What do you mean by statement? 

ANS:A statement is an instruction that a Python interpreter can execute

**************************************************************************

#32.Write the logical expression for the following: 
#A is greater than B and C is greater than D


In logical expressions, A is greater than B can be written as 
A is less than C can be written as 
The operator for OR is 
Hence, the logical expression for A is greater than B or A is less than C  

**************************************************************************


#33.Accept any city from the user and display monument of that city. 

               #   City                                 Monument 

               #    Delhi                               Red Fort 

               #   Agra                                Taj Mahal 

               #   Jaipur                              Jal Mahal 



city = input('Enter the city:')

if city=='delhi':
    print('Red Fort')
elif city=='agra':
    print('Taj Mahal')
elif city=='jaipur':
    print('JalMahal')

output:
Enter the city:delhi
Red Fort

***************************************************************************

#34.Write the output of the following if a = 9 

         

   # if (a > 5 and a <=10):     

    #     print("Hello")     

     #      else:     

      #  print("Bye") 


output:
    Hello

***********************************************************************

#35.Write a program to check whether a number entered is three digit number or not


num=int(input("Enter your number:"))

if(num < 1000 and num > 99):
    print(num,'is a three digit number')
else:
    print(num,'is not a three digit number')

output:
Enter your number:454
454 is a three digit number
*****************************************************************************

#36.Write a program to check whether a person is eligible for voting or not.(voting age >=18) 

age = int(input('Enter the age:'))

if age>=18:
    print(age,'person is eligible for voting')
else:
    print(age,'person is not eligible for voting')


output:
Enter the age:14
14 person is not eligible for voting

*******************************************************************************

#37.Write a program to check whether a person is senior citizen or not. 


age = int(input('Enter the age:'))

if age>=60:
    print(age,'person is senior citizen')
else:
    print(age,'person is not senior citizen')

output:
Enter the age:65
65 person is senior citizen

*********************************************************************************

#38.Write a program to find the lowest number out of two numbers excepted from user. 

num1 = int(input('Enter the number:'))
num2 = int(input('Enter the number:'))

if num1<num2:
    print(num1,'is lowest number')
else:
    print(num2,'is lowest number')

output:
Enter the number:11
Enter the number:10
10 is lowest number

***********************************************************************************

#39.Write a program to find the largest number out of two numbers excepted from user

num1 = int(input('Enter the number:'))
num2 = int(input('Enter the number:'))

if num1>num2:
    print(num1,'is largest number')
else:
    print(num2,'is largest number')

output:
Enter the number:54
Enter the number:87
87 is largest number
**********************************************************************************

#40.Write a program to check whether a number (accepted from user) is positive or negative. 


num = int(input('Enter the number:'))

if num>0:
    print(num,'is positive ')
else:
    print(num,'is negative')

output:
    
Enter the number:-5
-5 is negative

*********************************************************************************
#41.Write a program to check whether a number is even or odd. 

num = int(input('Enter the number:'))

if num%2==0:
    print(num,'is even number')
else:
    print(num,'is odd number')

output:
Enter the number:6
6 is even number
*******************************************************************************

#42.Write a program to whether a number (accepted from user) is divisible by 2 and 3 both. 

num = int(input('Enter the number:'))

if num%2==0 and num%3==0:
    print(num,'is divisible by 2 and 3')
else:
    print(num,'is not divisible by 2 and 3')

output:
Enter the number:11
11 is not divisible by 2 and 3

********************************************************************************

#43.Write a program to find the largest number out of three numbers excepted from user. 

num1 = int(input('Enter the number:'))
num2 = int(input('Enter the number:'))
num3 = int(input('Enter the number:'))

if num1>num2 and num1>num3:
    print(num1,'is largest number')
elif num2>num3:
    print(num2,'is largest number')
else:
    print(num3,'is largest number')

output:
Enter the number:45
Enter the number:15
Enter the number:13
45 is largest number

******************************************************************************

#44.Accept the temperature in degree Celsius of water and check whether
#it is boiling or not (boiling point of water in 100 oC. 
temp= int(input('Enter the temperature:'))

if temp>= 100:
    print('Boiling')
else:
    print('not Boiling')

output:
Enter the temperature:95
not Boiling
************************************************************************

#45.the age of 4 people and display the youngest one and oldest one? Accept 

age = int(input('Enter the age:'))

if age<50:
    print(age,'is young person')
else:
    print(age,'is oldest person')

output:
Enter the age:45
45 is young person

********************************************************************

#46.Accept the following from the user and calculate the percentage of class attended: 

#a.     Total number of working days 

#b.     Total number of days for absent 


total = 30

no_of_days_absent=int(input('Enter the no of days absent:'))

percentage = (total-no_of_days_absent)/total*100
                  
print(round(percentage,2),'%')

if percentage>75:
    print('student will  be able to sit in exam')
else:
    print('student will not be able to sit in exam' )

output:
Enter the no of days absent:4
86.67 %
student will  be able to sit in exam

*********************************************************************

#47.Accept three sides of a triangle and check whether it is an equilateral, isosceles or
#scalene triangle. 

#Note : 

#An equilateral triangle is a triangle in which all three sides are equal. 

#A scalene triangle is a triangle that has three unequal sides. 

#An isosceles triangle is a triangle with (at least) two equal sides. 


print('Input lengths of the triangle sides: ')
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

if x == y == z:
	print('Equilateral triangle')
elif x==y or y==z or z==x:
	print('isosceles triangle')
else:
	print('Scalene triangle')

output:

Input lengths of the triangle sides: 
x: 8
y: 8
z: 8
Equilateral triangle


***********************************************************************'''
















