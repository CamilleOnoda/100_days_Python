from flask import Flask
import random

app = Flask(__name__)

correct_number = random.randint(0, 9)
print(correct_number)

@app.route('/')
def game():
    return "<div style='text-align: center'>"\
        "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>"\
        "<img style='display: block; margin: auto' src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"\
        "</div>"

@app.route('/<int:number>')
def guess_nb(number):
    if number == correct_number:
        return "<h1 style='text-align: center; color: orange'>You found me!</h1>"\
        "<img style='display: block; margin: auto' src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXlkZGozZWJ5dWJ1NWRydWE2YW8xamVwZmxkOTc0NzE5OGRuNzN4dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cXblnKXr2BQOaYnTni/giphy.gif'>"
    elif number < correct_number:
        return "<h1 style='text-align: center; color: green'>Too low! Try again!</h1>"\
        "<img style='display: block; margin: auto' src='https://media.giphy.com/media/ljtfkyTD3PIUZaKWRi/giphy.gif'>"
    elif number > correct_number:
        return "<h1 style='text-align: center; color: blue'>Too high! Try again!</h1>"\
        "<img style='display: block; margin: auto' src='https://media.giphy.com/media/BY8ORoRpnJDXeBNwxg/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
