import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = posts.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)