from flask import Flask, render_template, request
# render_template用作返回html页面 request:页面发来的请求
# hello world
# 创建应用程序
# web应用程序
app = Flask(__name__)

# 写一个函数来处理浏览器的请求
# 路由：通过浏览器访问过来的请求到底交给谁处理

# #---------------------------------------------------------------#
# @app.route("/")  # 路由，当访问到127.0.0.1：5000/时，默认执行下列函数
# def index():
# 	return "hello, my name is Sai Liya"    # 返回数据--响应
# #---------------------------------------------------------------#

# @app.route("/jay")
# def Jay():
# 	return "I love Jay Chou"
# #---------------------------------------------------------------#

# # 引入html
# @app.route("/html1")
# def Chou():
# 	return render_template("hello.html")  # 自动找templates里的html
# #---------------------------------------------------------------#

# # 把变量发送到页面
# @app.route("/html2")
# def html2():
# 	# 字符串
# 	s = "My name is Guo Jiaxian"

# 	# 列表
# 	lst = ["郭嘉贤","崔圆圆","陈怡钒","刘老师"]
# 	return render_template("hello.html", j=s, lst = lst)  # 自动找templates里的html
# #---------------------------------------------------------------#

# 从页面接受数据，登录
@app.route("/")
def index():

	return render_template("login.html")
 
@app.route("/login", methods=['POST'])
def login():
	# 接收用户名和密码  <!-- {username:gjx pwd:123} -->
	username = request.form.get("username")
	password = request.form.get("pwd")
	if username == "gjx" and password=="123":
		return "成功"
	else:
		return render_template("login.html",msg="登陆失败")


if __name__ == '__main__':   # 固定写法。程序的入口
	# 启动一个flask项目应用程序 debug=True:不重启服务器即可更新
	app.run(debug=True)  


