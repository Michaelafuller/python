from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_ import 

@app.route("/")
def index():
    return render_template("index.html")
            

@app.route('/create', methods=['post'])
def create():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    .create(data)

    return redirect('/')

@app.route('/users')
def get_all():
    users = .get_all()

    return render_template('users.html', users=users)

@app.route('/users/<int:id>')
def show_one(id):
    data = {
        'id': id
    }
    user = .get_one(data)

    return render_template('users.html', user=user)

@app.route('/users/<int:id>/update')
def update_one(id):
    data = {
        'id' : id
    }
    
    user = .get_one(data)

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
