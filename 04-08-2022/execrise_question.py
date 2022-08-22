'''
#1.write a python program to print the pattern
#        * 
#       * * 
#      * * * 
#     * * * * 
#    * * * * * 
#   * * * * * * 
#    * * * * * 
#     * * * * 
#      * * * 
#       * * 
#        *

rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = rows - 2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

output:
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        *     

*****************************************************************************************


#2.How would you check if each word in a string begins with a capital letter?

st=input('enter string:')

print(st.istitle())

output:
enter string:Shravan Kumar
True
enter string:shrvan kumar
False

***********************************************************************************

#3.Write a Python program that prints all the numbers from 0 to 6 except 4 and 5.

for i in range(7):
    if i==4 or i==5:
        pass
    else:
        print(i,end=' ')
output:
0 1 2 3 6

*********************************************************************************

#4.Print list of elements and store in a another list and print  reverse order of list 

ls=[]
for i in range(1,11):
    n=int(input('Enter the n value:'))
    ls.append(n)
print(ls)

print(ls[::-1])

output:
Enter the n value:1
Enter the n value:4
Enter the n value:5
Enter the n value:7
Enter the n value:8
Enter the n value:9
Enter the n value:6
Enter the n value:3
Enter the n value:78
Enter the n value:4
[1, 4, 5, 7, 8, 9, 6, 3, 78, 4]
[4, 78, 3, 6, 9, 8, 7, 5, 4, 1]

**************************************************************************************

#5.write a python program to print the pattern
#            A  
#           B C  
#          D E F  
#         G H I J  
#        K L M N O  
#       P Q R S T U

size = 6
asciiNumber = 65
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        character = chr(asciiNumber)
        print(character, end=' ')
        asciiNumber += 1
    print(" ")

output:

          A  
         B C  
        D E F  
       G H I J  
      K L M N O  
     P Q R S T U 

*********************************************************************************

#problem statement:
#13. Write a Python program to find the strings in a given list, starting with a given prefix.
#Input:
#[( ca,('cat', 'car', 'fear', 'center'))]
#Output:
#['cat', 'car']
#Input:
#[(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
#Output:
#['dog', 'donut']





strs =  ['cat', 'car', 'fear', 'center']
prefix = 'ca'

ls=[]
for s in strs:
  result=s.startswith(prefix)
  if result==True:
    ls.append(s)
print(ls)
        
output:

['cat', 'car']

**********************************************************************************'''





























































