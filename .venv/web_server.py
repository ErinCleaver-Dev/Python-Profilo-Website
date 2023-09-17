from flask import Flask, render_template, request, url_for, flash, redirect
from server.mongodb import database
from bson import ObjectId
import server.fb as fb







# use the flask class to 
app = Flask(__name__)
login = False

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/<number>')
def blog():
    return render_template('blog.html')


@app.route('/blog/<number><post>')
def blog_post(number, post):
    return render_template('post.html')

@app.route('/blog/create_post')
def blog_post():
    return render_template('create_post', login)


@app.route('/work')
def work():
    return render_template('work.html', login)

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
@app.route('/work/todo', methods=['POST', 'GET'])
def todo():
    try:
        todo_db = database().todo
        if request.method == 'POST':
            item = request.form['todo']
            todo_db.insert_one({'text': item, 'complete': False})

        
    except Exception as e:
        print(e)

    todo_list = todo_db.find()
    return render_template('/work/todo.html', todo_list = todo_list)

@app.route('/complete/<oid>')
def complete(oid):
    print(oid)
    todo_db = database().todo
    print()
    item = todo_db.find_one({"_id":  ObjectId(oid)})['complete']

    if(item):
        item = False
    else: 
        item = True

    todo_db.update_one({'_id': ObjectId(oid)}, {'$set': {'complete': item}})
    return redirect('/work/todo')


@app.route('/delete_complated')
def delete_complated():
    todo_db = database().todo
    todo_db.delete_many({"complete": True})
    return redirect('/work/todo')


@app.route('/delete_all')
def delete_all():
    todo_db = database().todo
    todo_db.delete_many({})
    return redirect('/work/todo')
