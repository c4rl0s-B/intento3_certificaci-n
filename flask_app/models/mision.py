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