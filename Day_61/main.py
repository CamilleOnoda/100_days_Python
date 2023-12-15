from flask import Flask, redirect, render_template, request
from flask_wtf import FlaskForm
import os
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from itsdangerous.serializer import Serializer


app = Flask(__name__)

SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)
app.config['SECRET_KEY'] = SECRET_KEY


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In', validators=[DataRequired()])


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
