
'''
##You're writing code to control your town's traffic lights.
##You need a function to handle each change from green, to yellow, to red, and then to green again.
##
##
##
##Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.
##
##
##
##For example, when the input is green, output should be yellow.
##
##
##
##Test Case 1
##Input
##Green
##Output
##Yellow
##
##
##
##Test Case 2
##Input
##Red
##Output
##Green

light=input("enter current status of light:")
lst=['green','yellow','red']
for i in lst:
    if i=='red':
        print("The changed light is :",lst[0])
    elif light==i:
        t=lst.index(i)+1
        print("The changed light is :",lst[t])
        break

output:
enter current status of light:green
The changed light is : yellow

enter current status of light:red
The changed light is : green


********************************************************************************************'''






































