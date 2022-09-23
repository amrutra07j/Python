from flask import Flask

app = Flask(__name__)

def make_bold(fun):
    def wrap():
        return f"""<b>{fun()}</b>"""
    return wrap

def make_under(fun):
    def wrap():
        return f"""<u>{fun()}</u>"""
    return wrap

@app.route('/')
@make_bold
@make_under
def start():
    return "You are the best"

if __name__ == "__main__":
    app.run(debug=True)