
'''
#1.Display square and perfect square root of numbers from 48 to 82. using list Comprehension.

import math

squareroot = [i for i in range(48,83) if (math.sqrt(i) == math.floor(math.sqrt(i)))]
square=[i**2 for i in range(48,83)]

print('The perfect squares numbers from 48 to 82 is =', squareroot)
print('Squares from 48 to 82 is =',square)

##output:
##
The perfect squares numbers from 48 to 82 is = [49, 64, 81]
Squares from 48 to 82 is = [2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364,
3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476,
5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724]


********************************************************************************************

#2.Display square and perfect square root of numbers from 48 to 82. using dictionary
#Comprehension.

import math

squareroot ={math.floor(k**0.5):k for k in range(48,83) if (math.sqrt(k) == math.floor(math.sqrt(k))) }

print(squareroot)


square={k:k**2 for k in range(48,83)}

print(square)

output:
{7: 49, 8: 64, 9: 81}
{48: 2304, 49: 2401, 50: 2500, 51: 2601, 52: 2704, 53: 2809, 54: 2916, 55: 3025, 56: 3136,
 57: 3249, 58: 3364, 59: 3481, 60: 3600, 61: 3721, 62: 3844, 63: 3969, 64: 4096, 65: 4225,
 66: 4356, 67: 4489, 68: 4624, 69: 4761, 70: 4900, 71: 5041, 72: 5184, 73: 5329, 74: 5476,
 75: 5625, 76: 5776, 77: 5929, 78: 6084, 79: 6241, 80: 6400, 81: 6561, 82: 6724}

*******************************************************************************************

#3.if the square of number inside list is divisible by 2 print the num.
#(1st questions answer should be taken as a list)

ls=[2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844,
    3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929,
    6084, 6241, 6400, 6561, 6724]

square=[i**2 for i in range(48,83) if i%2==0]

print(square)

output:
[2304, 2500, 2704, 2916, 3136, 3364, 3600, 3844, 4096, 4356, 4624, 4900, 5184, 5476, 5776, 6084,
 6400, 6724]

*********************************************************************************************'''







