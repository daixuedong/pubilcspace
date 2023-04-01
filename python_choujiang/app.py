from flask import Flask,render_template
import random


app=Flask(__name__)

hero=['张三','李四','王五','赵六','钱七']

@app.route('/')
def index():
    return render_template('index.html',hero=hero)

@app.route('/draw')
def draw():
    random_hero=random.choice(hero)
    return render_template('index.html',hero=hero,h=random_hero)


if __name__ == '__main__':
    app.run()