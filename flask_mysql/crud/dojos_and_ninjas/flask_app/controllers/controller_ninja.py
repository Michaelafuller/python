from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_ninja import Ninja
from flask_app.models.model_dojo import Dojo

            

@app.route('/createninja', methods=['post'])
def create_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id' : request.form['dojo_id']
    }

    Ninja.create_ninja(data)

    return redirect('/dojos')

@app.route('/ninjas')
def show_ninjas():
    dojos = Dojo.get_all_dojo()

    return render_template('/ninjas.html', dojos=dojos)

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
