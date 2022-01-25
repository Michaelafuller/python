from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/createuser', methods=['post'])
def create_user():
    data = {
        'email' : request.form['email']
    }
    if not Email.validator(request.form):
        return redirect('/')

    Email.create_email(data)

    return redirect('/users')

@app.route('/users')
def show_users():
    users = Email.get_all_users()

    # if Email.validate_success(request.form):
    #     return render_template(success)

    return render_template('/users.html', users=users)

@app.route('/ninjas/<int:id>')
def show_one_ninja(id):
    data = {
        'id': id
    }
    ninja = Ninja.get_one(data)

    return render_template('/users.html', ninja=ninja)

@app.route('/ninjas/<int:id>/update')
def update_one_ninja(id):
    data = {
        'id' : id
    }
    
    ninja = Ninja.get_one(data)

    return render_template('update.html', ninja=ninja)

@app.route('/updateninja/<int:id>', methods=['post'])
def update_ninja(id):
    data = {
        'id' : id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }

    Ninja.update_one(data)

    return redirect ('/ninjas')

@app.route('/ninjas/<int:id>/delete')
def delete_one_ninja(id):
    data = {
        'id' : id
    }

    Ninja.delete_one(data)

    return redirect ('/ninjas')
