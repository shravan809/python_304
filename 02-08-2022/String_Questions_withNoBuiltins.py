'''
#1.WAP to print middle charector of the string

st= 'shravan'

length=len(st)

middle=length//2

print(st[middle])

output:
a

************************************************************************************

#2.2. WAP to print half reverse of the string 

#Input: KNOWLEDGE
#Output: EGDELKNOW

st = 'KNOWLEDGE'

print('half reverse of the string:',st[:3:-1]+st[0:4])


output:

half reverse of the string: EGDELKNOW

***********************************************************************************

#3. WAP to remove all the vouels from the given string

st='shravan'

st1='aeiouAEIOU'

e_string= ''

for i in st:
    if i not in st1:
        e_string=e_string+i
print('without vouels are:',e_string)

output:
    without vouels are: shrvn

*************************************************************************************

#4. WAP to insert * in front of every vouels in the string.

#Input: BANANA
#Output: B*AN*AN*A

st='BANANA'

for i in st:
    if i == 'A' or i == 'E' or i == 'I' or i =='O' or i == 'U' or i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        print('*'+i,end="")
    else:
        print(i,end="")
output:
B*AN*AN*A

**************************************************************************************

#5. WAP to count number of words in the string.

st = 'python is object oriented language'

count=0

for i in st:
    if i==' ':
        pass
    else:
        count+=1
print(count,'is the words in the given string')

output:
30 is the words in the given string

******************************************************************************************

#6. WAP to remove extra space from the given string

st = 'Python is a very high-level programming language'
st1=''
for i in st:
    if i==' ':
        pass
    else:
        st1=st1+i
print(st1)

output:
Pythonisaveryhigh-levelprogramminglanguage

***********************************************************************************

#7. WAP to insert string in between the given string
#Input: Ojas technologies 
#Output: Ojas innovative technologies

st='Ojas technologies'

print('Ojas {} technologies'.format('innovative'))

output:
Ojas innovative technologies

*********************************************************************************

#8. WAP to find the ascci value of given char

st='A'

print('Ascci value of',st,'is :',ord(st))

output:
Ascci value of A is : 65

********************************************************************************

#9. insert ojas in front of every string


st='Python'

print('ojas'+st)

output:
ojasPython

*********************************************************************************

#10. insert ojas in every extra space in the string

st=input("Enter the string")

st1=""
for i in st:
    if i==' ':
        st1=st1+' ojas '
    else:
        st1=st1+i
     
print(st1)

output:
shravan ojaskumar ojasdasari

******************************************************************************************'''








































































































