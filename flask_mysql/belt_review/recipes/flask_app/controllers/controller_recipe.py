from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_recipe import Recipe
from flask_app.models import model_recipe
from flask_app.controllers import controller_user


@app.route('/recipe/form')
def new_recipe():
    if 'uuid' not in session:
        return redirect('/')

    return render_template('/create.html')

@app.route('/recipes/create', methods=['post'])
def create_recipe():
    if 'uuid' not in session:
        return redirect('/')

    if not Recipe.validate_recipe(request.form):
        return redirect ('/dashboard')

    data = {
        **request.form,
        'user_id' : session['uuid']
    }

    Recipe.create(data)

    return redirect('/dashboard')

@app.route('/recipes/<int:id>/update')
def update_recipe(id):
    data = {
        'id' : id
    }
    
    edit_recipe = Recipe.get_one_recipe(data)

    return render_template('update.html', edit_recipe=edit_recipe)

@app.route('/recipes/<int:id>/delete')
def delete_one_recipe(id):
    data = {
        'id' : id
    }

    Recipe.delete_one(data)

    return redirect ('/dashboard')

@app.route('/recipes/update', methods=['post'])
def update_one_recipe():
    
    data = {
        **request.form,
        'id' : session['recipe']
            # 'name': request.form['name'],
            # 'description': request.form['description'],
            # 'instructions': request.form['instructions'],
            # 'under_half_hour' : request.form['under_half_hour']
        }

    Recipe.update_one(data)

    return redirect ('/dashboard')

@app.route('/recipes/<int:id>')
def show_one_recipe(id):
    data = {
        'id': id
    }
    if 'recipe' not in session:
        session['recipe'] = data['id']
    else:
        del session['recipe']
        session['recipe'] = data['id']

    recipe = Recipe.get_one_recipe(data)

    return render_template('/instructions.html', recipe=recipe)
