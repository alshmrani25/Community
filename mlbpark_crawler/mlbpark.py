from bs4 import BeautifulSoup
import urllib.request
import time
import random


def crawl_mlbpark():
    pageCount = 1
    while True:
        page_url = 'http://mlbpark.donga.com/mlbpark/b.php?p="+str(pageCount)+"&m=list&b=kbotown2&query=&select=title&user='
        url_open = urllib.request.urlopen(page_url)

        soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')

        table_list = soup.find('table', attrs={'class':'tbl_type01'})

        tr_list = table_list.findAll('tr')


        for tr_count in range(3, len(tr_list)):
            notice = str(tr_list[tr_count].find('td').text)
            saveContent(pageCount, notice)
            #print(notice)

        pageCount+=30

def saveContent(pageCount, cid):
    content_url = 'http://mlbpark.donga.com/mlbpark/b.php?p='+str(pageCount)+'&b=kbotown2&id='+str(cid)+'&select=title&query=&user=&reply='

    try:
        url_open = urllib.request.urlopen(content_url)
    except UnicodeEncodeError as e:
        print(cid, e)
        return

    soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')

    f=open('/home/hknam/Documents/mlbpark/data/'+cid+'.html', 'w')
    f.write(soup.prettify())
    f.close()
    print (cid+ ' save complete...')

    time.sleep(random.randrange(2,5))

def main():
    crawl_mlbpark()

if __name__ == '__main__':
    main()