from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja


@app.route("/")
def index():
    dojos = Dojo.get_all_dojo()

    return render_template("index.html", dojos=dojos)


@app.route('/createdojo', methods=['post'])
def create_dojo():
    data = {
        'name': request.form['name'],
    }

    Dojo.create_dojo(data)

    return redirect('/dojos')

@app.route('/dojos')
def show_dojos():
    dojos = Dojo.get_all_dojo()

    return render_template('/dojos.html', dojos=dojos)

@app.route('/dojos/<int:id>')
def show_one_dojo(id):
    data = {
        'id': id
    }
    dojos = Dojo.get_all_dojo()

    dojo_and_ninja = Dojo.get_dojo_with_ninja(data)

    return render_template('/dojos.html', dojo_and_ninja=dojo_and_ninja, dojos=dojos)

@app.route('/dojos/<int:id>/update')
def update_one_dojo(id):
    data = {
        'id' : id
    }
    
    dojo = Dojo.get_one_dojo(data)

    return render_template('update.html', dojo=dojo)

@app.route('/updatedojo/<int:id>', methods=['post'])
def update_dojo(id):
    data = {
        'id' : id,
        'name': request.form['name'],
    }

    Dojo.update_one_dojo(data)

    return redirect ('/dojos')

@app.route('/dojos/<int:id>/delete')
def delete_one_dojo(id):
    data = {
        'id' : id
    }

    Dojo.delete_one_dojo(data)

    return redirect ('/dojos')
