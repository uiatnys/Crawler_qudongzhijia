import urllib2
import urllib
import time

url = 'http://news.mydrivers.com/'
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'

i=0
while (i<5):
    timestamp = int(round(time.time() * 1000))
    values = {"pageid":'5','cids':'','timestamp':timestamp,'callback':'NewsList','_':timestamp}
# headers= {'User-Agent':user_agent
#          ,'Cookie':'JSESSIONID=50C8B6B6DB530B00ED9942A01C4AE27A; _gscu_1924971701=877505915xrsx786; _gscs_1924971701=87750591hlo3np86|pv:2; _gscbrs_1924971701=1'
#          ,'Connection':'keep-alive'
#          ,'Accept-Language':'zh-CN,zh;q=0.8'
#          ,'Accept-Encoding':'gzip, deflate, sdch'
#          ,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
#          ,'Referer':'https://www.baidu.com/link?url=8kiCOuck2laQYSYSfkg5LVgGEpanX1k6qiATCCgfNn4CD8nMGnIbzsWA3cbO__z-&wd=&eqid=d9753493000061490000000458ad43f4'
#          ,'If-None-Match':'58acf73a-6ca6'}
    date = urllib.urlencode(values)
    response = urllib2.Request(url)
    responses = urllib2.urlopen(response,date)
    #print responses.read()
    file_object = open(r'D:\python\test.txt','a')
    try:
        file_object.write(responses.read())
    finally:
        file_object.close()
    i = i+1
    print i
