from flask import Flask, redirect, url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def firstpage():
    return render_template('index.html')


@app.route('/sucess/<int:score>')
def sucess(score):
    res = ""
    if score < 70:
        res = "Your Score " +str(score) + " is less than 70% that is why Prepare well next time and Pass the Exam"
    else:
        res = "Your Score " +str(score) + " is Greater than 70%. So, Congratulations you passes the exam"
    return render_template('result.html',result = res )




@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        math = float(request.form['maths'])
        datascience = float(request.form['datascience'])
        c = float(request.form['c'])
        total_marks = (science+math+datascience+c)/4

    return redirect(url_for('sucess', score=total_marks))
    

if __name__ == '__main__':
    app.run(debug=True)