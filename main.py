import library as lib
from flask import Flask,render_template, request
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")
@app.route('/register', methods = ['POST'])
def register():
  if request.method == 'POST':
    user_name = request.form['user_id']
    user_password = request.form['password']
  lib.create_user(user_name, user_password)
  message = lib.login(user_name, user_password)
  return render_template("index.html", message=message)
@app.route('/login_visite', methods = ['GET'])
def login_visite():
  return render_template("log-in.html")


@app.route('/login', methods = ['POST'])
def login():
  if request.method == 'POST':
    user_name = request.form['user_id']
    user_password = request.form['password']
    lib.login(user_name, user_password)
    message = lib.login(user_name, user_password)
  return render_template("index.html", message=message)
 

if __name__ == '__main__':
  app.run(debug=True)