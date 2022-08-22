'''
#1.WAP to reverse a number

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

**********************************************

#2.. WAP to count  the number  occurrence/frequency
#of a  each character in a string

st = input('Enter a string')

count = 0

for i in st:
    count= count+1
    print(count)

output:
Enter a stringhello
1
2
3
4
5

***************************************************

#3.WAP  to check length of two string is equal or not.

str1 = 'shravan'
str2 = 'shravan'

if str1==str2:
    print('strings are same')
else:
    print('strings are not same')

output:
strings are same

****************************************************

#4.Python program to print even numbers up to 100

n = 100

for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=' ')
output:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 

***************************************************************

#5.Write a program in python to find greatest among three integers

num1 = 25
num2 = 14
num3 = 12

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

output:
The largest number is 25

*************************************************************

#problem statement:



n = int(input('enter the n value'))


if n%2==0:
    if n>=2 and n<=5:
       print('not weird')
    elif n>=6 and n<=20:
       print('weird')
    elif n>=20:
       print('not weird')
else:
   print('weird')
        
output:
enter the n value25
weird

**********************************************************'''




























































