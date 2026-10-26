from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')

class Usuario:
    def __init__(self,data):
        self.id = data.get('id')
        self.nombre = data.get('nombre')
        self.apellido = data.get('apellido')
        self.email = data.get('email')
        self.password = data.get('password')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    @classmethod
    def save(cls,data):
        query = """INSERT INTO usuarios (nombre, apellido, email, password, created_at, updated_at) VALUES (%(nombre)s,%(apellido)s,%(email)s,%(password)s,NOW(),NOW());"""
        return connectToMySQL('VoluntaMe').query_db(query,data)

    @classmethod
    def get_all(cls):
        query ="SELECT * FROM usuarios"
        usuarios_en_db = connectToMySQL('VoluntaMe').query_db(query)
        usuarios =[]
        for usuario in usuarios_en_db:
            usuarios.append(cls(usuario))
        return usuarios

    @classmethod
    def get_by_email(cls, data):
        query ="SELECT * FROM usuarios WHERE email=%(email)s"
        usuario_en_db = connectToMySQL('VoluntaMe').query_db(query, data)
        print("USUARIO EN DB",usuario_en_db)
        if not usuario_en_db:
            return None
        return cls(usuario_en_db[0])

    @staticmethod
    def valaidar_registro(formulario):
        es_valido = True

        if len(formulario['nombre'])< 2:
            flash("Nombre debe tener al menos 2 caracteres","registro")
            es_valido = False

        if len(formulario['apellido'])< 2:
            flash("Apellido debe tener al menos 2 caracteres","registro")
            es_valido = False

        if not EMAIL_REGEX.match(formulario['email']):
            flash("Email sin formato valido","registro")
            es_valido = False

        elif Usuario.get_by_email({'email':formulario['email']}):
            print(Usuario.get_by_email({'email':formulario['email']}))
            flash("Ya existe una cuenta registrada con este email",'registro')
            es_valido = False
        
        return es_valido 

    @staticmethod
    def validar_login(formulario):
        si_valido = True
        if not EMAIL_REGEX.match(formulario['email_inicio_session']):
            flash("El email no tiene un formato valido",'inicio_sesion')
            si_valido = False
        if len (formulario['password_inicio_sesion']) < 8:
            flash("el password deve tener mas de 8 caracteres",'inicio_sesion')
            si_valido = False
        return si_valido

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM usuarios WHERE id=%(id)s"
        usuario_en_db = connectToMySQL('viajero-frecuente').query_db(query,data)
        if not usuario_en_db:
            return None
        return cls(usuario_en_db[0])