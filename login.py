from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    num = 2
    num3 = 3
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)