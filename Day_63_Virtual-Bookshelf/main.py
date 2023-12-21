from ast import Str
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import os


app = Flask(__name__)
Bootstrap5(app)


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

# Flask form
class Bookform(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])

# Flask routes
@app.route('/')
def home():
    books_list = list(db.session.execute(db.select(Book).order_by(Book.id)).scalars())
    return render_template('index.html', books_list=books_list)


@app.route("/add", methods=['GET','POST'])
def add():
    form = Bookform()
    if form.validate_on_submit():
        new_book = Book(title=form.title.data,author=form.author.data,
                            rating=form.rating.data)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route("/edit", methods=['GET','POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html",book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

