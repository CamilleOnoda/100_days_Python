from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import os


app = Flask(__name__)
Bootstrap5(app)

SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)
app.config['SECRET_KEY'] = SECRET_KEY


class CafeForm(FlaskForm):
    cafe = StringField('Cafe', validators=[DataRequired()])
    city = StringField('City/Prefecture', validators=[DataRequired()])
    location = StringField('Location on Google Map (URL)', validators=[URL()])
    open_hours = StringField('Opening hours (e.g.: 8AM - 5PM)', validators=[DataRequired()])
    closed = StringField('Closing days', validators=[DataRequired()])
    coffee = SelectField('Coffee rating', choices=['☕','☕☕','☕☕☕',
                                                   '☕☕☕☕','☕☕☕☕☕'], 
                                                   validators=[DataRequired()])
    wifi = SelectField('Wifi strength rating', choices=['❌','💪','💪💪','💪💪💪',
                                                   '💪💪💪💪','💪💪💪💪💪'], 
                                                   validators=[DataRequired()])
    power = SelectField('Power socket availability', choices=['❌','🔌','🔌🔌','🔌🔌🔌',
                                                   '🔌🔌🔌🔌','🔌🔌🔌🔌🔌'], 
                                                   validators=[DataRequired()])
    submit = SubmitField('Submit', )


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', mode='a', encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open_hours.data},"
                           f"{form.closed.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power.data}")
            return redirect(url_for('cafes'))
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
