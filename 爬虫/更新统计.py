import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import tkinter as tk
import datetime
import time
import random
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
# url = "https://space.bilibili.com/43645887/video"
user_input = input("UID:")
user_input1 = input("UID:")
user_input2 = input("UID:")
Up1 = []
Up2 = []
Up3 = []
def get_main(User_ID,act):
    User_ID = str(User_ID)
    browser = webdriver.Chrome(executable_path='chromedriver.exe')
    browser.get(F"https://space.bilibili.com/{User_ID}/video")
    global a
    a = browser.page_source
    with open("test.txt","a",encoding="utf-8") as fp:
        fp.write(F"{a}")
    fp = BeautifulSoup(a,"lxml")
    global b
    try:
        b = fp.select("div>div>div>div>div>div>div>div>ul>li>.title")[0].string
    except IndexError:
        browser.quit()
        time.sleep(5)
        try:
            b = fp.select("div>div>div>div>div>div>div>div>ul>li>.title")[0].string
        except IndexError:
            time.sleep(5)
            try:
                b = fp.select("div>div>div>div>div>div>div>div>ul>li>.title")[0].string
            except IndexError:
                time.sleep(5)
                b = fp.select("div>div>div>div>div>div>div>div>ul>li>.title")[0].string
    browser.quit()
    if User_ID == user_input:
        Up1.append(b)
        if act == 5:
            if Up1[-1:] != Up1[-1:-2]:
                with open("更新统计.txt","a",encoding="utf-8") as fp:
                    fp.write(F"{User_ID}于 " + str(datetime.datetime.now()) + "更新！" + "\n")
                root = tk.Tk()
                w = tk.Label(root, text=F"UID:{User_ID}更新啦！\n标题：{b}")
                w.pack()
                root.geometry("300x200")
                root.mainloop()
    elif User_ID == user_input1:
        Up2.append(b)
        if act == 5:
            if Up2[-1:] != Up2[-1:-2]:
                with open("更新统计.txt","a",encoding="utf-8") as fp:
                    fp.write(F"{User_ID}于 " + str(datetime.datetime.now()) + "更新！" + "\n")
                root = tk.Tk()
                w = tk.Label(root, text=F"UID:{User_ID}更新啦！\n标题：{b}")
                w.pack()
                root.geometry("300x200")
                root.mainloop()
    elif User_ID == user_input2:
        Up3.append(b)
        if act == 5:
            if Up3[-1:] != Up3[-1:-2]:
                with open("更新统计.txt","a",encoding="utf-8") as fp:
                    fp.write(F"{User_ID}于 " + str(datetime.datetime.now()) + "更新！" + "\n")
                root = tk.Tk()
                w = tk.Label(root, text=F"UID:{User_ID}更新啦！\n标题：{b}")
                w.pack()
                root.geometry("300x200")
                root.mainloop()
    time.sleep(random.uniform(0.5,5))

with open("更新统计.txt","a",encoding="utf-8") as fp:
    fp.write("\n")
    fp.write(str(datetime.datetime.now()) + "\n")
get_main(user_input,3)
get_main(user_input1,3)
get_main(user_input2,3)
while True:
    get_main(user_input,5)
    get_main(user_input1,5)
    get_main(user_input2,5)
