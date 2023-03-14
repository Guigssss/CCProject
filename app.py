from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId

#Create a Flask App
app = Flask(__name__)

#Create connexion with Mongo Database
client = MongoClient("mongodb://mongodb:27017/")

db = client.todoapp

#Route / get : Main page that show every elements in the Mongo DB
@app.route('/', methods=['GET'])
def get_todos():
    #Get the copyright from the bind
    with open('data/footer.txt') as file:
        footer = file.read()
    todos = []
    #Get all elements inside Mongo DB
    for todo in db.todos.find():
        todos.append(todo)
    return render_template('form.html', names=todos, footer=footer)

#Route / post : Add element to the todolist
@app.route('/', methods=['POST'])
def create_todo():
    #Get value from form
    title = request.form['name']
    todo = {
        'title': title,
        'checked': False  # Add a new field to the document to store the checked value.
    }
    #Add the elements inside Mongo DB with unchecked by default
    result = db.todos.insert_one(todo)
    return redirect(url_for('get_todos'))

#Route /update post : Check or uncheck elements
@app.route('/update', methods=['POST'])
def update_todo():
    # Get value from form
    todo = request.form['todo']
    title = eval(todo, {'ObjectId': ObjectId})
    checked = request.form['checked'] == 'true'
    # Modify the elements inside Mongo DB with unchecked or check value depending on current situation
    db.todos.update_one({'title': title["title"]}, {'$set': {'checked': checked}})
    return 'success'

#Route /clear post : Delete every elements inside the list
@app.route('/clear', methods=['POST'])
def execute():
    # Delete all elements inside MongoDB
    db.todos.delete_many({})
    return redirect(url_for('get_todos'))

#Run Flask (access through 5001 port)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
