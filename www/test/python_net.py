# !-_- coding:utf-8 -_-!
"This is a practice about python net operation"


# import urllib
# response=urllib.urlopen("http://coolshell.cn/featured_posts")
# html=response.read()
# print html



import urllib,urllib2
url="http://coolshell.cn/featured_posts"
read=urllib2.urlopen(url)
data=read.read()
with open("coolshell.html","wb") as code:
    code.write(data)
urllib.urlretrieve(url,"shell.html")