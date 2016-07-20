import sys

from bs4 import BeautifulSoup
import urllib.request

import http.client
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'
import time

import random


def crawl_dcinside(filePath):
    pageCount = 1
    while True:
        page_url = 'http://gall.dcinside.com/board/lists/?id=samsunglions&page='
        url_open = urllib.request.urlopen(page_url)

        soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')

        tr_list = soup.findAll('tr', attrs={'class':'tb'})


        for tr_count in range(1, len(tr_list)):
            body_list = tr_list[tr_count].find('td', attrs={'class':'t_subject'})
            body_url =  'http://gall.dcinside.com'+body_list.find('a')['href']
            notice = tr_list[tr_count].find('td', attrs={'class':'t_subject'}).text
            save_content(notice, body_url, filePath)
            #print(notice)

        pageCount+=30

def save_content(cid, content_url, filePath):

    try:
        url_open = urllib.request.urlopen(content_url)
    except UnicodeEncodeError as e:
        print(cid, e)
        return

    soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')

    try:
        f=open(filePath+cid+'.html', 'w')
        f.write(soup.prettify())
        f.close()
        print (cid+ ' save complete...')
    except UnicodeEncodeError as e:
        print(e)
    time.sleep(random.randrange(2,5))




def main():

    if len(sys.argv)<2:
        print('Need File Path')
        sys.exit()

    filePath = sys.argv[1]
    crawl_dcinside(filePath)


if __name__ == "__main__":
    main()