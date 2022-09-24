from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

Y_PASSWORD = "xmztmmahhsfnmboj"
G_EMAIL = "msdraj52@gmail.com"
Y_EMAIL = "udemyt07@yahoo.com"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        msg = f"""{request.form['name']},
                  {request.form['email']},
                  {request.form['phone']},
                  {request.form['message']}"""
        with smtplib.SMTP('smtp.mail.yahoo.com', port=587) as server:
            server.starttls()
            server.login(user=Y_EMAIL, password=Y_PASSWORD)
            server.sendmail(from_addr=Y_EMAIL, to_addrs=G_EMAIL, msg=f"Subject: `new user loogged in\n\n{msg}")
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
