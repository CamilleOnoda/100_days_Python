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

# Read all records
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()

# Read a particular record by Query
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == 'Courage to be disliked')).scalar()
    print(book)

# Update a particular record by query
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter and the Chamber of Secrets")).scalar()
    book_to_update.title = "Harry Potter"
    book_to_update.rating = 3
    db.session.commit()


# Update a record by primary key
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()
    

# get_or_404() query method // returns None as the row with the given id doesn't exist
book_id = 3
with app.app_context():
    book = db.get_or_404(Book, book_id)
    

# Delete a particular record by primary key
book_id = 1
with app.app_context():
    #book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
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