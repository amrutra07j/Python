from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def starter():
    return render_template('index.html')
@app.route('/land')
def lander():
    return render_template('landing.html')

if __name__ == "__main__":
    app.run(debug=True)