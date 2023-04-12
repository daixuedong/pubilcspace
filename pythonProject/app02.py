import requests
r=requests.get('http://www.santostang.com/')
print('文本编码：',r.encoding)
print('相应状态码：',r.status_code)
print('字符串方式响应体：',r.text)
