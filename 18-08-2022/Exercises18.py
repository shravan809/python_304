'''

##1.Write a Python program find a list of integers with exactly two occurrences of nineteen and
##at least three occurrences of five. 
##
##Input: 
##
##[19, 19, 15, 5, 3, 5, 5, 2] 
##
##Output: 
##
##True 


ls=[19,15,19,5,2,4,5,6,9,5]

if ls.count(19)==2 and ls.count(5)>=3:
    print(True)
else:
    print(False)

output:

True

********************************************************************************************

##2.WAPP to check a given list of integers where the sum of the integers is equal to length of list. 

ls=[1,1,2,0,1]

length=len(ls)
x=sum(ls)
    
if length==x:
    print('is equal')
else:
    print('is not equal')


output:

is not equal

********************************************************************************************

##3.WAPP to add two integers without using arithmetic operator 

num1=10
num2=15

while(num2!=0):
    carry=num1&num2
    num1=num1^num2
    num2=carry<<1
print(num1)

output:

25


******************************************************************************************'''

































