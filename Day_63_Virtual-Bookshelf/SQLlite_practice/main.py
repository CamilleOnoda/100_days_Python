import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# Initialize extension (custom Base class for more complex structures)
#class Base(DeclarativeBase):
#    pass
#db = SQLAlchemy(model_class=Base)


# Create a new database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy()
db.init_app(app)

# Create a table Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

# Create the table
with app.app_context():
    db.create_all()

# Add object to the session
with app.app_context():
    new_book = Book(id=2,title='Courage to be disliked',author='Koga Fumitake and Ichiro Kishimi',rating=9)
    db.session.add(new_book)
    db.session.commit()










#db = sqlite3.connect("books-collection.db")
#cursor = db.cursor()

#cursor.execute("CREATE TABLE books "
#              "(id INTEGER PRIMARY KEY," 
#               "title varchar(250) NOT NULL UNIQUE, "
#               "author varchar(250) NOT NULL, "
#               "rating FLOAT NOT NULL)")

#cursor.execute("INSERT INTO books VALUES(1, 'The Courage to be disliked', "
#               "'Koga Fumitaka-Ichiro Kishimi',"
#               "'9.3')")
#db.commit()
#cursor.execute("INSERT INTO books VALUES(2, 'Harry Potter', 'J.K. Rowling', "
#               "'5')")
#db.commit()