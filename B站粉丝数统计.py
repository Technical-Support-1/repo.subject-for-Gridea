import requests
import ast
import time
import datetime
from selenium import webdriver 
import random

x = []
user_ID = input("请输入UID：")
steps = input("请输入记录量级：")
steps = int(steps)
with open("粉丝数.txt", "a") as file:
    file.write("\n")
    file.write("\n")
    file.write(user_ID + " " + str(datetime.datetime.now()))
    file.write("\n")
with open("日志1.txt", "a") as file:
    file.write("\n")
    file.write("\n")
    file.write(user_ID + " " + str(datetime.datetime.now()))
    file.write("\n")


def get_main():
    test_fans = user_fans // steps
    x.append("记录变化情况：")
    while True:
        time_break = random.uniform(0.5,5)
        time.sleep(time_break)
        reponse = requests.get(url=url,headers=headers)
        result = reponse.text
        user_dict = ast.literal_eval(result)
        b = datetime.datetime.now()
        try:
            a = user_dict["data"]["follower"]
        except ValueError:
            print("API已封禁，请稍后再试！")
            browser = webdriver.Chrome(executable_path="chromedriver.exe")
            browser.get("https://www.gitee.com")
            with open("日志1.txt", "a") as file:
                file.write(str(datetime.datetime.now()) + "" +"出错了！" + "\n")
            break
        if (a >= user_fans) and (a // steps >test_fans):
            print("恭喜！")
            with open("播放量.txt", "a") as file:
                file.write(F"{a}播放达成时间：" + str(datetime.datetime.now()) + "\n")
            time.sleep(5)
            root = tk.Tk()
            w = tk.Label(root, text=f"恭喜 {User_ID} 在{b} 获得了{a} 粉丝！")
            w.pack()
            root.geometry("300x200")
            root.lift()
            root.attributes('-topmost',True)
            root.after_idle(root.attributes,'-topmost',False)
            root.mainloop()
        print(F"时间{b}，粉丝数{a}")
        if a != x[-1:][0]:
            with open("日志1.txt", "a") as file:
                file.write(F"时间{b}，粉丝数{a}" + "\n")
        test_fans = a // steps
        x.append(a)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
url = F"https://api.bilibili.com/x/relation/stat?vmid={user_ID}&jsonp=jsonp"
reponse = requests.get(url=url,headers=headers)
result = reponse.text
user_dict = ast.literal_eval(result)
b = datetime.datetime.now()
try:
    user_fans = user_dict["data"]["follower"]
    k = 3
except ValueError:
    print("API已封禁，请稍后再试！")
    browser = webdriver.Chrome(executable_path="chromedriver.exe")
    browser.get("https://www.gitee.com")
    with open("日志1.txt", "a") as file:
        file.write(str(datetime.datetime.now()) + "" +"出错了！" + "\n")
    k = 5
time.sleep(random.uniform(0.5,5))

if k == 3:
    get_main()
