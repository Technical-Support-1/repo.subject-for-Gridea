import requests
import ast
import time
import datetime
from selenium import webdriver 
import random
import math

def BvToAv(Bv):
    # 1.去除Bv号前的"Bv"字符
    BvNo1 = Bv[2:]
    keys = {
        '1':'13', '2':'12', '3':'46', '4':'31', '5':'43', '6':'18', '7':'40', '8':'28', '9':'5',
        'A':'54', 'B':'20', 'C':'15', 'D':'8', 'E':'39', 'F':'57', 'G':'45', 'H':'36', 'J':'38', 'K':'51', 'L':'42', 'M':'49', 'N':'52', 'P':'53', 'Q':'7', 'R':'4', 'S':'9', 'T':'50', 'U':'10', 'V':'44', 'W':'34', 'X':'6', 'Y':'25', 'Z':'1',
        'a': '26', 'b': '29', 'c': '56', 'd': '3', 'e': '24', 'f': '0', 'g': '47', 'h': '27', 'i': '22', 'j': '41', 'k': '16', 'm': '11', 'n': '37', 'o': '2',
        'p': '35', 'q': '21', 'r': '17', 's': '33', 't': '30', 'u': '48', 'v': '23', 'w': '55', 'x': '32', 'y': '14','z':'19'

    }
    # 2. 将key对应的value存入一个列表
    BvNo2 = []
    for index, ch in enumerate(BvNo1):
        BvNo2.append(int(str(keys[ch])))

    # 3. 对列表中不同位置的数进行*58的x次方的操作

    BvNo2[0] = int(BvNo2[0] * math.pow(58, 6));
    BvNo2[1] = int(BvNo2[1] * math.pow(58, 2));
    BvNo2[2] = int(BvNo2[2] * math.pow(58, 4));
    BvNo2[3] = int(BvNo2[3] * math.pow(58, 8));
    BvNo2[4] = int(BvNo2[4] * math.pow(58, 5));
    BvNo2[5] = int(BvNo2[5] * math.pow(58, 9));
    BvNo2[6] = int(BvNo2[6] * math.pow(58, 3));
    BvNo2[7] = int(BvNo2[7] * math.pow(58, 7));
    BvNo2[8] = int(BvNo2[8] * math.pow(58, 1));
    BvNo2[9] = int(BvNo2[9] * math.pow(58, 0));

    # 4.求出这10个数的合
    sum = 0
    for i in BvNo2:
        sum += i
    # 5. 将和减去100618342136696320
    sum -= 100618342136696320
    # 6. 将sum 与177451812进行异或
    temp = 177451812

    return sum ^ temp
    
if __name__ == '__main__':
    Bv = input("请输入Bv号:")
    av_video = str(BvToAv(Bv))

with open("播放量.txt", "a") as file:
    file.write("\n")
    file.write("\n")
    file.write(Bv + " " + str(datetime.datetime.now()))
    file.write("\n")
with open("日志.txt", "a") as file:
    file.write("\n")
    file.write("\n")
    file.write(Bv + " " + str(datetime.datetime.now()))
    file.write("\n")

def get_main(ready_number,say):
    while True:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
        url = F"http://api.bilibili.com/archive_stat/stat?aid={av_video}"
        time_break = random.uniform(0.5,5)
        time.sleep(time_break)
        reponse = requests.get(url=url,headers=headers)
        result = reponse.text
        user_dict = ast.literal_eval(result)
        b = datetime.datetime.now()
        try:
            a = user_dict["data"]["view"]
        except ValueError:
            print("API已封禁，请稍后再试！")
            browser = webdriver.Chrome(executable_path="chromedriver.exe")
            browser.get("https://www.gitee.com")
            with open("日志.txt", "a") as file:
                file.write(str(datetime.datetime.now()) + "" +"出错了！" + "\n")
            break
        if a >= ready_number:
            print("恭喜！")
            with open("播放量.txt", "a") as file:
                file.write(F"{say}播放达成时间：" + str(datetime.datetime.now()) + "\n")
            time.sleep(5)
            root = tk.Tk()
            w = tk.Label(root, text=f"恭喜{av_video}在{b}获得了 {a}播放！")
            w.pack()
            root.geometry("300x200")
            root.lift()
            root.attributes('-topmost',True)
            root.after_idle(root.attributes,'-topmost',False)
            root.mainloop()
            break
        print(F"时间{b}，播放量{a}")
        with open("日志.txt", "a") as file:
            file.write(F"时间{b}，播放量{a}" + "\n")

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
url = F"http://api.bilibili.com/archive_stat/stat?aid={av_video}"
reponse = requests.get(url=url,headers=headers)
result = reponse.text
user_dict = ast.literal_eval(result)
b = datetime.datetime.now()
try:
    fans_number = user_dict["data"]["view"]
    k = 3
except ValueError:
    print("API已封禁，请稍后再试！")
    browser = webdriver.Chrome(executable_path="chromedriver.exe")
    browser.get("https://www.gitee.com")
    with open("日志.txt", "a") as file:
        file.write(str(datetime.datetime.now()) + "" +"出错了！(test)" + "\n")
    k = 5
time.sleep(random.uniform(0.5,5))

if k != 5:
    if fans_number < 10000:
        get_main(10000,"一万")
    if fans_number < 100000:
        get_main(100000,"十万")
    if fans_number < 1000000:
        get_main(1000000,"百万")
    if fans_number < 10000000:    
        get_main(10000000,"千万")
    if fans_number < 100000000:
        get_main(100000000,"一亿")
