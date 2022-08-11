import trafilatura
import feedparser
import yaml


def readfeeds():
    with open("feeds.yaml", "r") as f:
        feeds = yaml.load(f)
        return feeds


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
    return xml


def main(key):
    feeds = readfeeds()
    for feed in feeds:
        if key == feed.key:
            url = feed.url
            return reconstructfeed(url)


print(reconstructfeed('https://www.theatlantic.com/feed/all/'))
