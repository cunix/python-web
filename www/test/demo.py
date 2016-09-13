import urllib2 , urllib
from bs4 import BeautifulSoup
import time
url=[]
def geturl(depth):
    j=0
    global url
    while j<depth:
        taobaourl="http://mm.taobao.com/json/request_top_list.htm?type=2&page="+str(j)
        print taobaourl
        ret=urllib2.urlopen(taobaourl)
        ret=ret.read()
        soup=BeautifulSoup(ret)
        tag=soup.findAll('a',{'class:','lady-avatar'})
        print tag
        for hr in tag:
            url.append("http:"+hr.get("href"))
        j+=1

def getpic(urlr):
    urlpic=[]
    picurl="http://mm.taobao.com/139108254.htm"
    print 'in getpic',urlr
    ret=urllib2.urlopen(urlr)
    ret=ret.read()
    soup=BeautifulSoup(ret)
    tag=soup.findAll('img',{'style':'float:none;margin:10.0px;'})
    if len(tag)==0:
        tag = soup.findAll('img', {'style': 'margin:10.0px;float:none;'})
    print 'tag',tag
    uu="http://img04.taobao.com/imgextra/i4/18254030107239481/T1GBDFiBeXXXXXXXX_!!"
    for hr in tag:
        urlpic.append(hr.get("src"))
    #download image
    i=0
    for urlx in urlpic:
        un=urlx[len(uu):]
        un=un[:-4]+str(i)+".jpg"
        print 'from',urlr
        print "downloading....",un
        if len(urlpic[i]):
            urllib.urlretrieve(urlpic[i],'pic/'+un)
            time.sleep(0.2)
            i+=1

def main():
    d=10
    geturl(d)
    print len(url),url
    i=1
    while i<len(url):
        print "in main",url[i]
        getpic(url[i])
        i+1

if __name__ == '__main__':
    main()






