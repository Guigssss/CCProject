from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return request.form['name']
    else:
        return render_template('form.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 5001)