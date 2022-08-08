from newsplease import NewsPlease
import feedparser
from requests import get


def readfeeds():
    with open()


def main():
    urls = ['https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
            'https://theatlantic.com/feed/all']
    fs = [feedparser.parse(u) for u in urls]
    links = [[f.link for f in src.entries] for src in fs]







#print(feed)
