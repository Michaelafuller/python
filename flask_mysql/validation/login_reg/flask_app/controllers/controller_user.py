from flask import render_template, redirect, request, session, flash
from flask_app import app, bcrypt
from flask_app.models.model_user import User


@app.route("/")
def index():
    if 'uuid' in session:
        return redirect('/success')

    return render_template("index.html")
            

@app.route('/register/user', methods=['post'])
def register():
    if not User.validate_user(request.form):
        return redirect ('/')

    pw_hash = bcrypt.generate_password_hash(request.form['pw'])
    
    data = {
        **request.form,
        'pw' : pw_hash
    }

    user_id = User.create(data)
    
    session['uuid'] = user_id


    return redirect('/success')

@app.route('/success')
def success():
    if 'uuid' not in session:
        return redirect('/')

    return render_template('success.html')

@app.route('/login', methods=['post'])
def login():
    is_valid = User.validate_login(request.form)
    
    return redirect('/success')

# @app.route('/create', methods=['post'])
# def create():
#     data = {
#         'email': request.form['email'],
#         'pw' : request.form['pw']
#     }

#     User.create(data)

#     return redirect('/users')

@app.route('/logout')
def logout():
    del session['uuid']

    return redirect('/')

@app.route('/users')
def show_users():
    users = User.get_all()

    return render_template('/users.html', users=users)

@app.route('/users/<int:id>')
def show_one(id):
    data = {
        'id': id
    }
    user = User.get_one(data)

    return render_template('/users.html', user=user)

@app.route('/users/<int:id>/update')
def update_one(id):
    data = {
        'id' : id
    }
    
    user = User.get_one(data)

    return render_template('update.html', user=user)

@app.route('/update', methods=['post'])
def update():
    data = {
        'id' : request.form['id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    User.update_one(data)

    return redirect ('/users')

@app.route('/users/<int:id>/delete')
def delete_one(id):
    data = {
        'id' : id
    }

    User.delete_one(data)

    return redirect ('/users')
