from flask import Flask, render_template



# use the flask class to 
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/work')
def work():
    return render_template('work.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
@app.route('/work/todo')
def todo():
    return render_template('/work/todo.html')

