# encoding='utf-8

# @Time: 2023-08-24
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests
from lxml import etree


# text = open('gigab2b_w679.html', 'r', encoding='utf-8').read()
#
# content = etree.HTML(text)

def Parse_href(content):
    divs = content.xpath('//*[@id="product_all_list"]/div')
    links = []
    for div in divs:
        divvs = div.xpath('./div')
        # print(len(divvs))
        for divv in divvs:
            link = divv.xpath('./div/div/a/@href')[0]
            # print(link)
            links.append(link)
    print(len(links))
    return links
