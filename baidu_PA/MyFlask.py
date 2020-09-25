# encoding:utf-8
from flask import Flask, render_template, request
import requests
import base64
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():

	return render_template("login.html")


@app.route("/login", methods=['GET','POST'])
def login():
	# 接收文件

	request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"

	

	pic = request.files["pic_file"]
	# 此时，文件名保存为pic_file，问题待解决

	# pic_name = request.form.get("pic_name")

	# file_path = BASE_DIR + "/static/file/" + pic_name

	# 文件保存命名未解决

	pic_name  = pic.name
	
	pic.save(pic_name)

	# 二进制方式打开图片文件
	f = open(pic_name, 'rb')
	img = base64.b64encode(f.read())

	params = {"image":img}
	access_token = '24.fb5b1b9ae127d1e2f46fa9570d05e795.2592000.1603153209.282335-22705755'
	request_url = request_url + "?access_token=" + access_token
	headers = {'content-type': 'application/x-www-form-urlencoded'}
	response = requests.post(request_url, data=params, headers=headers)


	return render_template("login.html",msg=response.json(),name=pic_name)

if __name__ == '__main__':   # 固定写法。程序的入口
	# 启动一个flask项目应用程序 debug=True:不重启服务器即可更新
	app.run(debug=True)  


