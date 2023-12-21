import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# Initialize extension
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

# Configure the extension
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

# Define Models
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

# Create the Table
with app.app_context():
    db.create_all()

# Add object to the session
with app.app_context():
    new_book = Book(id=1,title='Harry Potter',author='J.K. Rowling',rating=5.3)
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