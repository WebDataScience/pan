from HTMLParser import HTMLParser
from os import listdir
from os.path import isfile, join
import os, re

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

    onlyfiles = [ f for f in listdir(src) if isfile(join(src,f)) ]

    for entry in onlyfiles:
        with open (src + "/" + entry, "r") as myfile:
            data=myfile.read().replace('\n', '').replace('\t', '')
            data=re.sub("a href=(.)*;", '', data)

            file(dst + "/" + entry,"wb").write(strip_tags(data).replace('\n', '').replace('\r', '').replace('/', '').replace(';br', '').replace(';li', ''))