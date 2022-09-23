from flask import Flask

app = Flask(__name__)

@app.route('/')
def start():
    return '<h1 style="text-align: center">Hello smart person</h1>' \
            '<p style="text-align: center">You are at the edge of the world!</p>' \
            '<img width=200, src="https://media3.giphy.com/media/nNQJkZcgc4V5kGfxIg/200.webp">'

@app.route('/<name>')
def greet(name):
    return f'Thanks for choosing us! {name} will be remembered'

if __name__ == "__main__":
    app.run(debug=True)