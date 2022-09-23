import json

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def start():
    return "<h1>Enter your name to see magic</h1>"

@app.route('/<name>')
def assume(name):
    get_age = requests.get(f"https://api.agify.io/?name={name}")
    age = json.loads(get_age.text)['age']
    get_gender = requests.get(f"https://api.genderize.io/?name={name}")
    gender = json.loads(get_gender.text)['gender']
    return render_template('index.html', name=name, age=age, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)