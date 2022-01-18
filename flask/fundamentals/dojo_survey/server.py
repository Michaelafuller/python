from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['POST'])
def submit():
    if 'user' not in session:
        session['user'] = {
            **request.form
        }
    else:
        session['user'] = {
            **request.form
        }
    print(session['user'])

    return redirect('/user')

@app.route('/user')
def user_index():
    return render_template('user.html')

if __name__=="__main__":   
    app.run(debug=True)    