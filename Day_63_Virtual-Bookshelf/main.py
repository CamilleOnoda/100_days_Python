from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)


SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)
app.config['SECRET_KEY'] = SECRET_KEY

# Create new database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///virtual-bookshelf.db"
db = SQLAlchemy()
db.init_app(app)
# Create table model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
# Create table
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    books_list = db.session.execute(db.select(Book).order_by(Book.id)).scalars()
    return render_template('index.html', books_list=books_list)


@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == 'POST':
        new_book = Book(title=request.form["title"],author=request.form["author"],
                            rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

