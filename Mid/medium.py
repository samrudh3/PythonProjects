# import time

# def usingWhile():
#     i = 0 
#     while i < 100:
#         print(i)
#         i = i + 1

# def usingFor():
#     for i in range(100):
#         print(i)

# init = time.time()
# usingWhile()
# end = time.time() - init
# init = time.time()
# usingFor()
# print(f"For Loop {time.time() - init}")
# print(f"While Loop {end}")

# import time

# t = time.localtime()
# formattedTime = time.strftime("%D-%M-%Y %H:%M:%S", t)

# print(formattedTime)

# a = True
# print(a:=False)

# l1 = [1,2,3,4,5]

# while (n := len(l1)) > 0:
#     print(l1.pop())

# foods = list()

# while (food := input("Enter the Food you Like")) != "quit":
#     foods.append(food)

# print(foods)