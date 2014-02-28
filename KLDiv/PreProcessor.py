from HTMLParser import HTMLParser
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
import os, re, shutil
import unicodedata

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

#strip html from text
def clean(src, dst):
    path = "src"
    clean_path = "dst"

    if not os.path.exists(dst):
        os.makedirs(dst)
    else:
        shutil.rmtree(dst)
        os.makedirs(dst)

    onlyfiles = [ f for f in listdir(src) if isfile(join(src,f)) ]

    print "Cleaning Files"

    for entry in onlyfiles:
        soup = BeautifulSoup(open(src+"/"+entry))
        
        file(dst + "/" + entry,"wb").write(unicodedata.normalize('NFKD', re.sub(' +',' ', strip_tags(soup.prettify()).replace("\n", "").replace("\t", ""))).encode('ascii','ignore'))