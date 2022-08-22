'''
1.Write a program to find sum of numbers.

n= 687

sum = 0
while n!=0:
  sum = sum +int(n%10)
  n=int(n/10)
print(sum)

output:
21

******************************************************************'''
'''

2.WAP to find the number is strong number or not

my_sum=0
my_num = 145
print("The number is")
print(my_num)
temp = my_num
while(my_num):
    i=1
    fact=1
    remainder = my_num%10
    while(i<=remainder):
        fact=fact*i
        i=i+1
    my_sum = my_sum+fact
    my_num=my_num//10
if(my_sum == temp):
    print("The number is a strong number")
else:
    print("The number is not a strong number")

output:
The number is
145
The number is a strong number

*******************************************************************'''

'''

3.Python Program to Find the Square Root

num = int(input('Enter a number: '))

num_sqrt = num ** 0.5
print('The square root of', num, 'is', num_sqrt)

output:
Enter a number: 25
The square root of 25.000 is 5.0

******************************************************************'''
'''

4.Python Program to Calculate the Area of a Triangle

a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))


s = (a + b + c) / 2


area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
area_of_triangle = round(area,2)
print('The area of the triangle is ',area_of_triangle)

output:
Enter first side: 5
Enter second side: 4
Enter third side: 8
The area of the triangle is 8.18

******************************************************************'''
'''

5.Python Program to Solve Quadratic Equation

a=1
b=6
c=10
d=(b**2)-(4*a*c)
equation1=(-b-(d)**0.5)/2*a
equation2=(-b+(d)**0.5)/2*a
print('the equations are', equation1, equation2)

output:
The equations are (-3-1j) (-3+1j)

********************************************************************'''

'''

6.Python Program to Swap Two Variables

x = input('Enter value of x: ')
y = input('Enter value of y: ')

temp = x
x = y
y = temp

print('The value of x after swapping: ',x)
print('The value of y after swapping: ',y)

output:

Enter value of x: 20
Enter value of y: 5
The value of x after swapping: 5
The value of y after swapping: 20

*********************************************************************'''

'''
7.Python Program to Convert Kilometres to Miles

kilometer = float(input('Enter the km = '))

con_factor = 0.62137

miles = kilometer*con_factor

print(kilometer,'km of miles =',miles,'miles')

output:
Enter value in kilometers: 3.5
3.50 kilometers is equal to 2.17 miles

*********************************************************************'''

'''
8.Python Program to Check Leap Year

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

**************************************************************'''

'''
9.Python Program to Check Prime Number

num = int(input('enter the value of num = '))

for i in range(2,num):
    if num%i==0:
        print(num, 'is not a prime number')
        break
else:
        print(num, 'is a prime number')
        
output:

enter the value of num = 465
465 is not a prime number

enter the value of num = 157
157 is a prime number

**************************************************************'''

'''
10.Python Program to Find the Factorial of a Number

num = int(input('Enter the value of num = '))

fact = 1

if num<0:
    print("factorial of negetive is doesn't exist")
elif num==0:
    print('factorial of 0 is 1')
else:
    for i in range(1,num+1):
        fact = fact*i
    print('factorial of ', num ,' is ',fact)
        
output:
Enter the value of num = 6
factorial of  6  is  720

******************************************************************'''

'''
11.Python Program to Print the Fibonacci seqnceue

first_number = 0
second_number = 1

number = int(input('Enter the number of series = '))

print(first_number,second_number,end=' ')

for i in range(2,number):
    third_number = first_number+second_number
    first_number = second_number
    second_number = third_number
    print(third_number,end=',')
   
output:
    
Enter the number of series = 10
0 1 1 2 3 5 8 13 21 34

********************************************************************'''
'''
12.Python Program to Check Armstrong Number

armstorng = int(input('Enter the value= '))

temp = armstorng
sum = 0
while temp>0:
    digit = temp%10
    sum = sum + digit**3
    temp = temp//10
if sum == armstorng:
    print(armstorng,'is a armstrong number')
else:
    print(armstorng,'is not a armstrong number')

output:
Enter the value= 153
153 is a armstrong number

*******************************************************************'''
'''
13.Python Program to Find Armstrong Number in an Interval

print('Armstrong Number in a range of 100 to 50000 are')
for i in range(100,50000+1):
    o = len(str(i))
    sum = 0
    temp = i
    while temp>0:
        rem = temp%10
        sum = sum + rem**o
        temp = temp//10
    if sum == i:
         print(i,end = ',')
        
output:   
Armstrong Number in a range of 100 to 50000 are
153,370,371,407,1634,8208,9474

******************************************************************'''

'''
14.Python Program to Find the Sum of Natural Numbers

num = int(input('Enter the number = '))

if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   
   while(num > 0):  
       sum += num  
       num -= 1  
   print("The sum is",sum)
   
output:
Enter the number = 100
The sum is 5050


******************************************************************'''
'''
15.Python Program to Find the Factors of a Number

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 4

print_factors(num)

output:
The factors of 4 are:
1
2
4


******************************************************************'''

'''
16.Python Program to Convert Decimal to Binary, Octal and Hexadecimal

decimal = 40

binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

print(binary)
print(octal)
print(hexadecimal)

output:
0b101000
0o50
0x28

******************************************************************'''
'''
17.Python Program to Find LCM

def hcf(n1,n2):
  l=[]
  for i in range(1,n1):
    if (n1%i==0) and (n2%i==0): 
      l.append(i)
  print(l[-1])
  
fun(35,30)
fun(17,35)
output:
5
1
*******************************************************************'''
'''
18.Python Program to Find HCF

def lcm(x,y):

  if x>y:
    z=x
  else:
    z=y
  while(True):
    if z%x==0 and z%y==0:
       break
    z=z+1
  return z
print(lcm(12,14))
print(lcm(17,13))

output:
84
221

*******************************************************************'''




