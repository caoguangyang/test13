from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    num = 1
    return 'index3333'

if __name__ == '__main__':
    app.run(debug=True)