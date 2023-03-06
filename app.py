from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongodb:27017/")
db = client.todoapp


@app.route('/', methods=['GET'])
def get_todos():
    with open('data/footer.txt') as file:
        footer = file.read()
    todos = []
    for todo in db.todos.find():
        todos.append(todo['title'])
    return render_template('form.html', names=todos, footer=footer)


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
    return redirect(url_for('get_todos'))


@app.route('/clear', methods=['POST'])
def execute():
    db.todos.delete_many({})
    return redirect(url_for('get_todos'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
