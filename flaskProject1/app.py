from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('./templates/home.html') 

# @app.route('/user/<name>')
# def user(name):  # put application's code here
#     return '<h1>Hello, {}!</h1>'.format(name) 

if __name__ == '__main__':
    # app.run()
    app.run()
