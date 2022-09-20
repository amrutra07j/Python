import requests
from flask import Flask, render_template

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts: object = posts.json()


@app.route('/')
def get_blog():
    return render_template('index.html', posts=all_posts)


@app.route('/post/<int:num>')
def show_post(num):
    send_post = None
    for single_post in all_posts:
        if single_post['id'] == num:
            print(single_post)
            send_post = single_post
    return render_template("post.html", post=send_post)


if __name__ == "__main__":
    app.run(debug=True)
