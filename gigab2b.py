# encoding='utf-8
# @Time: 2023-08-24
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests
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
datas = {
        'email':'larryerik14',
        'redirect':'https://www.gigab2b.com/index.php?route=common/home'
        }
home_url = 'https://www.gigab2b.com/'

session = requests.Session()
session.headers.update(headers)
resp = session.get(home_url)
# 用正则匹配 X-CSRF-TOKEN
# 使用正则表达式进行匹配
import re
pattern = r"window\.oriCsrfToken\.init\('X-CSRF-TOKEN', '([^']+)'\);"
match = re.search(pattern, resp.text)

# 如果匹配成功，则提取出字段内容
if match:
    csrf_token = match.group(1)
    print("匹配到的 X-CSRF-TOKEN 字段内容:", csrf_token)
else:
    print("未匹配到任何内容")

datas['X-CSRF-TOKEN'] = csrf_token



reponse = session.post('https://www.gigab2b.com/index.php?route=account/login',data=datas)
#
url = "https://www.gigab2b.com/index.php?route=product/channel/getChannelData&type=best_sellers"
rep = session.get(url)
with open('gigab2b.html','w',encoding='utf-8') as f:
    f.write(rep.text)
#  
#
