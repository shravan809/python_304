'''
#1.Write a program which will find all such numbers which are divisible by 7 but are not a
#multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

ls=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        ls.append(str(i))
print(', '.join(ls))

output:
2002, 2009, 2016, 2023, 2037, 2044, 2051, 2058, 2072, 2079, 2086, 2093, 2107, 2114, 2121, 2128,
2142, 2149, 2156, 2163, 2177, 2184, 2191, 2198, 2212, 2219, 2226, 2233, 2247, 2254, 2261, 2268,
2282, 2289, 2296, 2303, 2317, 2324, 2331, 2338, 2352, 2359, 2366, 2373, 2387, 2394, 2401, 2408,
2422, 2429, 2436, 2443, 2457, 2464, 2471, 2478, 2492, 2499, 2506, 2513, 2527, 2534, 2541, 2548,
2562, 2569, 2576, 2583, 2597, 2604, 2611, 2618, 2632, 2639, 2646, 2653, 2667, 2674, 2681, 2688,
2702, 2709, 2716, 2723, 2737, 2744, 2751, 2758, 2772, 2779, 2786, 2793, 2807, 2814, 2821, 2828,
2842, 2849, 2856, 2863, 2877, 2884, 2891, 2898, 2912, 2919, 2926, 2933, 2947, 2954, 2961, 2968,
2982, 2989, 2996, 3003, 3017, 3024, 3031, 3038, 3052, 3059, 3066, 3073, 3087, 3094, 3101, 3108,
3122, 3129, 3136, 3143, 3157, 3164, 3171, 3178, 3192, 3199


*********************************************************************************************

#2.Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320

num = int(input('Enter the factorial of a number:'))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

output:
Enter the factorial of a number:8
40320

******************************************************************************************

#3.With a given integral number n, write a program to generate a dictionary that contains
#(i, i*i) such that is an integral number between 1 and n (both included). and then the program
#should print the dictionary.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

num=int(input('Enter the number:'))

dic={}
for i in range(1,num+1):
    dic[i]=i*i

print(dic)

output:

Enter the number:8
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

******************************************************************************************

#4.Write a program which accepts a sequence of comma-separated numbers from console and
#generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

num=input('Enter the number:')

list=num.split(',')

tup=tuple(list)
print('list:',list)
print('tuple:',tup)

output:

Enter the number:34,67,55,33,12,98
list: ['34', '67', '55', '33', '12', '98']
tuple: ('34', '67', '55', '33', '12', '98')

*******************************************************************************************

##5.Define a class which has at least two methods:
##getString: to get a string from console input
##printString: to print the string in upper case.
##Also please include simple test function to test the class methods.

class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input('Enter the string:')

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()

output:

Enter the string:ojas innovative
OJAS INNOVATIVE

*****************************************************************************************

#6.Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.
#Example
#Let us assume the following comma separated input sequence is given to the program:
#100,150,180
#The output of the program should be:
#18,22,24

nums=[n for n in input('Enter the value of D:').split(',')]
C=50
H=30
ls=[]
for D in nums:
    ls.append(str(int(round((2 * C * float(D))/H)**0.5)))
print(','.join(ls))

output:
Enter the value of D:100,150,180
18,22,24

******************************************************************************************

##7.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
##The element value in the i-th row and j-th column of the array should be i*j.
##Note: i=0,1.., X-1; j=0,1,¡­Y-1.
##Example
##Suppose the following inputs are given to the program:
##3,5
##Then, the output of the program should be:
##[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 


x=int(input('Enter the rows:'))
y=int(input('Enter the cols:'))

ls=[[0 for col in range(y)]for row in range(x)]

for row in range(x):
    for col in range(y):
        ls[row][col]=row*col
print(ls)

output:
Enter the rows:3
Enter the cols:5
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

*******************************************************************************************

##8.Write a program that accepts a comma separated sequence of words as input and prints the
##words in a comma-separated sequence after sorting them alphabetically.
##Suppose the following input is supplied to the program:
##without,hello,bag,world
##Then, the output should be:
##bag,hello,without,world


word=input('Enter a word')


ls= [ls for ls in word.split(",")]
print(",".join(sorted(list(set(ls)))))

output:
Enter a wordwithout,hello,bag,world
bag,hello,without,world

*******************************************************************************************

##9.Write a program that accepts sequence of lines as input and prints the lines after making
##all characters in the sentence capitalized.
##Suppose the following input is supplied to the program:
##Hello world
##Practice makes perfect
##Then, the output should be:
##HELLO WORLD
##PRACTICE MAKES PERFECT

ls=[]
while True:
    word=input('Enter the words:')
    if word:
        ls.append(word.upper())
    else:
        break
for i in ls:
    print(i)

output:
    
Enter the words:hello world
Enter the words:practice makes perfect
Enter the words:
HELLO WORLD
PRACTICE MAKES PERFECT

*****************************************************************************************

##10.Write a program that accepts a sequence of whitespace separated words as input and prints
##the words after removing all duplicate words and sorting them alphanumerically.
##Suppose the following input is supplied to the program:
##hello world and practice makes perfect and hello world again
##Then, the output should be:
##again and hello makes perfect practice world

st=input('Enter the sequence:')

ls= [ls for ls in st.split(" ")]
print(" ".join(sorted(list(set(ls)))))


output:
Enter the sequence:hello world and practice males perfect and hello world again
again and hello males perfect practice world

******************************************************************************************

##11.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its
##input and then check whether they are divisible by 5 or not. The numbers that are divisible
##by 5 are to be printed in a comma separated sequence.
##Example:
##0100,0011,1010,1001
##Then the output should be:
##1010
##Notes: Assume the data is input by console.

ls=[]
binary=[b for b in input('Enter the binary number 0and1:').split(',')]

for i in binary:
    inp=int(i,2)
    if not inp%5:
        ls.append(i)

print(','.join(ls))

output:

Enter the binary number 0and1:1010,1111,1001
1010,1111

*******************************************************************************************

##12.Write a program, which will find all such numbers between 1000 and 3000 (both included)
##such that each digit of the number is an even number.
##The numbers obtained should be printed in a comma-separated sequence on a single line.

ls=[]
for i in range(1000,3001):
    if i%2==0:
        ls.append(str(i))
print(','.join(ls))

output:
1000,1002,1004,1006,1008,1010,1012,1014,1016,1018,1020,1022,1024,1026,1028,1030,1032,1034,1036,
1038,1040,1042,1044,1046,1048,1050,1052,1054,1056,1058,1060,1062,1064,1066,1068,1070,1072,1074,
1076,1078,1080,1082,1084,1086,1088,1090,1092,1094,1096,1098,1100,1102,1104,1106,1108,1110,1112,
1114,1116,1118,1120,1122,1124,1126,1128,1130,1132,1134,1136,1138,1140,1142,1144,1146,1148,1150,
1152,1154,1156,1158,1160,1162,1164,1166,1168,1170,1172,1174,1176,1178,1180,1182,1184,1186,1188,
1190,1192,1194,1196,1198,1200,1202,1204,1206,1208,1210,1212,1214,1216,1218,1220,1222,1224,1226,
1228,1230,1232,1234,1236,1238,1240,1242,1244,1246,1248,1250,1252,1254,1256,1258,1260,1262,1264,
1266,1268,1270,1272,1274,1276,1278,1280,1282,1284,1286,1288,1290,1292,1294,1296,1298,1300,1302,
1304,1306,1308,1310,1312,1314,1316,1318,1320,1322,1324,1326,1328,1330,1332,1334,1336,1338,1340,
1342,1344,1346,1348,1350,1352,1354,1356,1358,1360,1362,1364,1366,1368,1370,1372,1374,1376,1378,
1380,1382,1384,1386,1388,1390,1392,1394,1396,1398,1400,1402,1404,1406,1408,1410,1412,1414,1416,
1418,1420,1422,1424,1426,1428,1430,1432,1434,1436,1438,1440,1442,1444,1446,1448,1450,1452,1454,
1456,1458,1460,1462,1464,1466,1468,1470,1472,1474,1476,1478,1480,1482,1484,1486,1488,1490,1492,
1494,1496,1498,1500,1502,1504,1506,1508,1510,1512,1514,1516,1518,1520,1522,1524,1526,1528,1530,
1532,1534,1536,1538,1540,1542,1544,1546,1548,1550,1552,1554,1556,1558,1560,1562,1564,1566,1568,
1570,1572,1574,1576,1578,1580,1582,1584,1586,1588,1590,1592,1594,1596,1598,1600,1602,1604,1606,
1608,1610,1612,1614,1616,1618,1620,1622,1624,1626,1628,1630,1632,1634,1636,1638,1640,1642,1644,
1646,1648,1650,1652,1654,1656,1658,1660,1662,1664,1666,1668,1670,1672,1674,1676,1678,1680,1682,
1684,1686,1688,1690,1692,1694,1696,1698,1700,1702,1704,1706,1708,1710,1712,1714,1716,1718,1720,
1722,1724,1726,1728,1730,1732,1734,1736,1738,1740,1742,1744,1746,1748,1750,1752,1754,1756,1758,
1760,1762,1764,1766,1768,1770,1772,1774,1776,1778,1780,1782,1784,1786,1788,1790,1792,1794,1796,
1798,1800,1802,1804,1806,1808,1810,1812,1814,1816,1818,1820,1822,1824,1826,1828,1830,1832,1834,
1836,1838,1840,1842,1844,1846,1848,1850,1852,1854,1856,1858,1860,1862,1864,1866,1868,1870,1872,
1874,1876,1878,1880,1882,1884,1886,1888,1890,1892,1894,1896,1898,1900,1902,1904,1906,1908,1910,
1912,1914,1916,1918,1920,1922,1924,1926,1928,1930,1932,1934,1936,1938,1940,1942,1944,1946,1948,
1950,1952,1954,1956,1958,1960,1962,1964,1966,1968,1970,1972,1974,1976,1978,1980,1982,1984,1986,
1988,1990,1992,1994,1996,1998,2000

*******************************************************************************************

##13.Write a program that accepts a sentence and calculate the number of letters and digits.
##Suppose the following input is supplied to the program:
##hello world! 123
##Then, the output should be:
##LETTERS 10
##DIGITS 3

sen=input('Enter the Sentence:')

count1=0
count2=0
for i in sen:
    x=i.isalpha()
    y=i.isdigit()
    if x==True:
        count1=count1+1
    elif y==True:
        count2=count2+1
print('LETTERS:',count1)
print('DIGITS:',count2)

output:
Enter the Sentence:hello world! 123
LETTERS: 10
DIGITS: 3

********************************************************************************************

##14.Write a program that accepts a sentence and calculate the number of upper case letters and
##lower case letters.
##Suppose the following input is supplied to the program:
##Hello world!
##Then, the output should be:
##UPPER CASE 1
##LOWER CASE 9

sen=input('Enter the Sentence:')

count1=0
count2=0
for i in sen:
    x=i.isupper()
    y=i.islower()
    if x==True:
        count1=count1+1
    elif y==True:
        count2=count2+1
print('UPPER CASE:',count1)
print('LOWER CASE:',count2)

output:
nter the Sentence:Hello world!
UPPER CASE: 1
LOWER CASE: 9

*********************************************************************************************

##15.Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value
##of a.
##Suppose the following input is supplied to the program:
##9
##Then, the output should be:
##11106

num=input('Enter the num value:')

sum=0
for i in range(1,5):
    sum=sum+int(str(num*i))
    print(num*i)
print('**************+\n')
print('sum of n:',sum)

output:
Enter the num value:9
9
99
999
9999
**************+

sum of n:11106

*******************************************************************************************'''





































































































