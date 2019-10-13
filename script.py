
# ===== PROBLEM1 =====
# Exercise 1 - Introduction - Say "Hello, World!" With Python
print("Hello, World!")


# Exercise 2 - Introduction - Python If-Else
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    elif n%2 == 0 and n in range(2,6) :
        print("Not Weird")
    elif n%2==0 and n in range(6,21):
        print("Weird")
    elif n%2==0 and (n > 20) :
        print("Not Weird")

# Exercise 3 - Introduction - Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    # c=a+b
    # d=a-b
    # e=a*b

    print(a+b)
    print(a-b)
    print(a*b)
# Exercise 4 - Introduction - Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a//b)
print(a/b)
# Exercise 5 - Introduction - Loops
if __name__ == '__main__':
    n = int(input())

for i in range(0,n) :
    print(i**2)
# Exercise 6 - Introduction - Write a function
def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 4 == 0 and year % 100 !=0):
        return True 
    if (year % 400 == 0 and year % 100 == 0):
        return True
    else:
        return leap
# Exercise 7 - Introduction - Print Function
if __name__ == '__main__':
    n = int(input())
    a=[]
    x=range(1,n+1)
    for i in x:
        print(i , end='')
# Exercise 8 - Basic data types - List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,k]
    for i in range(0,x+1)
    for j in range(0,y+1)
    for k in range(0,z+1) 
    if i+j+k != n])
# Exercise 9 - Basic data types - Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()) #as int iterate through inputs split them and put in list

    #put the input list of array in a set
    x=set(arr)
    #create list and put the objects in set
    y=list(x)
    y.sort()
    #print the second larg number
    print(y[-2])

# Exercise 10 - Basic data types - Nested Lists
# #take input name+grade in small list and all in bigger list
# #print the student have the 2nd lowest mark
#online help 
marksheet=[]
scorelist=[]
if __name__ == '__main__':
        for _ in range(int(input())):
                name = input()
                score = float(input())
                marksheet=marksheet+[[name,score]]
                scorelist=scorelist+[score]
        b=sorted(list(set(scorelist)))[1] 

        for a,c in sorted(marksheet):
             if c==b:
                    print(a)

# #take input name+grade in small list and all in bigger list
# #print the student have the 2nd lowest mark
#online help 
marksheet=[]
scorelist=[]
if __name__ == '__main__':
        for _ in range(int(input())):
                name = input()
                score = float(input())
                marksheet=marksheet+[[name,score]]
                scorelist=scorelist+[score]
        b=sorted(list(set(scorelist)))[1] 

        for a,c in sorted(marksheet):
             if c==b:
                    print(a)
# Exercise 11 - Basic data types - Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    the_score=student_marks[query_name]
    average =sum(the_score)/len(the_score)
    print('%3.2f' %(average) )
#Floating point numbers use the format %5.2f. 
# Here, 5 would be the minimum number of characters the string should contain

# Exercise 12 - Basic data types - Lists
arr=[]
if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        command=input().split()
        
        if (command[0] == "insert"):
            arr.insert(int(command[1]), int(command[2]))
        elif (command[0] == "print"):
            print(arr)
        elif (command[0] == "remove"):
            arr.remove(int(command[1]))
        elif (command[0]=="append"):
            arr.append(int(command[1]))
        elif (command[0] == "sort"):
            arr.sort()
        elif (command[0] == "pop" and (len(arr)!=0)):
            arr.pop()
        elif (command[0] == "reverse"):
            arr.reverse()
            # print(arr)
# Exercise 13 - Basic data types - Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))
# Exercise 14 - Strings - sWAP cASE
def swap_case(s):
    x=''
    for i in s:
        if i.isupper():
            x=x+i.lower()
        elif i.islower():
            x=x+i.upper()
        else:
            x=x+i
    return x
# Exercise 15 - Strings - String Split and Join
def split_and_join(line):
    line=line.split(" ")
    line= "-".join(line)
    return line
# Exercise 16 - Strings - What's Your Name?
def print_full_name(a, b):
    print("Hello"+" "+a+" "+b+"!"+" "+"You just delved into python.")
# Exercise 17 - Strings - Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]

    return string
    # string = string[:5] + "k" + string[6:]

# Exercise 18 - Strings - Find a string
def count_substring(string, sub_string):
    c=0

    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            c=c+1
    return c
#take string as input
#find length
#find sub string
#find sub string length
#find its lenngth

# Exercise 19 - Strings - String Validators
 # correct output but faild in test cases :
if __name__ == '__main__':
    s = input()
    for i in s:

        if s.isalnum():
            print("True") 
            break
    for i in s:
       
        if i.isalpha():
            print("True")
            break
            
      
    for i in s:
        if i.isdigit():
            print("True")
            break
      
    for i in s:
        if i.islower():
            print("True")
            break
            
     
    for i in s:
        if i.isupper: 
            print("True")
            break
#with Online help the test were corect :
if __name__ == '__main__':
    s = input()
    i=''
    if any(i.isalnum() 
    for i in s)==True:
          print(True)
    else:
            print(False)
    if any(i.isalpha() for i in s)==True :
         print(True)
    else:
            print(False)        
    if any(i.isdigit() for i in s)==True :
          print(True)
    else:
            print(False)
    if any(i.islower() for i in s)==True:
          print(True)
    else:
            print(False)
    if any(i.isupper() for i in s)==True:
          print(True)
    else:
            print(False) 
# Exercise 20 - Strings - Text Alignment
#Replace all ______ with rjust, ljust or center. 
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Exercise 21 - Strings - Text Wrap
def wrap(string, max_width):
    return textwrap.fill(string,max_width)

# Exercise 22 - Strings - Designer Door Mat
#with Online help
# Enter your code here. Read input from STDIN. Print output to STDOUT
# str.center(width[, fillchar]) center align the string, using a specified character (space is default) as the fill character

s = input()
lst = s.split();
n = int(lst[0])
m = int(lst[1])

s= ['.|.','WELCOME'] 
n1 = (n-1)//2

for i in range(1,2*n1, 2):
    print((s[0]*i).center(m, '-'))

print(s[1].center(m,'-'))

for i in range(((2*n1)-1), 0,-2):
    print((s[0]*i).center(m, '-'))

# Exercise 23 - Strings - String Formatting
def print_formatted(number):
    # your code goes here
    width = len(bin(n))-2 #bin func 
    for i in range(1, n+1):
        octt=oct(i)
        hexx=hex(i)[2:].upper()
        binn=bin(i)
        print(str(i).rjust(width),octt[2:].rjust(width),hexx.rjust(width),binn[2:].rjust(width)
        
        )

##############Exercise 24 - Strings - Alphabet Rangoli

# Exercise 25 - Strings - Capitalize!
# Complete the solve function below.
def solve(s):
    x=list(s.split(" "))
    y=''
    for i in range(len(x)):
        y=y+x[i].capitalize()+' '
    return y
###############Exercise 26 - Strings - The Minion Game
############### Exercise 27 - Strings - Merge the Tools!

# Exercise 28 - Sets - Introduction to Sets
def average(array):
    # your code goes here
    x=set(array)
    average=sum(x)/len(x)
    return average
# Exercise 29 - Sets - No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m =(int(i) for i in input().split())
l = map(int, input().strip().split(' '))
a = set(map(int, input().strip().split(' ')))
b = set(map(int, input().strip().split(' ')))
result = 0
for i in l:
    if i in a:
        result += 1
    if i in b:
        result += -1
print(result)
# Exercise 30 - Sets - Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())
x1=input().split()
y=int(input())
y1=input().split()

x11=set(list(map(int,x1)))
y11=set(list(map(int,y1)))
dx=x11.difference(y11)
dy=y11.difference(x11)
fin=dx.union(dy)
fin1=sorted(fin)
for i in fin1:
    print (i)
#Exercise 31 - Sets - Set .add()

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=set(input() for i in range(n)) 
print(len(s))
######################## Exercise 32 - Sets - Set .discard(), .remove() & .pop()
########################Exercise 33 - Sets - Set .union() Operation
#########################Exercise 34 - Sets - Set .intersection() Operation
######################### Exercise 35 - Sets - Set .difference() Operation
# Exercise 36 - Sets - Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())
x1=input().split()
y=int(input())
y1=input().split()

x11=set(list(map(int,x1)))
y11=set(list(map(int,y1)))
dx=x11.difference(y11)
dy=y11.difference(x11)
fin=dx.union(dy)
fin1=sorted(fin)
for i in fin1:
    print (i)



# Exercise 37 - Sets - Set Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]

    return string
    # string = string[:5] + "k" + string[6:]



######################### Exercise 38 - Sets - The Captain's Room
##########################Exercise 39 - Sets - Check Subset
####################Exercise 40 - Sets - Check Strict Superset

# Exercise 41 - Collections - collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
#from collections import Counter 
x= int(input())
y =list(map(int,input().split()))
no_cu = 0
for x in range(int(input())):
    s,p=map(int,input().split())
    if s in y:
        no_cu= no_cu+p
        y.pop(y.index(s))
print(no_cu)

# Exercise 42 - Collections - DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n,m=map(int,input().split(" "))
d = defaultdict(list)
a=[]
b=[]
for i in range(1,1+n):
    a=d[input()].append(i)
for i in range(m):
    x=input()
    if d[x]==[]:
        print("-1")
    else:
        print(*d[x]) #* to remove[]
 

#####Exercise 43 - Collections - Collections.namedtuple()
######Exercise 44 - Collections - Collections.OrderedDict()
###### Exercise 45 - Collections - Word Order
#######Exercise 46 - Collections - Collections.deque()
####### Exercise 47 - Collections - Company Logo
####### Exercise 48 - Collections - Piling Up!



# Exercise 49 - Date time - Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
m ,d,y =(int(x) for x in input().split())
print((calendar.day_name[calendar.weekday(y,m,d)].upper()))
       

######## Exercise 50 - Date time - Time Delta

# Exercise 51 - Exceptions -
# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
for i in range(n):
    [a,b]=input().split()
    try:
        a=int(a)
        b=int(b)
        #
        print(a//b)
    except ValueError as v :
        print("Error Code:",v)
    except Exception as e:
        print("Error Code:",e)
#1 value err means when function gets argument with the wrong value
#2 base class for all exceptions


########Exercise 52 - Built-ins - Zipped!
######## Exercise 53 - Built-ins - Athlete Sort

########Exercise 54 - Built-ins - Ginorts
# Exercise 55 - Map and lambda function
cube = lambda x: x**3 # complete the lambda function 

#fn=fn-1+fn-2
def fibonacci(n):
    x=[0,1]
    for i in range (n):
        x.append(x[-1]+x[-2])
    return (x[:-2])
    # return a list of fibonacci numbers
    


#Exercise 56 - Regex - Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT


import re
#t=int(input())
#with online help used direct input instead of assign it to t
for i in range(int(input())):
    print(bool(re.match("^[+-]?[0-9]*\.[0-9]+$",input())))


######### Exercise 57 - Regex - Re.split()
######### Exercise 58 - Regex - Group(), Groups() & Groupdict()
######### Exercise 59 - Regex - Re.findall() & Re.finditer()
######### Exercise 60 - Regex - Re.start() & Re.end()
######### Exercise 61 - Regex - Regex Substitution
######### Exercise 62 - Regex - Validating Roman Numerals
######### Exercise 63 - Regex - Validating phone numbers
#########Exercise 64 - Regex - Validating and Parsing Email Addresses
######### Exercise 65 - Regex - Hex Color Code
######### Exercise 66 - Regex - HTML Parser - Part 1
######### Exercise 67 - Regex - HTML Parser - Part 2
######### Exercise 68 - Regex - Detect HTML Tags, Attributes and Attribute Values
######### Exercise 69 - Regex - Validating UID
######### Exercise 70 - Regex - Validating Credit Card Numbers
######### Exercise 71 - Regex - Validating Postal Codes
######### Exercise 72 - Regex - Matrix Script
######### Exercise 73 - Xml - XML 1 - Find the Score
######### Exercise 74 - Xml - XML 2 - Find the Maximum Depth
######### Exercise 75 - Closures and decorators - Standardize Mobile Number Using Decorators
######### Exercise 76 - Closures and decorators - Decorators 2 - Name Directory


# Exercise 77 - Numpy - Arrays
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    x=numpy.array(arr[::-1], float)
    return x

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# Exercise 78 - Numpy - Shape and Reshape
import numpy as np

x1=np.array(list (map(int, input().split())
))

x1.shape=(3,3)
print(x1)
# Exercise 79 - Numpy - Transpose and Flatten
import numpy as np

np.transpose
n,m =map(int,input().split())
#m=map(int,input().split())
arr=[]
for i in range(n):
    row=list(map(int,input().split()))
    arr.append(row)
ar=np.array(arr)
print(np.transpose(ar))
print(ar.flatten()) #1d

# Exercise 80 - Numpy - Concatenate
import numpy as np 
#order
n,m,p=list(map(int ,input().split(" ")))
arr1=[]
arr2=[]
for i in range(n):
    arr1.append(list(map(int, input().split(" "))))

for i in range(m):
    arr2.append(list(map(int,input().split(" "))))
arr1=np.array(arr1)
arr2=np.array(arr2)
print(np.concatenate((arr1,arr2)))

# Exercise 81 - Numpy - Zeros and Ones
import numpy as np

x=list(map(int,input().split(" ")))

# for i in range(x):
print(np.zeros(x,dtype=np.int))
# for i in range(x):
print(np.ones(x,dtype=np.int))
# np.zeros()
# np.ones()

# Exercise 82 - Numpy - Eye and Identity
import numpy as np 
n,m=list(map(int,input().split(" “)))
#online help for space
np.set_printoptions(sign=' ')
#print(np.identity(n))
print(np.eye(n,m,k=0))

# Exercise 83 - Numpy - Array Mathematics
#correct code but faild at one test 
import numpy as np
n,m=list(map(int, input().split(" ")))
# a=np.array(int,[input().split()])
# b=np.array(int,[input().split()])
a = np.array([input().split()],int) 
b = np.array([input().split()],int)
print(np.add(a,b)) 
print(np.subtract(a,b)) 
print(np.multiply(a,b)) 
print(a//b) 
print(np.mod(a,b))
print(np.power(a,b))

# Exercise 84 - Numpy - Floor, Ceil and Rint
import numpy as np 
#floor same without after.
#ceil above the number
#rint rounds
a=list(map(float,input().split()))
arr1=np.floor(a)
arr2=np.ceil(a)
arr3=np.rint(a)
#online help for space
np.set_printoptions(sign=' ')
print(arr1)
print(arr2)
print(arr3)

######### Exercise 85 - Numpy - Sum and Prod
######### Exercise 86 - Numpy - Min and Max
######### Exercise 87 - Numpy - Mean, Var, and Std
######### Exercise 88 - Numpy - Dot and Cross
######### Exercise 89 - Numpy - Inner and Outer
######### Exercise 90 - Numpy - Polynomials
######### Exercise 91 - Numpy - Linear Algebra
​
# ===== PROBLEM2 =====
​
# Exercise 92 - Challenges - Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    #ar=int(input())
    tall=max(ar) #find max number
    winner= ar.count(tall) #count how many max numbers in 
    return winner

        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

######### Exercise 93 - Challenges - Kangaroo
# Exercise 94 - Challenges - Viral Advertising
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shares=5
    likes=0
    
    for i in range(1,n+1):
        likes=likes + (shares // 2) #share always to 5 and half liked it
        shares=shares// 2 * 3 #the half of the shared list shared it with other *3
    return likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

######### Exercise 95 - Challenges - Recursive Digit Sum
######### Exercise 96 - Challenges - Insertion Sort - Part 1
######### Exercise 97 - Challenges - Insertion Sort - Part 2
