from flask import Flask, render_template



# use the flask class to 
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')

# uses the first route
@app.route('/about')
def about():
    return render_template('about.html')
# can provide a veriable information
# needs a user name now

@app.route('/work')
def work():
    return render_template('work.html')

@app.route('/work/todo')
def todo():
    return render_template('/work/todo.html')

