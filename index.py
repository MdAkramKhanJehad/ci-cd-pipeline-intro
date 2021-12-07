from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {
        'Message': 'Hello Bro!',
    }

@app.route('/multi/<a>/<b>')
def multi_route(a, b):
    return {
        'Multi result': multi(a, b)
    }


def mssulti(a,b):
    if type(a) == str and not a.isdigit():
        return "Invalid Input"

    if type(b) == str and not b.isdigit():
        return "Invalid Input"

    a = int(a)
    b = int(b)
    return a * b


if __name__ == "__main__":
    app.run()








