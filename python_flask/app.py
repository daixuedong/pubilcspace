# 导入flask
from flask import Flask,render_template


app=Flask(__name__)

@app.route('/index')
def index():
    return "dai"


if __name__=='__main__':
    app.run(debug=True)