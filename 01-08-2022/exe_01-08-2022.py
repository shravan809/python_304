'''

#1. WAP to find the target value of 5 in the given list of 1,5,7,8,90,6,and 23 elements?

ls = [1,5,7,8,90,6,23]

target = int(input('Enter the target value:'))
for i in ls:
    if target==i:
        print("target of {} index is {}".format(target,ls.index(i)))

output:
Enter the target value:5
target of 5 index is 1


*************************************************************************************

#2. WAP to sort the given list of elements 1,5,7,8,90,6,and 23, without using sort() function?


ls = [1,5,7,8,90,6,23]

for i in range(len(ls)-1):
    for j in range(i+1,len(ls)):
        if ls[i]>ls[j]:
            ls[i],ls[j]=ls[j],ls[i]
print('Elements are in the assending order are:')
print(ls)

output:
Elements are in the assending order are:
[1, 5, 6, 7, 8, 23, 90]

****************************************************************************************

#3. WAP to calcalte the compound interest of 3 years with the priciple amount of RS:10000 and rate of return is 5 percentage for annum.
#  and display the total amount to pay on  the end of the year.?

p=int(input("Enter principle amount:"))
t=int(input("Enter time for annum:"))
r=int(input("Enter rate of return:"))
compound_interest=p*(1+r/100)**t
print("result:",compound_interest)

output:
Enter principle amount:10000
Enter time for annum:2
Enter rate of return:3
result: 10609.0


*****************************************************************************************

#4. WAP to calculate the sum of the given matrix   [[x1,x2,x3],[x4,x5,x6],[x7,x8,x9]],
#where x1,x2....x9 values must take from command-line
#   arguments?
### 1 2 3
### 4 5 6  
### 7 8 9   

#sum is : 45   

ls=[]
for i in range(1,10):
    matrix=int(input('Enter the element:'))
    ls.append(i)
sum=0
for i in ls:
    sum=sum+i
print('addition of matrix is:',sum)

output:
Enter the element:1
Enter the element:2
Enter the element:3
Enter the element:4
Enter the element:5
Enter the element:6
Enter the element:7
Enter the element:8
Enter the element:9
addition of matrix is: 45

********************************************************************************************

#5. WAP pattern program

"""  * * * * *
      * * * *
       * * *
        * *
         *
        * *
       * * *
      * * * * 
     * * * * *     """


t=0
p=5
while p>0:
    for row in range(4,-1,-1):
        print(" "*t,end=' ')
        for col in range(row+1):
            print("*",end=' ')
        t=t+1
        p=p-1
        print()
else:
    t=3
    for k in range(2,6):
        print(" "*t,end=' ')
        for m in range(k):
            print('*',end=' ')
        t-=1
        print()

output:
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 

********************************************************************************'''

#problem statement:

'''You are required to enter a word that consists of x and y 
that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if 2 * x = y


Determine if the entered word is similar to word zoo.

For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

Input format

    First line: A word that starts with several Zs and continues by several Os.
    Note: The maximum length of this word must be 20.

    

Output format

Print Yes if the input word can be considered as the string zoo otherwise, print No.

instruction
-----------
if input = zzzoooooo then print "yes".
if input = zzooo print "no". 

while True:
    l=[]
    lt=[]
    x=input("enter  word:")
    if len(x)<20:
        for i in x:
            if 'z'==i:
                l.append(i)
            elif 'o'==i:
                lt.append(i)
        if (len(l)>0) and len(lt)>0:
            if len(l)*2==len(lt):
                print("yes")
            elif len(l)*2!=len(lt):
                print("no")
        else:
            print("no")
    else:
        print("length out of range")


output:
enter  word:zoo
yes
enter  word:zzoo
no
enter  word:zzo
no
enter  word:zzooo
no
enter  word:zzzoooooo
yes
enter  word:


***********************************************************************'''
















































































