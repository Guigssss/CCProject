from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongodb:27017/")
db = client.todoapp


@app.route('/', methods=['GET'])
def get_todos():
    todos = []
    for todo in db.todos.find():
        todos.append(todo['title'])
    return render_template('form.html', names=todos)


@app.route('/', methods=['POST'])
def create_todo():
    todos = []
    for todo in db.todos.find():
        todos.append({
            'title': todo['title']
        })
    title = request.form['name']
    todo = {
        'title': title,
    }
    result = db.todos.insert_one(todo)
    todos.append(todo)
    return render_template('form.html', names=todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
