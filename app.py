from flask import Flask, url_for, redirect, request, render_template
# first program:
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello world"

#variables:
@app.route('/login/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

#url_for, redirect
@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))
  
#post, get
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
  
#render_template
@app.route('/index')
def index():
   return render_template('app.html')

#

if __name__ == '__main__' :
    app.run(debug = True)



