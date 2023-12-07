from flask import Flask, render_template, request
import random
from datetime import date
import requests

app = Flask(__name__)

#@app.route('/')
#def home():
#    date_time = date.today()
#    year = date_time.year
#    random_number = random.randint(1,10)
#    return render_template("index.html", num=random_number, d=date_time, y=year)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/guess', methods=["GET","POST"])
def guess():
    name = request.form.get("name", "world")
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_response.raise_for_status()
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)


#@app.route('/blog')
#def blog():
#    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
#    response = requests.get(blog_url)
#    all_posts = response.json()
#    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
