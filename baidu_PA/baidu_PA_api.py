# encoding:utf-8

import requests
import base64

'''
人体检测和属性识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"

# 二进制方式打开图片文件

pic_name = input("please input the picname:")
f = open(pic_name, 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.fb5b1b9ae127d1e2f46fa9570d05e795.2592000.1603153209.282335-22705755'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())