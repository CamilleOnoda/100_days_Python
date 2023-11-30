from flask import Flask, render_template
import random
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    date_time = date.today()
    year = date_time.year
    random_number = random.randint(1,10)
    return render_template("index.html", num=random_number, d=date_time, y=year)

@app.route('/guess/<name>')
def guess(name):
    return render_template("index.html", n=name)



if __name__ == "__main__":
    app.run(debug=True)
