DATABASE = 'dojos_and_ninjas'
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_dojo

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']


    @classmethod
    def create_ninja(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s );'
        
        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def get_all_ninja(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)

        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )

        return ninjas


    @classmethod
    def get_one_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        ninja_called = connectToMySQL(DATABASE).query_db(query, data)

        return cls(ninja_called[0])


    @classmethod
    def update_one_ninja(cls, data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s, dojo_id=%(dojo_id)s WHERE id = %(id)s;"

        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def delete_one_ninja(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"

        return connectToMySQL(DATABASE).query_db(query, data)

