'''
#1.WAP to find the senior citizens in the given list,list values should take dynamicaly (or) from the user only.
# suppose list=[23,67,45,89,65,12,15,19], and output:[65,67,89] final list should be in accending order.
# person age is 60 (or) more than 60 belongs to senior citizens.?


ls=[]
for i in range(1,7):
    age=int(input('enter the age'))
    ls.append(age)
print(ls)

ls1=[]
for i in ls:
    if i>60:
        ls1.append(i)
print(ls1.sort())
print(ls1)

output:
[75, 88, 98]

**************************************************************************************

#2. WAP to find the diagonal matrix absolute difference?
# suppose  1   2  3
#          7   9  3
#         12   5  67
#result:=>53

ls =[[1,2,3],
     [7,9,3],
     [12,5,67]]
n=3
d1=0
d2=0
for i in range(3):
    for j in range(3):
        if i==j:
            d1=d1+ls[i][j]
        if i==n-j-1:
            d2=d2+ls[i][j]
            
print(abs(d1-d2))

output:
53

*****************************************************************************************

#3. WAP to solve this pattern
     A
     A B
     A B C
     A B C D
     A B C D E
     A B C D
     A B C
     A B
     A 
                         


for i in range (65,70):
    for j in range(65,i+1):
        print(chr(j),end=' ')
    print()

for i in range (70,65,-1):
    for j in range(65,i-1):
        print(chr(j),end=' ')
    print()

output:

A 
A B 
A B C 
A B C D 
A B C D E 
A B C D 
A B C 
A B 
A 

**************************************************************************************'''






































































