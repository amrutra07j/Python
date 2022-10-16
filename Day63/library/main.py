from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    db = sqlite3.connect('fav_books.db')
    cursor = db.cursor()
    all_books = cursor.execute("select * from books").fetchall()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        db = sqlite3.connect('fav_books.db')
        cursor = db.cursor()
        id = cursor.execute("select max(id) from books").fetchall()[0][0]
        id = 1 if id == None else id+1
        try:
            if request.form["author"] and request.form["rating"]:
                cursor.execute(
                    f'INSERT INTO books VALUES({id}, "{request.form["title"]}", "{request.form["author"]}", "{request.form["rating"]}")')
                db.commit()
                return redirect(url_for('home'))
            elif not request.form["author"]:
                return "<p>Must Provide author name </p>"
            else:
                return "<p>Must provide rating</p>"
        except Exception as e:
            if str(e).endswith('title'):
                return '<p>Book is already present in shelf</p>'
            else:
                return f'{e}'

    return render_template('add.html')


@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        id = request.form['id']
        db = sqlite3.connect('fav_books.db')
        cursor = db.cursor()
        cursor.execute(f'update books set rating={request.form["change_rating"]} where id={id}')
        db.commit()
        return redirect(url_for('home'))
    db = sqlite3.connect('fav_books.db')
    cursor = db.cursor()
    book_id = request.args.get('id')
    book_selected = cursor.execute(f'select * from books where id={book_id}').fetchall()[0]
    return render_template('edit_rating.html', book=book_selected)


@app.route('/delete')
def delete():
    id = request.args.get('id')
    db = sqlite3.connect('fav_books.db')
    cursor = db.cursor()
    cursor.execute(f'DELETE FROM books WHERE id={id}')
    db.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
