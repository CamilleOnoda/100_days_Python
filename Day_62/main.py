from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import os


app = Flask(__name__)
SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[URL()])
    open_hours = StringField('Opening hours', validators=[DataRequired()])
    closed = StringField('Closed', validators=[DataRequired()])
    coffee = SelectField('Coffee rating', choices=['☕','☕☕','☕☕☕',
                                                   '☕☕☕☕','☕☕☕☕☕'])
    wifi = SelectField('Wifi strength rating', choices=['💪','💪💪','💪💪💪',
                                                   '💪💪💪💪','💪💪💪💪💪'])
    power = SelectField('Power socket availability', choices=['🔌','🔌🔌','🔌🔌🔌',
                                                   '🔌🔌🔌🔌','🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit', )


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
