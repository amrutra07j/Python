from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def start():
    return '<h1>Guess the number between 0 and 9</h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:num>')
def guess(num):
    gen_num = random.randint(0, 9)
    if int(num) == gen_num:
        return '<h1 style="color:green">You found me!</h1>' \
                '<img width=400, src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif int(num) > gen_num:
        return '<h1 style="color:red">Too high</h1>' \
                '<img width=400, src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    if int(num) < gen_num:
        return '<h1 style="color:blue">Too Low</h1>' \
                '<img width=400, src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)