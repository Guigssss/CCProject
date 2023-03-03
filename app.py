from flask import Flask, render_template, request, session, jsonify

from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'my_secret_key'

client = MongoClient('db', 27017)
db = client.todoapp


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        names = session.get('names', [])
        names.append(name)
        session['names'] = names
        return render_template('form.html', names=names)
    else:
        return render_template('form.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 5001)