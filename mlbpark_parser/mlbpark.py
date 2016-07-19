import os
import sys
import urllib
from bs4 import BeautifulSoup

def read_file(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        parse_html(full_filename)


def parse_html(filePath):
    url_open = urllib.urlopen(filePath)
    soup = BeautifulSoup(url_open, 'html.parser')

    try:
        title_div = soup.find('div', attrs={'class':'titles'})
        span_keyword = title_div.find('span').text.strip()

        offset = title_div.text.find(span_keyword)
        title = title_div.text.strip()
        title = title.replace('\n', '')
        title = title.replace('  ', '')
        if offset > 0:
            title = title.replace(span_keyword, '')

        date_div = soup.find('div', attrs={'class':'text3'})
        date_div = date_div.text.strip()
        date_div = date_div.replace('\n', '')
        date_div = date_div.replace('  ', '')
        notice = date_div.split("|")[0][4:]
        write_time = date_div.split("|")[1].strip()

        author_div = soup.find('div', attrs={'class':'text1'})
        author = author_div.text
        author = author.replace('\n', '')
        author = author.replace(' ', '')

        recomm_div = soup.find('div', attrs={'class':'text2'})
        recomm_list = recomm_div.findAll('span', attrs={'class':'val'})

        recomm_count = recomm_list[0].text
        recomm_count = recomm_count.replace('\n', '')
        recomm_count = recomm_count.replace(' ', '')

        read_count =  recomm_list[1].text
        read_count = read_count.replace('\n', '')
        read_count = read_count.replace(' ', '')

        body_div = soup.find('div', attrs={'id':'contentDetail'}).text.strip()
        body = body_div.replace('\n', ' ')
        body = body.replace('           ', ' ')

        reply_lst = soup.find('div', attrs={'class':'reply_list'})
        reply_lst = reply_lst.findAll('div', attrs={'class':'other_con'})
        reply_count = len(reply_lst)

        #reply_list = []

        for i in range(0, reply_count):
            reply_nickname = reply_lst[i].find('span', attrs={'class':'name'}).text.strip()
            reply_nickname = reply_nickname.replace('\n', '')

            reply_date = reply_lst[i].find('span', attrs={'class':'date'}).text.strip()
            reply_date = reply_date.replace('n', '')

            reply_txt = reply_lst[i].find('span', attrs={'class':'re_txt'}).text.strip()
            reply_txt = reply_txt.replace('\n', '')

            print reply_nickname, reply_date, reply_txt


        #print title, author, notice, write_time, recomm_count, read_count, comment_count

    except AttributeError as e:
        print e
        return


def main():


    if len(sys.argv) < 2:
        print 'Need file path'
        sys.exit()

    filePath = sys.argv[1]

    read_file(filePath)


if __name__ == '__main__':
    main()