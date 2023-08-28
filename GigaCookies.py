# encoding='utf-8
# @Time: 2023-08-27
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import re
import execjs
import requests
index_url = "https://www.gigab2b.com/"
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryJVhdwreLurE0oIMR',
    'Origin': 'https://www.gigab2b.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.gigab2b.com/index.php?route=account/login',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

session = requests.session()
session.headers.update(headers)

def login(cookies):
    resp = requests.get(url=index_url, headers=headers)
    complete_cookie.update(resp.cookies.get_dict())
    pattern = r"window\.oriCsrfToken\.init\('X-CSRF-TOKEN', '([^']+)'\);"
    match = re.search(pattern, resp.text)
    # 如果匹配成功，则提取出字段内容
    if match:
        csrf_token = match.group(1)
        print("匹配到的 X-CSRF-TOKEN 字段内容:", csrf_token)
    else:
        print("未匹配到任何内容")
    data = '------WebKitFormBoundaryJVhdwreLurE0oIMR\r\nContent-Disposition: form-data; name="X-CSRF-TOKEN"\r\n\r\n{}\r\n------WebKitFormBoundaryJVhdwreLurE0oIMR\r\nContent-Disposition: form-data; name="email"\r\n\r\nlarryerik14@gmail.com\r\n------WebKitFormBoundaryJVhdwreLurE0oIMR\r\nContent-Disposition: form-data; name="password"\r\n\r\nlarryerik14\r\n------WebKitFormBoundaryJVhdwreLurE0oIMR\r\nContent-Disposition: form-data; name="redirect"\r\n\r\nhttps://www.gigab2b.com/index.php?route=common/home\r\n------WebKitFormBoundaryJVhdwreLurE0oIMR--\r\n'.format(
        csrf_token)
    response = session.post(
        'https://www.gigab2b.com/index.php?route=account/login', data=data, cookies=cookies)
    return response




def get_complete_cookie():
    complete_cookie = {}
    # 第一次不带参数访问首页，获取 acw_tc 和 acw_sc__v2
    resp = requests.get(url=index_url, headers=headers)
    complete_cookie.update(resp.cookies.get_dict())
    pattern = r"window\.oriCsrfToken\.init\('X-CSRF-TOKEN', '([^']+)'\);"
    match = re.search(pattern, resp.text)
    # 如果匹配成功，则提取出字段内容
    if match:
        csrf_token = match.group(1)
        print("匹配到的 X-CSRF-TOKEN 字段内容:", csrf_token)
    else:
        print("未匹配到任何内容")
    data = '------WebKitFormBoundaryJVhdwreLurE0oIMR\r\nContent-Disposition: form-data; name="X-CSRF-TOKEN"\r\n\r\n{}\r\n------WebKitFormBoundaryJVhdwreLurE0oIMR\r\nContent-Disposition: form-data; name="email"\r\n\r\nlarryerik14@gmail.com\r\n------WebKitFormBoundaryJVhdwreLurE0oIMR\r\nContent-Disposition: form-data; name="password"\r\n\r\nlarryerik14\r\n------WebKitFormBoundaryJVhdwreLurE0oIMR\r\nContent-Disposition: form-data; name="redirect"\r\n\r\nhttps://www.gigab2b.com/index.php?route=common/home\r\n------WebKitFormBoundaryJVhdwreLurE0oIMR--\r\n'.format(
        csrf_token)
    response = requests.post(
        'https://www.gigab2b.com/index.php?route=account/login', data=data, headers=headers, cookies=complete_cookie)

    arg1 = re.findall("arg1='(.*?)'", response.text)[0]
    print(arg1)
    with open('./acw_sc__v2.js', 'r', encoding='utf-8') as f:
        acw_sc_v2_js = f.read()
    acw_sc__v2 = execjs.compile(acw_sc_v2_js).call('getAcwScV2', arg1)
    complete_cookie.update({"acw_sc__v2": acw_sc__v2})
    # 第二次访问首页，获取其他 cookies
    response2 = requests.get(
        url=index_url, headers=headers, cookies=complete_cookie)
    complete_cookie.update(response2.cookies.get_dict())


    return complete_cookie


def news_test(news_test_url, cookies):
    response = session.get(
        url=news_test_url, headers=headers, cookies=cookies)
    return response



from lxml import etree

from ParseGiGa import *
if __name__ == '__main__':
    all_links = []
    complete_cookie = get_complete_cookie()
    login(complete_cookie)
    news_test_url = "https://www.gigab2b.com/index.php?route=product/search&search=w679&page={}&limit=20"
    for page in range(1,10):
        url = news_test_url.format(page)
        # print(url)
        res = news_test(url, complete_cookie)
        html = etree.HTML(res.text)
        links = Parse_GiGa_href(html)
        all_links.extend(links)
    print(len(all_links))
