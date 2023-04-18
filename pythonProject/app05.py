from flask import Flask,template_rendered


app = Flask(__name__)


@app.route('/')
def index():
    return template_rendered('index.html',title='Home Page')



if __name__ == '__main__':
    app.run(debug=True)