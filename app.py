from flask import Flask, render_template, request, session, jsonify

from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'my_secret_key'

client = MongoClient('db', 27017)
db = client.todoapp


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        todos = []
        for todo in db.todos.find():
            todos.append({
                'title': todo['title']
            })

        title = request.json['name']
        todo = {
            'title': title,
        }
        result = db.todos.insert_one(todo)
        todos.append(todo)
        return render_template('form.html', names=todos)
    else:
        todos = []
        for todo in db.todos.find():
            todos.append({
                'title': todo['title']
            })
        return render_template('form.html', names=todos)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 5001)