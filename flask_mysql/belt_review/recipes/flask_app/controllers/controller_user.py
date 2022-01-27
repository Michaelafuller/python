from flask import render_template, redirect, request, session, flash
from flask_app import app, bcrypt
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe
from flask_app.controllers import controller_recipe


@app.route("/")
def index():
    if 'uuid' in session:
        return redirect('/dashboard')

    return render_template("index.html")
            

@app.route('/users/create', methods=['post'])
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


    return redirect('/dashboard')


@app.route('/dashboard')
def dasboard():
    if 'uuid' not in session:
        return redirect('/')

    data = {
        'id' : session['uuid']
    }
    user = User.get_one(data)
    recipe = Recipe.get_all()

    return render_template('dashboard.html', user=user, recipe=recipe)

@app.route('/login', methods=['post'])
def login():
    is_valid = User.validate_login(request.form)
    
    return redirect('/dashboard')

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

    return render_template('/dashboard.html', user=user)

@app.route('/users/<int:id>/update')
def update_one(id):
    data = {
        'id' : id
    }
    
    user = User.get_one(data)

    return render_template('update.html', user=user)

@app.route('/users/update', methods=['post'])
def update_one_user():
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
