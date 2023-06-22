# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app.models import ninja

class Dojo:
    DB='dojos_and_ninjas_schema'

    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.all_ninjas= []


    @ classmethod
    def get_all(cls):
        query="""
        SELECT * FROM dojos;
        """

        result= connectToMySQL(cls.DB).query_db(query)
        all_dojos=[]

        for dojo in result:
            all_dojos.append(cls(dojo))

        return all_dojos
        
    @classmethod
    def add_dojo(cls,data):
        query="""
        INSERT INTO dojos (name)
        VALUES(%(name)s);
        """

        result=connectToMySQL(cls.DB).query_db(query, data)

        return result

    @classmethod
    def get_one_dojo (cls, data):
        query="""
        SELECT * FROM dojos 
        JOIN ninjas ON dojos.id=ninjas.dojo_id
        WHERE dojos.id=%(id)s;
        """

        result=connectToMySQL(cls.DB).query_db(query,data)

        one_dojo = cls(result[0]) 

        print(result)

        for row_from_db in result:

            ninja_data = {
                'id': row_from_db['ninjas.id'],
                'dojo_id': row_from_db['dojo_id'],
                'first_name': row_from_db['first_name'],
                'last_name': row_from_db['last_name'],
                'age': row_from_db['age'],
                'created_at': row_from_db['ninjas.created_at'],
                'updated_at': row_from_db['ninjas.updated_at']
            }

            one_dojo.all_ninjas.append(ninja.Ninja(ninja_data))

        return one_dojo
