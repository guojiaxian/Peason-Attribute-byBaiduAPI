
# encoding:utf-8
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【Wo6j2hyHHeC9TeVOEsXhevdg】&client_secret=【cTr4bsSqEHG794A4etaq32ClVkUcjk36】'
response = requests.get(host)
if response:
    print(response.json())
    