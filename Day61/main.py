import os
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "Great Secret"


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, max=30, message='Minmum password length should be 8')])
    submit = SubmitField(label='Log In')




@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)