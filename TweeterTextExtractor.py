import os,re
import urllib2
import urllib
import sys, os
import datetime
from urllib2 import urlopen


def getPageContent(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""
    
def extractTweet(content):
    tweetLabel = '<title>Twitter'
    tweet = ''
    index = content.find( tweetLabel)
    if index <>-1:
        startIndex = content.find(':',index)
        finishIndex = content.find('</title>',index)
        tweet = content[startIndex+1: finishIndex]
    return tweet
    
  
def getTweet(url):
    content = getPageContent(url)
    tweet = extractTweet(content)  
    return tweet     


print getTweet('https://twitter.com/GE_Miller/status/10001439929')