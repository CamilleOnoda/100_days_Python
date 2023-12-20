from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == 'POST':
        return render_template('index.html', title=request.form.get("title"), 
                               author=request.form.get("author"), 
                               rating=request.form.get("rating"))
    elif request.method == 'GET':
        return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

