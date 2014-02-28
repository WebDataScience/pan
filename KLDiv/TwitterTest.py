import twitter
from xml.dom import minidom

#Gets 
def getTweetText(id):

	api = twitter.Api(consumer_key='VQBHhv9HTDPhvUJaWiPS8w',consumer_secret='RR7rs0O2CA69bVBH99BJFFPk7OWxg1cOFgoQ6tllk',access_token_key='1419796309-piq3wxkBNKFSiZ2xgB3V6GfO492IrnYKNWg620C',access_token_secret='VeD79qq68cy8cuZwgt9xoGd7RUaMj1aN5Kze2tBVFLKKY')

	status = api.GetStatus(id)
	return status.GetText()

def getAllTweets(path):
	tweetlist = []

	xmldoc = minidom.parse(path)
	itemlist = xmldoc.getElementsByTagName('document') 
	for s in itemlist :
		tweetlist.append(getTweetText(s.attributes['id'].value))
	return tweetlist

getAllTweets("/Users/the_james_marq/PAN/Data/PAN14/twitter/en/75470794aa1249218c8d5699018560ab_en_50-64_female.xml")