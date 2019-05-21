# encoding=utf-8
from urllib import request
import http.cookiejar as cookielab


url = "http://www.baidu.com"
# 基本网页下载
response = request.urlopen('http://www.baidu.com')
print(response.getcode())
cont = response.read()
print(len(cont))
# 添加cookie处理
cj = cookielab.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
response2 = request.urlopen(url)
print(response2.getcode())
print(cj)
print(len(response2.read()))

#打印网页源代码
print(str(cont,'utf-8'))
