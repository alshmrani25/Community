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
