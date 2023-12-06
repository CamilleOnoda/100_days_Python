from flask import Flask, render_template
import requests


app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()


@app.route('/')
def blog():
    return render_template("index.html", posts=all_posts)


@app.route('/blog/<int:index>')
def get_post(index):
    return render_template("post.html", posts=all_posts, id=index)


if __name__ == "__main__":
    app.run(debug=True)
