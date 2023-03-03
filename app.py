from flask import Flask, request, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("127.0.0.1",27017)
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
        todos.append(todo['title'])
    title = request.form['name']
    todo = {
        'title': title,
    }
    result = db.todos.insert_one(todo)
    todos.append(title)
    return render_template('form.html', names=todos)

@app.route('/clear', methods=['POST'])
def execute():
    db.todos.delete_many({})
    return "Todo-List has been cleared"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
