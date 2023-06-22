# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database


class Ninja:
    DB='dojos_and_ninjas_schema'

    def __init__(self, data):
        self.id=data['id']
        self.dojo_id=data['dojo_id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query= """
        SELECT * 
        FROM ninjas;
        """

        result= connectToMySQL(cls.DB).query_db(query)

        all_ninjas= []

        for ninja in result:
            all_ninjas.append(cls(ninja))

            return all_ninjas
        
    @classmethod
    def add_ninja(cls,data):
        query="""
        INSERT INTO ninjas (dojo_id, first_name, last_name, age)
        VALUES(%(dojo_id)s,%(first_name)s, %(last_name)s, %(age)s);
        """

        result=connectToMySQL(cls.DB).query_db(query, data)

        return result
    
    @classmethod
    def get_one (cls, data):
        query="""
        SELECT * FROM ninjas WHERE id=%(id)s;
        """

        result=connectToMySQL(cls.DB).query_db(query,data)

        return cls(result[0])
    
    @classmethod
    def update_ninja(cls, data):
        query= """
        UPDATE ninjas SET (dojo_id, first_name, last_name, age)
        VALUES(%(dojo_id)s,%(first_name)s, %(last_name)s, %(age)s)
        WHERE id=%(id)s;
        """

        result=connectToMySQL(cls,data).query_db(query, data)

        return result
    
    @classmethod
    def destroy_one (cls, data):
        query="""
        DELETE FROM ninjas WHERE id=%(id)s;
        """

        result=connectToMySQL(cls.DB).query_db(query,data)

        return result