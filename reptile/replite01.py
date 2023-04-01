import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings


disable_warnings(InsecureRequestWarning)

#网页url
url='https://www.example.com'


# 发送get或post请求并获取网页信息
req=requests.get(url,verify=False)
print(req.status_code)

# 使用bs解析网页内容
soup=BeautifulSoup(req.text,'html.parser')

# 提取网页中的所有链接和标题
links=[]
for link in soup.find_all('a'):
    links.append({
        'title':link.get('title'),
        'url':link.get('href')
    })


# 打印所有链接和标题
for link in links:
    print(link['title'],link['url'])