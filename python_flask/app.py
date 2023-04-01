from flask import Flask,render_template,request
import random

app=Flask(__name__)

# 抽奖参与者
participants=['张三','李四','王五','赵六','钱七']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw',methods=['POST'])
def draw():
    # 随机选取一人
    winner=random.choice(participants)
    # 返回中奖者名字
    return render_template('draw.html',winner=winner)


if __name__ == '__main__':
    app.run()