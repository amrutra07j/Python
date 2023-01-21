from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import json

MOVIE_DB_API_KEY = "66c72400abe805149e9221c620312d21"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie_collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.String(250))
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(500), nullable=False)

class Editform(FlaskForm):
    rating = StringField("Your rating out of 10", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
    done = SubmitField("Done")

class Addform(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    submit_button = SubmitField("Add Movie")

@app.route("/")
def home():
    db.create_all()
    all_movies = Movie.query.order_by('rating').all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["POST", "GET"])
def edit():
    form = Editform()
    if form.validate_on_submit():
        movie_id = request.args.get('id')
        movie_record = Movie.query.get(movie_id)
        movie_record.rating = form.rating.data
        movie_record.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form)

@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_record = Movie.query.get(movie_id)
    db.session.delete(movie_record)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=["POST", "GET"])
def add():
    form = Addform()
    if form.validate_on_submit():
        movie_name = form.movie_title.data
        res_api = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_name})
        res_dict = res_api.json()['results']
        return render_template('select.html', result=res_dict)
    return render_template('add.html', form=form)

@app.route('/find')
def movie_details():
    movie_id = request.args.get('id')
    if movie_id:
        movie_info = requests.get(f"{MOVIE_DB_INFO_URL}/{movie_id}", params={"api_key": MOVIE_DB_API_KEY})
        data = movie_info.json()
        new_movie = Movie(
            title=data["title"],
            # The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}/{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        movie_id = Movie.query.filter_by(title=data["title"]).first().id
        return redirect(url_for('edit', id=movie_id))

if __name__ == '__main__':
    app.run(debug=True)
