from flask import Flask

app = Flask(__name__)

@app.route('/')
def guess_nb():
    return "<div style='text-align: center'>"\
        "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>"\
        "<img style='display: block; margin: auto' src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"\
        "</div>"