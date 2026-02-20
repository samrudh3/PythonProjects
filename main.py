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

x = 5

match x:
    case 0:
        print("x is",x)
    case 1:
        print("x is", x)
    case _ if(x == 5):
        print("Ohh it is 5 ") 