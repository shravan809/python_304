'''
age = int(input('Enter the age of canditate:'))

if age>=18:
  if age<=80:
    print(age,'canditate is eligible for voter_id')
else:
  print(age,'canditate is not eligibe for voter_id')

output:
Enter the age of canditate:45
45 canditate is eligible for voter_id

*************************************************************'''
'''
telugu = int(input('enter the telugu marks'))
hindi = int(input('enter the hindi marks'))
maths = int(input('enter the maths marks'))
english = int(input('enter the english marks'))
social = int(input('enter the social marks'))

avg = (telugu+hindi+maths+english+social)//5

if 80<=avg<=100:
  print('Student grade is A ')
elif 75<=avg<=80:
  print('Student grade is B')
elif 35<=avg<=75:
  print('Student grade is c')
else:
  print('Student grade is Fail')

output:
enter the telugu marks98
enter the hindi marks98
enter the maths marks98
enter the english marks98
enter the social marks98
Student grade is A

*****************************************************'''
'''
num = int(input('Enter the value of num:'))

if num%2==0:
  print(num,'is even')
else:
  print(num,'is odd')
output:
Enter the value of num:24
24 is even

***************************************************'''
'''
radius = int(input('enter the radius value:'))
pi = 3.14
area = pi*radius**2
print('Area of circle =',area)

output:
enter the radius value:2
Area of circle = 12.56

******************************************************'''
'''
a= int(input('Enter the a value:'))
b= int(input('Enter the b value'))

if a is b:
  print('a and b are same memory loctions')
else:
  print('a and b are not same memory locations')

output:
Enter the a value:10
Enter the b value10
a and b are same memory loctions

*******************************************************'''
'''
#problem statement:
n = 5
sq = 1

for i in range(n):
    sq = (i)**2
    print(sq)
output:

0
1
4
9
16
    
*******************************************************'''




















