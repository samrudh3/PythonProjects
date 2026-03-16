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

# import requests
# import json
# query = input("What type of news are you interested in ? ")

# url = "https://newsapi.org/v2/everything?q={query}&from=2026-02-03&sortBy=publishedAt&apiKey=bdd42baecc624498acebb37b21fbdbaf"
# r = requests.get(url)

# news = json.loads(r.text)
# # print(news, type(news))

# for article in news['articles']:
#     print("Title :", article["title"] )
#     print("Description", article["description"])
#     print("--------------------------------------------------")

# def generator():
#     for i in range(5):
#         yield i

# gen = generator()
# # print(next(gen)) #0
# # print(next(gen)) #1

# for i in gen:
#     print(i)

# from functools import lru_cache
# import time

# @lru_cache(maxsize=None)
# def fx(n):
#     time.sleep(5)
#     return n * n


# print(fx(2))
# print(fx(3))
# print(fx(4))
# print(fx(2))
# print(fx(3))
# print(fx(4))
# print(fx(5))


# import asyncio
# from desktop_notifier import DesktopNotifier

# notifier = DesktopNotifier()

# async def main():
#     while True:
#         await notifier.send(
#             title="💧 Water Reminder",
#             message="Time to drink water!"
#         )
#         await asyncio.sleep(2 * 60 * 60)  # 2 hours

# asyncio.run(main())

# import asyncio

# async def myfunc():
#     await asyncio.sleep(1)
#     return "Hello"

# async def mainfuc():
#     # result =  await myfunc()
#     # print(result)
#     L = await asyncio.gather(
#         myfunc(),
#         myfunc(),
#         myfunc(),
#     )
#     print(L)

# asyncio.run(mainfuc())

# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor

# def func(sec):
#     print(f"Sleeping for {sec}")
#     time.sleep(sec)

# time1 = time.perf_counter()

#Normal Execution 
# func(4)  
# func(3)
# func(2)

#Using Thread 
# t1 = threading.Thread(target=func, args=[4])
# t2 = threading.Thread(target=func, args=[3])
# t3 = threading.Thread(target=func, args=[2])

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# time2 = time.perf_counter()

# print(time2 - time1)
    

# def poolingDemo():
#     with ThreadPoolExecutor() as executor:
#         future1 = executor.submit(func, 3)
#         print(future1.result())
#         future2 = executor.submit(func, 4)
#         print(future2.result())
#         future3 = executor.submit(func, 2)
#         print(future3.result())

# poolingDemo()
