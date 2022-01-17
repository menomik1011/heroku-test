import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return 'Hello, World!'

@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'username: {user_name}\n userid: {user_id} !'

@app.route('/api',methods=['POST'])
def post():
    id = request.form['id']
    pw = request.form['pw']
    # msg = "%s 님 안녕! " %value
    return f"<p>{id}</p><br/><p>{pw}</p>"


if __name__ == '__main__':
    app.run(debug=True)