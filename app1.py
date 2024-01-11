from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def firstpage():
    return "Welcome to my application"

@app.route('/fail/<int:score>')
def fail(score):
    return "Your Score " +str(score) + " is less than 70% that is why Prepare well next time and Pass the Exam"

@app.route('/sucess/<int:score>')
def sucess(score):
    return "Your Score " +str(score) + " is Greater than 70%. So, Congratulations you passes the exam"

@app.route('/results/<int:score>')
def results(score):
    result = ""
    if score<70:
        result = "fail"
    else:
        result = "sucess"
    return redirect(url_for(result, score=score))

if __name__ == '__main__':
    app.run(debug=True)