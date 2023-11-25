from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>" +function() + "</em>"
    return wrapper
    
def make_underline(function):
    def wrapper():
        return f"<u>" +function() + "</u>"
    return wrapper

@app.route('/')
@make_bold
@make_emphasis
@make_underline
def hello_world():
    return'Hello, World!'

@app.route('/bye')
def bye():
    return"Ok, Bye!"

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name.capitalize()}! How are you today? You have the number: {number}"


if __name__ == "__main__":
    app.run(debug=True)
