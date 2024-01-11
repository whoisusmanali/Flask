from flask import Flask

#WSGI
app = Flask(__name__)

@app.route('/')
def first():
    return "Hello! I am Usman Ali"

@app.route('/home')
def home():
    return "This is the Home Page"


if __name__ == '__main__':
    app.run(debug=True)