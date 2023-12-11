from flask import Flask, render_template, request
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/c4d87a9e2fc58ee5b3a7"
response = requests.get(blog_url)
all_posts = response.json()

@app.route('/')
def index():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:index>')
def get_post(index):
    return render_template('post.html', posts=all_posts, id=index)


if __name__ == "__main__":
    app.run(debug=True)
