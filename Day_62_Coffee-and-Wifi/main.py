from enum import unique
from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Nullable
from sqlalchemy.ext.declarative import declarative_base
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import os


app = Flask(__name__)
Bootstrap5(app)

SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)
app.config['SECRET_KEY'] = SECRET_KEY

#Create new database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///coffee-wifi.db"
db = SQLAlchemy()
db.init_app(app)

Base = declarative_base()

# Create a base model
class BaseModel(Base):
    __abstract__ = True
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }

# Create table model
class CafeForm(BaseModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cafe = db.Column(db.String(250), unique=True, nullable=False)
    city = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), unique=True, nullable=False)
    open_hours = db.Column(db.String(250), nullable=False )
    closed = db.Column(db.String(250), nullable=False)
    sweet = db.Column(db.String(250), nullable=False)
    coffee = db.Column(db.String(250), nullable=False)
    wifi = db.Column(db.String(250), nullable=False)
    power = db.Column(db.String(250), nullable=False)

#    closed = SelectMultipleField('Closing days', choices=[('Open everyday','Open everyday'),
#                                                          ('Monday','Monday'),
#                                                          ('Tuesday','Tuesday'),
#                                                          ('Wednesday','Wednesday'),
#                                                          ('Thursday','Thursday'),
#                                                          ('Friday','Friday'), 
#                                                          ('Saturday','Saturday'),
#                                                          ('Sunday','Sunday')],
#                                                          )
#    sweet = SelectField('Food rating', choices=['🍩','🍩🍩','🍩🍩🍩',
#                                                   '🍩🍩🍩🍩','🍩🍩🍩🍩🍩'], 
#                                                   )
#    coffee = SelectField('Coffee rating', choices=['☕','☕☕','☕☕☕',
#                                                   '☕☕☕☕','☕☕☕☕☕'], 
#                                                   )
#    wifi = SelectField('Wifi strength rating', choices=['✘','💪','💪💪','💪💪💪',
#                                                   '💪💪💪💪','💪💪💪💪💪'], 
#                                                   )
#   power = SelectField('Power socket availability', choices=['✘','🔌','🔌🔌','🔌🔌🔌',
#                                                   '🔌🔌🔌🔌','🔌🔌🔌🔌🔌'], 
#                                                   )
#    submit = SubmitField('Submit')
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    closed_days = ' & '.join(list(form.closed.data or []))
    if form.validate_on_submit():
        with open('cafe-data.csv', mode='a', encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.city.data},"
                           f"{form.location.data},"
                           f"{form.open_hours.data},"
                           f"{closed_days},"
                           f"{form.sweet.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power.data}")
            return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
