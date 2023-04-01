from flask import Flask,render_template,make_response
import random


app=Flask(__name__)

hero=['张三','李四','王五','赵六','钱七']
random_hero=random.choice(hero)

@app.route('/')
def index():
    response=make_response(render_template('index.html',hero=hero))
    response.headers['Cache-Control']='max-age=300'
    return response

@app.route('/draw')
def draw():
    h=random.choice(hero)
    return render_template('index.html',h=random_hero)


if __name__ == '__main__':
    app.run()