from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Look ma, hot abcdedf!'

@app.route('/what')
def what_world():
    return 'What!'


if __name__ == "__main__":
    app.run(host='0.0.0.0')