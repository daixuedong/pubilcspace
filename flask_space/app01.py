from flask import Flask,render_template,request

# 创建一个Flask应用实例
app=Flask(__name__)


hello="hello,World!"
h="This is an about page"
# 定义路由
@app.route('/')
def home():
    return render_template('hello.html',hello=hello)

@app.route('/about')
def about():
    return render_template("hello.html",hello=h)

@app.route('/contact',methods=["GET","POST"])
def contact():
    if request.method=="POST":
        name=request.form.get('name')
        email=request.form.get('email')
        message=request.form.get('message')
        # 保存联系表数据或发送电子邮件等操作
        return f"Thank you for contacting us,{name}!"
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)