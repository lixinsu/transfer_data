#!/usr/bin/env python
# coding: utf-8

import time
import json
import urllib
import requests
from pprint import pprint
from xml.etree import ElementTree
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=options)

def bing_search(query):
    query = query.replace('\"', '').replace('\'', '')
    driver.get("https://cn.bing.com/?ensearch=1&FORM=BEHPTB") #http://www.bing.com/search?format=rss&ensearch=1&FORM=QBLH&q=%s" % urllib.parse.quote(query))
    element = driver.find_element_by_name("q")
    element.send_keys(query, Keys.RETURN)
    ele = driver.find_element_by_id('b_results')
    eles = ele.find_elements_by_xpath('li[@class="b_algo"]')
    texts = []
    for ele in eles:
        try:
            text = ele.find_element_by_xpath('div[@class="b_caption"]/p').text
            texts.append(text)
            continue
        except:
            pass
        try:
            text = ele.find_element_by_xpath('div[@class="b_caption"]/div[@class="b_snippet"]/p').text
            texts.append(text)
            continue
        except:
            pass
    return texts

if __name__ == "__main__":
    st = time.time()
    try:
        for q in list(json.load(open('qid_query_mapping.json.0')).values())[:50]:
            print(q)
            ts = bing_search_by_se(q)
            pprint(ts[:2])
            print(len(ts))
    except KeyboardInterrupt:
        driver.close()
        print(time.time()-st)
        raise
    driver.close()
    print(time.time()-st)

