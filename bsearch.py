#!/usr/bin/env python
# coding: utf-8

import requests
from pprint import pprint
from xml.etree import ElementTree

def bing_search(query):
    response = requests.get("http://www.bing.com/search?format=rss&ensearch=1&FORM=QBLH&q=%s" % query)
    tree = ElementTree.fromstring(response.content)
    x = tree.find('item')
    texts = []
    for it in tree.find('channel').findall('item'):
        texts.append(it.find('description').text)
    return texts


if __name__ == "__main__":
    while True:
        q = input("query:")
        ts = bing_search(q)
        pprint(ts)

