import sys

from bs4 import BeautifulSoup
import urllib.request

import http.client
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'
import time

import random

class Dcinside:

    """
    주식갤 : id=stock_new1
    인방갤 : id=ib
    국내야갤 : id=baseball_new4
    기타국내드라마 : id=drama_new
    던전앤파이터 : id=d_fighter_new
    """

    def crawl(self):

        #f = open(pageName+".txt", "w")
        pageCount = 1
        while True:

            page = "http://gall.dcinside.com/board/lists/?id=baseball_new&page="+str(pageCount)
            url_open = urllib.request.urlopen(page)

            soup = BeautifulSoup(url_open, 'html.parser', from_encoding = 'utf-8')
            obj = soup.findAll('tr', attrs = {'class':'tb'})

            for j in range(1, len(obj)):

                b = obj[j].find('td', attrs={'class':'t_subject'})
                url = 'http://gall.dcinside.com'+b.find('a')['href']

                notice = obj[j].find('td', attrs={'class':'t_notice'}).text
                body_url_open = urllib.request.urlopen(url)
                body_soup = BeautifulSoup(body_url_open, 'html.parser', from_encoding="utf-8")
                html_source = str(body_soup.prettify())
                f=open("/home/hknam/Documents/dcinside/data/"+str(notice)+".html", "w")
                f.write(html_source)
                f.close()
                print(notice, str(pageCount)+" page")
                time.sleep(random.randrange(2,5))

            pageCount+=1


def main():
    '''
    print("stock_new1, baseball_new4, ib, drama_new")
    pageName = input("Enter page name : ")
    if len(sys.argv) < 1:
        print("Need Page Name")
    stock = "stock_new1"
    ib = "ib"
    baseball = "baseball_new4"
    drama = "drama_new"
    '''
    dcinside = Dcinside()
    #dcinside.crawl(stock, 20)
    dcinside.crawl()


if __name__ == "__main__":
    main()