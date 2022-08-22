#1.Write a program to get all vowels from given string
'''
st='shravan kumar is Good boy'
st1='aeiouAEIOU'

for i in st:
    if i in st1:
            print(i,end=' ') 

output:

a a u a i o o o

************************************************************************

#2.Write a program to calculate the simple interest

p=int(input('Enter the principal:'))
r=float(input('Enter the Rate of interest:'))
t= int(input('Enter the Time:'))

si=p*r*t/100

print(si)

output:
Enter the principal:1000
Enter the Rate of interest:4.5
Enter the Time:3
135.0

**********************************************************************

#3.Python Program to Find Sum of Series 1 + 1/2 + 1/3 + 1/4 + ……. + 1/N

n=int(input('Enter the n value:'))
sum=0
for i in range(1,n+1):
    sum =  1+(1/i)    

print(sum)

output:
Enter the n value:5
1.2

**************************************************************************

#4.Python Program to Find the Sum of the Series 1/1!+1/2!+1/3!+…1/N!

import math
n = int(input('Enter the n value:'))
sum=1

for i in range(1+n+1):
    
    sum=sum+(1/math.factorial(i))
print(sum)

output:
Enter the n value:5
3.7180555555555554

**************************************************************************

#5.Python Program to Replace All Occurrences of ‘a’ with $ in a String

st = 'shravan kumar..! welcome to OJAS'

st1 =''

for i in range(0,len(st)):
    if st[i] == 'a':
        st1 = st1+'$'
    else:
        st1=st1+st[i]
print(st1)

output:
shr$v$n kum$r..! welcome to OJAS

*********************************************************************




*****************problem statement***********************************

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]                                


num=[2,7,11,15]

target=9

for i in range(len(num)-1):
    for j in range(i,len(num)):
        if target==num[i]+num[j]:
            print('index:',i,j)

output:

index: 0 1

*******************************************************************************'''


















































