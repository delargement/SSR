import trafilatura
import dict2xml
import feedparser
import yaml
from feedgen.feed import FeedGenerator


def readfeeds():
    with open("feeds.yaml", "r") as f:
        feeds = yaml.load(f,yaml.SafeLoader)
        return feeds

def genfeed(feed):
    fg = FeedGenerator()
    fg.id(feed['feed']['link'])
    fg.title(feed['feed']['title'])
    fg.link(href=feed['feed']['link'])
    fg.updated(feed['feed']['updated'])
    fg.description(feed['feed']['title'])
    for entry in feed['entries']:
        fe = fg.add_entry()
        fe.id(entry['id'])
        fe.title(entry['title'])
        fe.link(href=entry['link'])
        fe.updated(entry['updated'])
        fe.content(entry['content'], type='xhtml')
        fe.updated(entry['updated'])
        fe.summary(entry['summary'], type='html')
        fe.description(entry['title'])
        # fe.author({'name': auth['name'] for auth in entry['authors']})
    fg.rss_file('feed.xml')
    return fg.rss_str()

def reconstructfeed(feedurl):
    xml = feedparser.parse(feedurl)
    links = [entry.link for entry in xml.entries]
    fetches = [trafilatura.fetch_url(link) for link in links]
    contents = [trafilatura.extract(trafilatura.fetch_url(ls),
                                    include_links=True,
                                    output_format='xml')
                for ls in links]
    for entry, content in zip(xml.entries, contents):
        entry['content'] = content
    # return xml
    return genfeed(xml)
    # return dict2xml.dict2xml(xml)


def main(key):
    feeds = readfeeds()
    for feed in feeds:
        if key == feed['key']:
            url = feed['feedurl']
            return reconstructfeed(url)
