import requests
key_dict={
    'key1':'value1','key2':'value2','key3':'value3'
}

respose=requests.get('http://httpbin.org/get',params=key_dict)
print('URL已经正确编码：',respose.url)
print('字符串方式的相应体：\n',respose.text)
