import feedparser

f = feedparser.parse(r'reddit.rss')
print(f['feed']['title'])
print(f.feed.title)
print(type(f.feed.title))
print(f.entries[0].author)
print(f.entries[0].title)
