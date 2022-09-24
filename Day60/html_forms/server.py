from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def starter():
    return render_template("index.html")


@app.route('/login', methods=["POST", "GET"])
def done():
    if request.method=="POST":
        return f"<h1>Name: {request.form['fname']}, Password: {request.form['password']}</h1>"
    return "<p>You are logged in</p>"


if __name__ == "__main__":
    app.run(debug=True)
