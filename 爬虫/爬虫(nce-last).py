import requests
from selenium import webdriver
from lxml import etree
import time
from bs4 import BeautifulSoup     # 导入所需模块
import re
last_text = []
def get_url():
    import re
    import requests
    from bs4 import BeautifulSoup
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
    url = "https://nce.koolearn.com/20150206/782161.html"
    reponse = requests.get(url=url,headers=headers,timeout=5.0)
    time.sleep(5)
    reponse.encoding = "utf-8"
    text = reponse.text
    soup = BeautifulSoup(text,"lxml")

    a = "http://nce.koolearn.com/20150122/781915.html 1 http://nce.koolearn.com/20150122/781916.html 3 http://nce.koolearn.com/20150122/781917.html 5 http://nce.koolearn.com/20150122/781918.html 7 http://nce.koolearn.com/20150122/781919.html 9 http://nce.koolearn.com/20150122/781920.html 11 http://nce.koolearn.com/20150122/781921.html 13 http://nce.koolearn.com/20150122/781922.html 15 http://nce.koolearn.com/20150122/781923.html 17 http://nce.koolearn.com/20150122/781924.html 19 http://nce.koolearn.com/20150123/781955.html 21 http://nce.koolearn.com/20150123/781956.html 23 http://nce.koolearn.com/20150123/781957.html 25 http://nce.koolearn.com/20150123/781958.html 27 http://nce.koolearn.com/20150123/781959.html 29 http://nce.koolearn.com/20150123/781960.html 31 http://nce.koolearn.com/20150123/781961.html 33 http://nce.koolearn.com/20150123/781962.html 35 http://nce.koolearn.com/20150123/781963.html 37 http://nce.koolearn.com/20150123/781964.html 39 http://nce.koolearn.com/20150126/781995.html 41 http://nce.koolearn.com/20150126/781996.html 43 http://nce.koolearn.com/20150126/781997.html 45 http://nce.koolearn.com/20150126/781998.html 47 http://nce.koolearn.com/20150126/781999.html 49 http://nce.koolearn.com/20150127/782015.html 51 http://nce.koolearn.com/20150127/782016.html 53 http://nce.koolearn.com/20150127/782017.html 55 http://nce.koolearn.com/20150127/782018.html 57 http://nce.koolearn.com/20150127/782019.html 59 http://nce.koolearn.com/20150128/782040.html 61 http://nce.koolearn.com/20150128/782041.html 63 http://nce.koolearn.com/20150128/782042.html 65 http://nce.koolearn.com/20150128/782043.html 67 http://nce.koolearn.com/20150128/782044.html 69 http://nce.koolearn.com/20150129/782060.html 71 http://nce.koolearn.com/20150129/782061.html 73 http://nce.koolearn.com/20150129/782062.html 75 http://nce.koolearn.com/20150129/782063.html 77 http://nce.koolearn.com/20150129/782064.html 79 http://nce.koolearn.com/20150130/782080.html 81 http://nce.koolearn.com/20150130/782081.html 83 http://nce.koolearn.com/20150130/782082.html 85 http://nce.koolearn.com/20150130/782083.html 87 http://nce.koolearn.com/20150130/782084.html 89 http://nce.koolearn.com/20150202/782103.html 91 http://nce.koolearn.com/20150202/782104.html 93 http://nce.koolearn.com/20150202/782105.html 95 http://nce.koolearn.com/20150202/782106.html 97 http://nce.koolearn.com/20150202/782107.html 99 http://nce.koolearn.com/20150203/782113.html 101 http://nce.koolearn.com/20150203/782114.html 103 http://nce.koolearn.com/20150203/782115.html 105 http://nce.koolearn.com/20150203/782116.html 107 http://nce.koolearn.com/20150203/782117.html 109 http://nce.koolearn.com/20150204/782129.html 111 http://nce.koolearn.com/20150204/782130.html 113 http://nce.koolearn.com/20150204/782131.html 115 http://nce.koolearn.com/20150204/782132.html 117 http://nce.koolearn.com/20150204/782133.html 119 http://nce.koolearn.com/20150205/782144.html 121 http://nce.koolearn.com/20150205/782145.html 123 http://nce.koolearn.com/20150205/782146.html 125 http://nce.koolearn.com/20150205/782147.html 127 http://nce.koolearn.com/20150205/782148.html 129 http://nce.koolearn.com/20150206/782154.html 131 http://nce.koolearn.com/20150206/782155.html 133 http://nce.koolearn.com/20150206/782156.html 135 http://nce.koolearn.com/20150206/782157.html 137 http://nce.koolearn.com/20150206/782158.html 139 http://nce.koolearn.com/20150206/782159.html Lesson141 http://nce.koolearn.com/20150206/782160.html Lesson143"
    a = soup.select(".xqy_core_text")
    a = str(a[0])
    global last_url
    last_url = re.findall('http://nce.koolearn.com/[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]/[0-9][0-9][0-9][0-9][0-9][0-9].html',a)
    last_url = last_url[2:]
    global last_url2
    last_url2 = last_url
    last_url2 = str(last_url2)
def get_text(url):
    last_text = []
    k = 0
    n = 0
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}   # 标头
    reponse = requests.get(url=url,headers=headers,timeout=(3.0,7.0))    # 获得字节码
    time.sleep(5)
    reponse.encoding = "utf-8"     # 指定编码方式避免乱码
    global result
    result = reponse.text   # 获取网页源代码
    
    soup = BeautifulSoup(result,"lxml")
    global b
    b = soup.select('.xqy_container.w1200>.xqy_container_box>.xqy_core>.xqy_core_main>.xqy_core_text>p')
    for test in range(len(b)):
        b[test] = str(b[test])
        b[test] = b[test].replace("<p>","")
        b[test] = b[test].replace("</p>","")
        b[test] = b[test].replace("\u3000","")
        b[test] = b[test].replace("\n","")
        b[test] = b[test].replace("\r","")
        if b[test] == "【课文】":
            start = test
            k =3
        if b[test] == "【课文翻译】":
            last = test
            n = 3
    if (k!=3) or (n!=3):
        start = 0
        last = len(b)-1
    last_text.append(b[start:last])
    global last_text1
    last_text1 = str(last_text)
    """
    global c
    global d
    c = etree.HTML(result)   # 实例化etree对象
    d = c.xpath('//div[@class="xqy_core_main"]/div/p//text()')    # 通过XPath获取信息
    """
get_url()
# last_url = ['http://nce.koolearn.com/20150206/782156.html', 'http://nce.koolearn.com/20150206/782157.html', 'http://nce.koolearn.com/20150206/782158.html', 'http://nce.koolearn.com/20150206/782159.html', 'http://nce.koolearn.com/20150206/782160.html']
for ppt in last_url:
    get_text(ppt)
    print(F"{ppt}已经完成")
    with open("nce1.txt","a",encoding="utf-8") as fp:
        fp.write(ppt + last_text1 + "\n")
