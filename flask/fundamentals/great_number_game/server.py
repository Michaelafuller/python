import random
from flask import Flask, render_template, request, redirect, session
from markupsafe import re
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'  



@app.route('/')
def index():
    if 'random' not in session:
        session['random'] = random.randint(1,100)

    print(session['random'])

    return render_template('index.html')



@app.route('/guess', methods=['POST'])
def guess_num():
    session['guess'] = int(request.form['input'])
    print(session['guess'])
    # if int(request.form['input']) > session['random']:
    #     print('too high')
    #     guess = 'too high'

    # elif int(request.form['input']) < session['random']:
    #     print('too low')
    #     guess = 'too low'

    # else:
    #     print('You guessed it!')
    #     guess = 'just right'

    # this is me trying to keep logic out of the HTML. Like the platform suggests. I cannot get it to work.
    
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    if 'random' in session:
        session['random'] = random.randint(1,100)
    print(session['random'])

    if 'guess' in session:
        session.pop('guess')

    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    