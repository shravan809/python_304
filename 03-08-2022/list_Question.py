'''
#1.Take 10 integer inputs from user and store them in a list and print them on screen.

ls=[]
for i in range(1,11):
    n=int(input('Enter the n value:'))
    ls.append(n)
print(ls)

output:
Enter the n value:5
Enter the n value:8
Enter the n value:4
Enter the n value:9
Enter the n value:7
Enter the n value:6
Enter the n value:1
Enter the n value:2
Enter the n value:45
Enter the n value:78
[5, 8, 4, 9, 7, 6, 1, 2, 45, 78]

**************************************************************************************

#2.Take 10 integer inputs from user and store them in a list. Again ask user to give a number.
#Now, tell user whether that number is present in list or not.
#( Iterate over list using while loop )

i=1
ls=[]
while i<=10:
    n=int(input('Enter the n value'))
    ls.append(n)
    i=i+1
print(ls)

n1=int(input('Enter any number:'))

if n1 in ls:
    print(n1,'is in list')
else:
    print(n1,'is not in list')

output:

Enter the n value5
Enter the n value9
Enter the n value8
Enter the n value7
Enter the n value4
Enter the n value12
Enter the n value45
Enter the n value78
Enter the n value98
Enter the n value63
[5, 9, 8, 7, 4, 12, 45, 78, 98, 63]
Enter any number:63
63 is in list

************************************************************************************

#3.Take 20 integer inputs from user and print the following:
#number of positive numbers
#number of negative numbers
#number of odd numbers
#number of even numbers
#number of 0s.

ls=[]
for i in range(1,21):
    n=int(input('Enter the n value:'))
    ls.append(n)
print(ls)
positive=0
negative=0
even=0
odd=0
zero=0
for i in ls:
    if i>0:
        positive=positive+1
    if i<0:
        negative=negative+1
    if i%2==0:
        even=even+1
    if i%2!=0:
        odd=odd+1
    if i==0:
        zero=zero+1

print(positive,'is a positive')
print(negative,'is a negative')
print(even,'is a even numbers')
print(odd,'is a odd')
print(zero,'is a zeros')

output:

Enter the n value:99
Enter the n value:-89
Enter the n value:-32
Enter the n value:-5
Enter the n value:45
Enter the n value:0
Enter the n value:25
Enter the n value:12
Enter the n value:0
Enter the n value:49
Enter the n value:78
Enter the n value:62
Enter the n value:32
Enter the n value:19
Enter the n value:17
Enter the n value:36
Enter the n value:-47
Enter the n value:-96
Enter the n value:25
Enter the n value:55
[99, -89, -32, -5, 45, 0, 25, 12, 0, 49, 78, 62, 32, 19, 17, 36, -47, -96, 25, 55]
13 is a positive
5 is a negative
9 is a even numbers
11 is a odd
2 is a zeros

****************************************************************************

#4.Take 10 integer inputs from user and store them in a list.
#Now, copy all the elements in another list but in reverse order.

ls=[]
for i in range(1,11):
    n=int(input('Enter the n value:'))
    ls.append(n)
print(ls)

print(ls[::-1])

output:

Enter the n value:12
Enter the n value:45
Enter the n value:78
Enter the n value:98
Enter the n value:65
Enter the n value:32
Enter the n value:15
Enter the n value:95
Enter the n value:46
Enter the n value:79
[12, 45, 78, 98, 65, 32, 15, 95, 46, 79]
[79, 46, 95, 15, 32, 65, 98, 78, 45, 12]

*************************************************************************

#5.Write a program to find the sum of all elements of a list.

ls=list(range(1,15,2))

sum=0
for i in ls:
    sum=sum+i
print(sum,'is the sum of the list')

output:
49 is the sum of the list

********************************************************************

#6.Write a program to find the product of all elements of a list.

ls=list(range(2,20,3))

mul=1
for i in ls:
    mul=mul*i
print(mul,'is the product of the list')

output:
209440 is the product of the list

********************************************************************************

#7.Initialize and print each element in new line of a list inside list.

ls=[[4,5,12,98,45],[78,65,1,23,78]]

for i in ls:
    for j in i:
        print(j)
    print()

output:
4
5
12
98
45

78
65
1
23
78

************************************************************************************

#8.Find largest and smallest elements of a list

ls=[45,98,21,12,100,50,101,14,75]

print(min(ls),'is the smallest element of a list')

print(max(ls),'is the largest element of a list')

output:

12 is the smallest element of a list
101 is the largest element of a list

****************************************************************************************

#9.Write a program to print sum, average of all numbers, smallest and largest element of a list.

ls=[1,45,78,96,56,35,24,74,54]

count=0
sum=0
for i in ls:
    sum=sum+i
    count=count+1
avg=sum/count
print(sum,'is the sum of elements in list')
print(round(avg,2),' is the average of all numbers in list')

print(max(ls),'is the largest element in list')
print(min(ls),'is the smallest element in list')

output:
    
463 is the sum of elements in list
51.44  is the average of all numbers in list
96 is the largest element in list
1 is the smallest element in list

*************************************************************************************

#10.Write a program to check if elements of a list are same or not it read from front or back.
#E.g.-
#2	3	15	15	3	2

ls=[2,3,15,15,3,2]

reverse =ls[::-1]

if ls==reverse:
    print(reverse,'Elements of the list is same')
else:
    print(reverse,'Elements of the list is not same')

#output:

[2, 3, 15, 15, 3, 2] Elements of the list is same

*************************************************************************************

#11.Take a list of 10 elements. Split it into middle and store the elements in two dfferent lists.
E.g.-
#INITIAL list :
#58 24	13	15	63	9	8	81	1   78

#After spliting :
#58	24	13	15	63
#9	8	81	1	78


ls=[58,28,13,15,63,9,8,81,1,78]

length=len(ls)
print('After spiting :')
print(ls[:length//2])
print(ls[length//2:])

output:
After spiting :
[58, 28, 13, 15, 63]
[9, 8, 81, 1, 78]

***************************************************************************************


#12. Ask user to give integer inputs to make a list. Store only even values given and
#print the list.

ls=[]
for i in range(1,6):
    n=int(input('Enter the n value:'))
    ls.append(n)
print('Given list is:',ls)

ls1=[]
for j in ls:
    if j%2==0:
        ls1.append(j)
print('even numbers list:',ls1)

output:
    
Enter the n value:1
Enter the n value:25
Enter the n value:47
Enter the n value:84
Enter the n value:66
Given list is: [1, 25, 47, 84, 66]
even numbers list: [84, 66]

********************************************************************************

'''



































































