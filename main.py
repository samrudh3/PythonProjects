# print('hello world', 1, 2, sep='-',end='!')

# a = int(input("Enter a number :"))
# b = int(input("Enter another number :"))
# print("the sum of a and b is :", a + b)

# mystr = "Let run the \t for loop\n"

# for c in mystr:
#     print(c)

# fruit = "banana"
# print(fruit[0])
# print(fruit[1])

# print (fruit[0:3])
# print(fruit[0: -2])
# print(fruit[:len(fruit)-2])

#len(str), str.lower(), str.upper()
# mystr = "!!!!! Harry !!!!"
# print(mystr.rstrip('!'))
# print(mystr.lstrip('!'))
# print(mystr.strip('!'))
# print(mystr.replace('!', '@'))
# print(mystr.split(' '))

# mystr = "harry Is a Good boy"
# print(mystr.capitalize()) #Convert first character to upper case and rest to lower case
# print(mystr.count('r'))
# print(mystr.endswith('sh'))
# print(mystr.find('z')) #Returns -1 No Error
# print(mystr.index('z')) #Throws Exception if not Found

# import time

# mytime = time.strftime('%H:%M:%S')
# print(mytime)

# if int(time.strftime('%H')) < 12 :
#     print("Good Morning")
# elif int(time.strftime('%H')) > 12 and int(time.strftime('%H')) > 15:
#     print("Good Afternoon")
# else :
#     print("Good Night")      

# x = 5

# match x:
#     case 0:
#         print("x is",x)
#     case 1:
#         print("x is", x)
#     case _ if(x == 5):
#         print("Ohh it is 5 ") 

# for i in range(5): #Prints 0 to 5
#     print(i)


# for i in range(1,5): #Starts from 1
#     print(i)

# for i in range(1, 11, 2): #Step index 2
#     print(i)

# i = 0 
# while(i < 5):
#     print(i)
#     i = i + 1

# i = 5
# while i > 0 :
#     print(i)
#     i -= 1
# else:
#     print("while loop else")    

# for i  in range(5):
#     if i == 2:
#         continue
#     print(i)
# else:
#     print("for loop else")

#Do while in python
# i = 0
# while True:
#     print(i)
#     i = i + 1
#     if i == 1:
#         break

# def addmyvalues(a,b):
#     print(a+b)

# def subMyValues(a,b):
#     pass # just do nothing 

# addmyvalues(3,4)

# def average(*nums):
#     print(type(nums)) #Takes as tuple
#     sum = 0 
#     for i in nums:
#         sum = sum + i

#     return sum / len(nums)

# c = average(2,3,4)
# print("Avg = ", c)

# def average(**nums):
#     print(type(nums)) #Takes as Dict
#     print(nums['a'], nums['b'], nums['c'])

# average(a = 1, b = 2 , c = 3)
# average(a = 1, b = 2) # Throws Error when we don't pass c 

# marks = [1,2,3,4,True, "harry"]

#Slicing
# print(marks[1:3:2])

# print(marks[-4]) #Equals to len(marks) - 4
# print(marks[2])
# if "harry" in marks:
#     print("Yes")
# else:
#     print("No") 

# lst = [i for i in range(10)]
# print(lst)

# lst1 = [i for i in range(10) if i%2 == 0]
# print(lst1)

# lst2 = [i*i for i in range(5)]
# print(lst2)

# l = [2,1]
# # m = [3,4]
# m = l
# k = l + m
# m.insert(1,5)
# print(k)
# print(m)
# print(l)

# tup = (1,2,3,4,2,4,6,9,3,6,2,5,8,0,4,7,9,4,6,9)
# # print(tup[1:3])

# res = tup.index(3, 4, 11)#Find 3 from start index to end Index
# print(res)

# question = [
#     {"question": "5 + 3", "answer": 8},
#     {"question": "10 - 4", "answer": 6},
#     {"question": "6 × 7", "answer": 42},
#     {"question": "9 ÷ 3", "answer": 3},
#     {"question": "12 + 15", "answer": 27}
# ]

# print("Lets play KBC of 5 Question, Each crt question 10rs")
# amt = 0 
# for q in question:
#     print("Q = ", q["question"])
#     ans = int(input("Enter the ans = "))
#     if ans == q["answer"]:
#         amt = amt + 10
#     else:
#         amt = 0
#         break

# if amt != 0:
#     print("You have won = ", amt)
# else:
#     print("Soory You lost")    

# item = "Pen"
# price = 23.284383982

# print(f"The item is {item} and price is {price}")
# print(f"The item is {item} and price is {price:.2f}")
# print(f"The item is {{item}} and price is {{price}}")

# def squareNum(n):
#     ''' Takes the number n and return the square of n '''
#     return n * n

# print(squareNum(5))
# print(squareNum.__doc__)

# def fibonacci(n):
#     if n == 0:
#         return 0 
#     if n == 1:
#         return 1
    
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(5))

# s = {1,2,3,4,5,2,4}
# print(s)

# s1 = set()
# print(type(s1))

# dict = {"john" : 36, "Ravi":33, "Neha":26, "Sonal":23}
# print(dict["john"]) #Throws Error if not Found 
# print(dict.get("john"))#Returns None if not found 
# print(dict.keys())
# print(dict.values())

# for key in dict.keys():
#     print(dict[key])


# print(dict.items())#Prints key value pairs

# print("1st Prg")
# for i in range(6):
#     print(i)
# else:
#     print("in the else block")    

# print("2nd Prg")
# for i in range(6):
#     print(i)
#     if i == 3:
#         break #Else will not be executed
# else:
#     print("in the else block")      

# l1 = [1,2,3,4]

# try:
#     print(l1[6])
# except:
#     print("Inavalid Index")    

# def myFuc(n):
#     try:
#         print(l1[n])
#         return 1 #Found
#     except Exception as e:
#         print("Inavalid Index", e)  
#         return 0 #Not found  
#     finally:
#         print("I always executes")
# x = myFuc(5)
# print(x)   

# x = int(input("Enter the Number btw 0 and 5 : "))

# if x > 5 or x < 0:
#     raise ValueError("Enter the valid Nummber")

# mystr = input("Enter the message to Encode, separated by Space :")

# l1 = list(mystr.split(" "))

# def encodeMsg(l1):
#     mylist = []
#     for i in l1:
#         if(len(i) >= 3):
#             i = i[1:] + i[0]
#             newstr =  ("xyz" + i + "xyz")
#             mylist.append(newstr)
#         else:
#             newstr = (i[::-1])
#             mylist.append(newstr)
#     print("After encoding = ", mylist)  
#     decodeMsg(mylist) 

# def decodeMsg(newList):
#     dlist = []
#     msg= ""
#     for item in newList:
#         if len(item) >= 6 :
#             if item.startswith("xyz") and item.endswith("xyz"):
#                 item = item[3:-3]
#                 item = item[-1] + item[0:-1]
#                 dlist.append(item)
#         else:
#             newstr = (item[::-1])
#             dlist.append(newstr)

#     for s in dlist:
#         msg = msg + " " + s

#     print("After Decoding the msg = ",msg)    
                
# encodeMsg(l1)

# import random
# import string
# rstr = "".join(random.choices(string.ascii_lowercase, k = 3)) #To Get the random Character
# print(rstr)

# a = 10
# b = 54
# print("A") if a > b else print("=") if a == b else print("B")

# l1 = [2,34,5,25,56,29,46,7,75]
# index = 0
# for item in l1:
#     print(item)
#     if index == 4:
#         print("Heighest Marks!")
#     index += 1   

# for index, item in enumerate(l1):
#     print(item)
#     if index == 4:
#         print("heighest marks")

# import pandas as pd
# print(pd.__version__)

# import math

# print(math.sqrt(9))

# from math import sqrt, pi
# from math import *
# from math import sqrt as s,pi
# import math as m
# print(pi)
# print(dir(m))

# import myModule

# myModule.printMsg()

# l1 = [1,2,34,5,6]
# l2 = []
# for i in l1:
#     if i == 2 or 5:
#         l2.append(i)

# print(l2)      

import os

# if not os.path.exists("DATA"):
#     os.mkdir("DATA")

# for i in range(0,5):
#     os.mkdir(f"DATA/Day {i} Notes")

# for i in range(0,5):
#     os.rename(f"DATA/Day {i} Notes",f"DATA/Day {i + 1}")   

# folders = os.listdir("DATA") 
# # print(folders)
# for folder in folders:
#     print(os.listdir(f"data/{folder}"))
# cmd = 'date'
# print(os.system(cmd))

# print(os.getcwd())
# print(os.chdir(f".."))
# print(os.getcwd())

# x = 5

# def hello():
#     global x
#     x = 2
#     y = 3
#     print(y)

# hello()
# print(x)
# print(y)#Gives Error Bcz we are trying to print local variable

#Reading al File
# f = open("Sample.txt", 'r')
# print(f)# Prints the Object
# text = f.read()
# print(text)
# f.close()

#Writing a file/Append
# f = open('Sample2.txt','w') 
# f.write("Hello Machii!")
# f.close()

# with open('Sample.txt','a') as f:
#     f.write("Long time no see Machi")

# with open('Sample.txt', 'r') as f :
#     mystr = f.readlines()
#     print(mystr)

# f = open("Sample.txt", 'r')
# while True:
#     line = f.readlines()
#     if not line:
#         break
#     print(line)

# f = open("Sample.txt", 'a')
# l1 = [" wegdjhed \n", "dgwdjhjkjd\n", "wwjdhqwjhd\n"]
# f.writelines()
# f.close()

# sqrt = lambda x : x * x
# print(sqrt(5))

# someValue = lambda x, y, z : (x + y+ z)/3
# print(someValue(2,3,4))

# def apply(fx, value ):
#     return fx(value) + value

# print(apply(lambda x: x + x, 2))

# l1 = [1,2,3,4,5]

# #map
# sumValue = list(map(lambda x: x + x, l1))
# print(sumValue)

# filterValue = list(filter(lambda x: x > 2, l1))
# print(filterValue)

# from functools import reduce

# reduceValue = reduce(lambda x,y : x + y, l1)
# print(reduceValue)

# a = 3
# b = "3"
#Any immutabel Data Types like, int(const), String , tuple, None will return True for "is" Python internally will make it single memory location 
#Mutable object like list will returm false in "a is b"
# print ( a is b) #exact location of object in memory
# print ( a == b) #value


# import random

# result_matrix = [
#     [0, -1, 1],   
#     [1, 0, -1],   
#     [-1, 1, 0]    
# ]

# print("Welcome to Rock Paper and Scissor!\n")
# playerValue = int(input("Enter 0:Rock, 1:Paper, 2: Scissor\n"))
# computerValue = int(random.choice([0, 1, 2]))
# print(random.randint(0,2)) 
# print(f"Computer Value {computerValue}")
# res = result_matrix[playerValue][computerValue]

# if res == 1:
#     print("Player Wins")
# elif res == -1:
#     print("Computer Wins")
# else :
#     print("Its a Draw")        
