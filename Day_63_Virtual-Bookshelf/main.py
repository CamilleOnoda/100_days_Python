from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from sqlalchemy.ext.declarative import declarative_base
import os


app = Flask(__name__)
Bootstrap5(app)


SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)
app.config['SECRET_KEY'] = SECRET_KEY

# Create new database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///virtual-bookshelf.db"
db = SQLAlchemy()
db.init_app(app)

Base = declarative_base()

# Create a base model to support emoji (utf8mb4)
class BaseModel(Base):
    __tablename__ = 'virtual-bookshelf'
    __abstract__ = True
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }


# Create table model
class Book(BaseModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.String(250), nullable=False)

# Create table
with app.app_context():
    db.create_all()

# Flask routes
@app.route('/')
def home():
    books_list = list(db.session.execute(db.select(Book).order_by(Book.title)).scalars())
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