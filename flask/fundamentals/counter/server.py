from itertools import count
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'  

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1

    return render_template('index.html')

@app.route('/counter', methods=['POST'])
def counter():
    session['counter'] += 1
    print(session['counter'])

    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def reset():
    session['counter'] = 1

    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    