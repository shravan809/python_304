
'''
##1.Python Program to Return the Length of the Longest Word from the List of Words
##
##Problem Description:
##
##The program takes a list of words and returns the word with the longest length.
##
##Runtime Test Cases:
##
##Case 1:
##Enter the number of elements in list:4
##Enter element1:"Apple"
##Enter element2:"Ball"
##Enter element3:"Cat"
##Enter element4:"Dinosaur"
##The word with the longest length is:
##Dinosaur
## 
##Case 2:
##Enter the number of elements in list:3
##Enter element1:"Bangalore"
##Enter element2:"Mumbai"
##Enter element3:"Delhi"
##The word with the longest length is:
##Bangalore

ls=[]
temp=0
num=int(input('Enter thenumber of elements:'))

for i in range(1,num+1):
    ip=input('enter element{}:'.format(i))
    ls.append(ip)
lst=[]

for i in ls:
    if len(i)>temp:
        temp=len(i)
        lst.append(i)
print(lst[-1])

output:

Enter thenumber of elements:4
enter element1:APple
enter element2:Ball
enter element3:Cat
enter element4:Dinosaur
Dinosaur

#***************************************************************************************'''












































