# flask blog
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')
    
# @app.route('/signin', methods=['POST'])    
# def signin():
#     # 需要从request对象读取表单内容：
#     if request.form['username']=='admin' and request.form['password']=='password':
#         return '<h3>Hello, admin!</h3>'
#     return '<h3>Bad username or password.</h3>'

@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/user/<username>')
def user(username):
    return 'hello %s' % username

@app.route('/projects/')
def projects():
    return 'The project page'

# 404重定向
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


# url_for('static', filename='style.css')

if __name__ == '__main__':
    app.run(debug=True)