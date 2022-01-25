DATABASE = 'email_schema'
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create_email(cls, data):
        query = 'INSERT INTO emails (email) VALUES ( %(email)s );'
        
        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)

        users = []
        for x in results:
            users.append( cls(x) )

        return users


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

    @staticmethod
    def validator(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash('Invalid email address. Please use the following format: name@domain.com')
            is_valid = False
        
        return is_valid

    @staticmethod
    def validate_success(email):
        is_valid = False
        if EMAIL_REGEX.match(email['email']):
            flash('Success! The follwing address has been added:')
            is_valid = True
        
        return is_valid

