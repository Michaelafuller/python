DATABASE = 'dojos_and_ninjas'
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_dojo_with_ninja (cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        dojo = cls(results[0])
        for x in results:
            ninja_data = {
                'id' : x['ninjas.id'],
                'first_name' : x['first_name'],
                'last_name' : x['last_name'],
                'age' : x['age'],
                'dojo_id' : x['dojo_id'],
                'created_at' : x['ninjas.created_at'],
                'updated_at' : x['ninjas.updated_at']
            }
            dojo.ninjas.append( model_ninja.Ninja(ninja_data))
        return dojo

    @classmethod
    def get_all_dojo_ninja (cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id"
        results = connectToMySQL(DATABASE).query_db(query, data)

        dojo = cls(results[0])
        for x in results:
            ninja_data = {
                'name' : x['dojo.name'],
                'first_name' : x['first_name'],
                'last_name' : x['last_name'],
                'age' : x['age'],
                'created_at' : x['ninjas.created_at'],
                'updated_at' : x['ninjas.updated_at']
            }
            dojo.ninjas.append( model_ninja.Ninja(ninja_data))
        return dojo



    @classmethod
    def create_dojo(cls, data):
        query = 'INSERT INTO dojos (name) VALUES ( %(name)s);'
        
        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def get_all_dojo(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)

        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )

        return dojos


    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        dojo_called = connectToMySQL(DATABASE).query_db(query, data)

        return cls(dojo_called[0])


    @classmethod
    def update_one_dojo(cls, data):
        query = "UPDATE dojos SET name=%(name)s WHERE id = %(id)s;"

        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def delete_one_dojo(cls, data):
        query = "DELETE FROM dojo WHERE id = %(id)s;"

        return connectToMySQL(DATABASE).query_db(query, data)

