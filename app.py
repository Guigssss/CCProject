from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

#client = MongoClient("mongodb://mongodb:27017/")
client = MongoClient("localhost:27017")
db = client.todoapp


@app.route('/', methods=['GET'])
def get_todos():
    with open('data/footer.txt') as file:
        footer = file.read()
    todos = []
    for todo in db.todos.find():
        todos.append(todo)
    return render_template('form.html', names=todos, footer=footer)


@app.route('/', methods=['POST'])
def create_todo():
    title = request.form['name']
    todo = {
        'title': title,
        'checked': False  # Add a new field to the document to store the checked value.
    }
    result = db.todos.insert_one(todo)
    return redirect(url_for('get_todos'))

@app.route('/update', methods=['POST'])
def update_todo():
    todo = request.form['todo']
    title = eval(todo, {'ObjectId': ObjectId})
    checked = request.form['checked'] == 'true'
    db.todos.update_one({'title': title["title"]}, {'$set': {'checked': checked}})
    return 'success'




@app.route('/clear', methods=['POST'])
def execute():
    db.todos.delete_many({})
    return redirect(url_for('get_todos'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
