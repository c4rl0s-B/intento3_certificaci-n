from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Mision:
    def __init__(self, data):
        self.id = data.get('id')
        self.nombre = data.get('nombre')
        self.fecha = data.get('fecha')
        self.voluntario_necesario = data.get('voluntario_necesario')
        self.descripcion = data.get('descripcion')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
        self.usuario_id = data.get('usuario_id')

    @classmethod
    def save(cls,data):
        query = """INSERT INTO misiones (nombre,fecha,voluntario_necesario,descripcion,created_at,updated_at,usuario_id)VALUE(%(nombre)s,%(fecha)s,%(voluntario_necesario)s,%(descripcion)s,NOW(),NOW(),%(usuario_id)s)"""
        return connectToMySQL('VoluntaMe').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM misiones"
        misiones_en_db = connectToMySQL('VoluntaMe').query_db(query)
        misiones = []
        for mision in misiones_en_db:
            misiones.append(cls(mision))
        return misiones

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM misiones WHERE id=%(id)s"
        mision_en_db = connectToMySQL('VoluntaMe').query_db(query,data)
        if not mision_en_db:
            return None
        return cls(mision_en_db[0])

    @classmethod
    def update(cls,data):
        query = """UPDATE misiones SET nombre =%(nombre)s, fecha= %(fecha)s, voluntario_necesario = %(voluntario_necesario)s, descripcion=%(descripcion)s, updated_at = NOW() WHERE id =%(id)s"""
        return connectToMySQL('VoluntaMe').query_db(query,data)

    @classmethod
    def eliminar(cls,data):
        query = "DELETE FROM misiones WHERE id = %(id)s"
        return connectToMySQL('VoluntaMe').query_db(query,data)


    @staticmethod
    def validar_mision(formulario):
        es_valido = True

        if len(formulario['nombre']) < 2:
            flash("los caracteres del nombre de la mision deben ser mas de 2 caracteres",'mision')
            es_valido = False

        if not formulario.get('fecha'):
            flash("La fecha es obligatoria",'mision')
            es_valido = False

        
        if not formulario.get ('voluntario_necesario'):
            flash("la cantidad de voluntarios es obligatoria",'mision')
            es_valido = False
        elif int(formulario['voluntario_necesario'])<2:
            flash("Debe necesitaral menos 2 voluntarios",'mision')
            es_valido = False
            

        if len(formulario['descripcion'])<10:
            flash("La descripción debe tener al menos 10 caracteres",'mision')
            es_valido = False

        return es_valido