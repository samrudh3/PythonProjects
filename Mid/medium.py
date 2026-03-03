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

# import shutil

# shutil.copy("medium.py", "medium2.py") #Copies the file
# shutil.copy2("medium.py", "medium2.py") #Copies the meta data also (when file was creted etc)
# shutil.copytree("src", "dst") #recursilvely copeis the directory from src to dst
# shutil.move("src", "dst") # Moves the file from src to dst (can we used to rename also)
# shutil.rmtree("path")# Helps to remove the dir(can't delete file)

# import requests
# from bs4 import BeautifulSoup

# url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"

# r = requests.get(url)

# soup = BeautifulSoup(r.text, 'html.parser')
# # print(soup.prettify())

# for heading in soup.find_all("h2"):
#     print(heading.text)
# print(r.text)

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'harry',
#     "body": 'bhai',
#     "userId": 12,
#   }
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response = requests.post(url, headers=headers, json=data)

# print(response.text)