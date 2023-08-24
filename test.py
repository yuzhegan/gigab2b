# encoding='utf-8
# @Time: 2023-08-24
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests
from parse import *
cookies = {
    'OCSESSID': '71f49995897288bfdf695dbfa1',
    '_ayo': 'cefae265ec5bf351ca39a65245a3f250',
    'country': 'USA',
    'currency': 'USD',
    'uuid_402613e0-f191-11e9-9a99-ab9f77aaeb99': 'f0586521-6a15-4d65-aec5-0582b6129949',
    'href': 'https%3A%2F%2Fwww.gigab2b.com%2Findex.php',
    '_pk_id.2.185c': 'a504ccc5c3dca094.1692845917.',
    'hubspotutk': 'da4f0d0c7d280f672d58950492a8c145',
    '__hssrc': '1',
    '__hs_opt_out': 'no',
    '__hs_initial_opt_in': 'true',
    'is_partner': '0',
    'login_flag': '',
    '_pk_ses.2.185c': '1',
    'qimo_seosource_0': '%E7%AB%99%E5%86%85',
    'qimo_seokeywords_0': '',
    'qimo_seosource_402613e0-f191-11e9-9a99-ab9f77aaeb99': '%E7%AB%99%E5%86%85',
    'qimo_seokeywords_402613e0-f191-11e9-9a99-ab9f77aaeb99': '',
    'qimo_xstKeywords_402613e0-f191-11e9-9a99-ab9f77aaeb99': '',
    '__hstc': '114550104.da4f0d0c7d280f672d58950492a8c145.1692845936803.1692864593846.1692868017364.3',
    'uuid_d2dd0510-3509-11eb-96fd-2f35d7dbffa2': '3c6e8e3a-8040-4cf2-9230-e3d3367bd091',
    'qimo_seosource_d2dd0510-3509-11eb-96fd-2f35d7dbffa2': '%E7%AB%99%E5%86%85',
    'qimo_seokeywords_d2dd0510-3509-11eb-96fd-2f35d7dbffa2': '',
    'qimo_xstKeywords_d2dd0510-3509-11eb-96fd-2f35d7dbffa2': '',
    'uuid_52bf0b60-3506-11eb-89bd-fba0225c9608': 'ddadf56a-4a00-435b-8ff6-80fdd21ecadc',
    'qimo_seosource_52bf0b60-3506-11eb-89bd-fba0225c9608': '%E7%AB%99%E5%86%85',
    'qimo_seokeywords_52bf0b60-3506-11eb-89bd-fba0225c9608': '',
    'qimo_xstKeywords_52bf0b60-3506-11eb-89bd-fba0225c9608': '',
    'acw_tc': '0bc1a05716928699167547489e98792565ef0f32e487c4228aad74c15584e3',
    'accessId': '402613e0-f191-11e9-9a99-ab9f77aaeb99',
    'acw_sc__v2': '64e725278251167e4c304c8809b47c4012c6f120',
    'pageViewNum': '87',
    '__hssc': '114550104.28.1692868017364',
    # 'SERVERID': 'dd0c4118f961197a4a442c72d58d69d5|1692870594|1692867991',
    # 'SERVERCORSID': 'dd0c4118f961197a4a442c72d58d69d5|1692870594|1692867991',
}
import time
import random
timestamp = int(time.time())
timestamp_hou = timestamp + random.randint(2500, 4000)
str_Server = 'dd0c4118f961197a4a442c72d58d69d5|'+ str(timestamp_hou)+'|'+ str(timestamp)
cookies['SERVERID'] = str_Server
cookies['SERVERCORSID'] = str_Server
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
home_url = 'https://www.gigab2b.com/'
session = requests.Session()
session.headers.update(headers)
session.cookies.update(cookies)
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
data = '------WebKitFormBoundaryJVhdwreLurE0oIMR\r\nContent-Disposition: form-data; name="X-CSRF-TOKEN"\r\n\r\n{}\r\n------WebKitFormBoundaryJVhdwreLurE0oIMR\r\nContent-Disposition: form-data; name="email"\r\n\r\nlarryerik14@gmail.com\r\n------WebKitFormBoundaryJVhdwreLurE0oIMR\r\nContent-Disposition: form-data; name="password"\r\n\r\nlarryerik14\r\n------WebKitFormBoundaryJVhdwreLurE0oIMR\r\nContent-Disposition: form-data; name="redirect"\r\n\r\nhttps://www.gigab2b.com/index.php?route=common/home\r\n------WebKitFormBoundaryJVhdwreLurE0oIMR--\r\n'.format(csrf_token)
response = session.post('https://www.gigab2b.com/index.php?route=account/login',data=data)


# from lxml import etree
# links = []
# for page in range(1,21):
#     url = "https://www.gigab2b.com/index.php?route=product/search&search=w679&page={}&limit=20".format(page)
#     print(url)
#     rep = session.get(url)
#     content = etree.HTML(rep.text)
#     hrefs = Parse_href(content)
#     links.extend(hrefs)
# print(len(links))
    
# headers['Referer'] = url

timestamp = int(time.time())
timestamp_hou = timestamp + random.randint(2500, 4000)
str_Server = 'dd0c4118f961197a4a442c72d58d69d5|'+ str(timestamp_hou)+'|'+ str(timestamp)
cookies['SERVERID'] = str_Server
cookies['SERVERCORSID'] = str_Server
session.cookies.update(cookies)


url_search = "https://www.gigab2b.com/index.php?route=product/search&search=w679"
rep = session.post(url_search)
with open('gigab2b_w679.html','w',encoding='utf-8') as f:
    f.write(rep.text)
# print(rep.text)
