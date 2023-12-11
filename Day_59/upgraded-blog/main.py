from flask import Flask, render_template, request
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/c4d87a9e2fc58ee5b3a7"
response = requests.get(blog_url)
all_posts = response.json()

@app.route('/')
def index():
    for blog_post in all_posts:
        id = blog_post['id']
        title = blog_post['title']
        subtitle = blog_post['subtitle']
        date = blog_post['date']
    return render_template("index.html", title=title, subtitle=subtitle, date=date,
                           id=id)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
