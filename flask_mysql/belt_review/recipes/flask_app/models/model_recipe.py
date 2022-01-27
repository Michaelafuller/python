DATABASE = 'recipes_schema'
from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.under_half_hour = data['under_half_hour']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create(cls, data):
        query = 'INSERT INTO recipes (name, description, under_half_hour, instructions, user_id) VALUES ( %(name)s, %(description)s, %(under_half_hour)s, %(instructions)s, %(user_id)s );'
        
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)

        recipes = []
        for x in results:
            recipes.append( cls(x) )

        return recipes

    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        return cls(results[0])

    @classmethod
    def update_one(cls, data):
        query = "UPDATE recipes SET name=%(name)s, under_half_hour=%(under_half_hour)s, description=%(description)s, instructions=%(instructions)s WHERE id = %(id)s;"

        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"

        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one_by_name(cls, data):
        query = 'SELECT * FROM recipes WHERE name = %(name)s;'

        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @staticmethod
    def validate_recipe(data):
        is_valid = True

        recipe = Recipe.get_one_by_name(data)
        if recipe:
            flash('A recipe by this name already exists! If you think yours is better, try another name.')
            is_valid = False

        return is_valid

