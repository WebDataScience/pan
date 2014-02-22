from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import re

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

def extractText(src):
	soup = BeautifulSoup(open(src))
	print re.sub(' +',' ', strip_tags(soup.prettify()).replace("\n", "").replace("\t", ""))

extractText("/home/jamarq/PAN/Data/PAN14/PAN14/pan14-author-profiling-training-corpus-blogs-2014-02-10/en/fe826c2665b9aecd0e77a27eaa21e1d5_en_35-49_male.xml")
