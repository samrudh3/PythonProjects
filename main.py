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