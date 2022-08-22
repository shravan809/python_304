'''
#1.Calculate income tax for the given income by adhering to the below rules
#Taxable Income    Rate (in %)
#First $10,000      0
#Next $10,000      10
#The remaining     20
#Expected Output:

#For example, suppose the taxable income is 45000 the income tax payable is

#10000*0% + 10000*10%  + 25000*20% = $6000.


income = int(input('What is your income? '))
if income<=10_000:
    print('You have zero tax')
elif 10_000 < income <= 20_000:
    income_2 = (income - 10_000)*0.1
    print(f"Your tax amount to be paid is ${income_2}")
elif income > 20_000:
    income_3_1 = ((income - 10_000)*0.1)
    income_3_2 = ((income - 20_000)*0.2)
    income_3 = income_3_1 + income_3_2
    print(f"Your tax amount to be paid is ${income_3}")
output:
What is your income? 45000
Your tax amount to be paid is $8500.0

***********************************************************************************

#2.Count the length of list with out using any inbuilt function.

ls = [1,2,5,4,9,13,54]

count=0
for i in ls:
    count=count+1
print('length of the list is:',count)
    
output:
length of the list is: 7

************************************************************************************

#3.Write a Python program to create a histogram from a given list of integers.

ls=[1,2,3,4,5,4,3,2,1]

for n in ls:
    output = ''
    times = n
    while( times > 0 ):
        output += '*'
        times = times - 1
    print(output)

output:

*
**
***
****
*****
****
***
**
*

*******************************************************************************'''
 
#Take input from user and if input is string print String
#if input is integer/float print integer
#if input is mix of string and integer print Error
#HINT Can be done using ASCII code


tp = input('enter the type:')

if type(tp) is str:
    print('string')
elif type(tp) is int:
    print('integer')
else:
    print('Error')






















































