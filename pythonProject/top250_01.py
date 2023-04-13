import random
import requests
from bs4 import BeautifulSoup

def get_movies():
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    ]
    headers = {
        'User-Agent': random.choice(user_agents),
        'Host': 'movie.douban.com'
    }
    movie_list = []
    for i in range(0,10):
        link= 'https://movie.douban.com/top250?start=' + str (i*25)
        try:
            response=requests.get(link,headers=headers,proxies=proxies,timeout=10)
            if response.status_code != 200:
                print(str(i+1),'请求失败')
                return None
            soup=BeautifulSoup(response.text,"lxml")
            div_list = soup.find_all('div',class_='hd')
            if not div_list:
                print(str(i+1),'返回结果为空')
                return None
            for each in div_list:
                movie = each.a.span.text.strip()
                movie_list.append(movie)
        except Exception as e:
            print(str(i+1),'请求或解析失败')
            return None
    return movie_list