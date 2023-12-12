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


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        return render_template('contact.html', name=name, message=message, message_sent=True)
    return render_template('contact.html', message_sent=False)


@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
