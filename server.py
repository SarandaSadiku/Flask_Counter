from flask import Flask, render_template,request,redirect,session
app=Flask(__name__)
app.secret_key='secret'

@app.route('/')
def index():
    try:
        session['counter']
    except:
        session['counter']=0
    session['counter']+=1
    return render_template('index.html')

@app.route('/ninjas')
def addTwo():
    session['counter']+=1
    return redirect ('/')

@app.route('/reset')
def reset():
    session['counter']=0
    return redirect('/')

app.run(debug=True)
