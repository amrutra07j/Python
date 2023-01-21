from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    # def __repr__(self):
    #     return f"{self.title}-{self.author}-{self.rating}"


all_books = []


@app.route('/')
def home():
    books = Book.query.all()
    return render_template('index.html', all_books=books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        db.create_all()

        new_book = Book(title=request.form.get('book'), author=request.form.get('author'), rating=request.form.get('rating'))
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit', methods=["POST", "GET"])
def edit():
    if request.method == "POST":
        id = request.form["id"]
        book_to_update = Book.query.get(id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_update = Book.query.filter_by(id=book_id).first()
    return render_template('edit.html', book=book_update)

@app.route('/delete')
def delete():
    book_id = Book.query.get(request.args.get('id'))
    db.session.delete(book_id)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
