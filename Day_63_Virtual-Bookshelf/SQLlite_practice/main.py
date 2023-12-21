import sqlite3

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

#cursor.execute("CREATE TABLE books "
#              "(id INTEGER PRIMARY KEY," 
#               "title varchar(250) NOT NULL UNIQUE, "
#               "author varchar(250) NOT NULL, "
#               "rating FLOAT NOT NULL)")

#cursor.execute("INSERT INTO books VALUES(1, 'The Courage to be disliked', "
#               "'Koga Fumitaka-Ichiro Kishimi',"
#               "'9.3')")
#db.commit()
cursor.execute("INSERT INTO books VALUES(2, 'Harry Potter', 'J.K. Rowling', "
               "'5')")
db.commit()