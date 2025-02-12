from json import dump
from urllib.request import urlopen
from xml.etree.ElementTree import fromstring, Element

res = []
item: Element

for item in fromstring(urlopen('https://lenta.ru/rss').read().decode('utf8')).findall('channel/item'):
    res.append({c.tag: c.text for c in item})

with open("news_items.json", "w", encoding='UTF-8') as out:
    dump(res, out, indent=1, ensure_ascii=False)