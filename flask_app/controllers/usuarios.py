from flask_app import app
from flask import render_template,request,redirect,flash,session
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def inicio():
    return render_template ('index.html')

@app.route('/registrar_usuario', methods=['POST'])
def crear_usuario():
    if not Usuario.valaidar_registro(request.form):
        print("Usuario Invalido")
        return redirect('/')

    pass_hasheado = bcrypt.generate_password_hash(request.form['password'])
    datos_registro = {
        'nombre':request.form['nombre'],
        'apellido':request.form['apellido'],
        'email':request.form['email'],
        'password': pass_hasheado
    }
    nuevo_id= Usuario.save(datos_registro)
    session['usuario_id'] = nuevo_id
    print("Usuario Creado", session['usuario_id'])
    return redirect ('/dashboard')

@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_session():
    usuario= Usuario.get_by_email({'email': request.form['email_inicio_sesion']})

    if not usuario or not bcrypt.check_password_hash(usuario.password,request.form['password_inicio_sesion']):
        flash("E-email o contraseña incorectos","inicio_sesion")
        return redirect('/')
    session['usuario_id'] = usuario.id
    session['nombre'] = usuario.nombre
    return redirect('/dashboard')

@app.route('/cerrar_sesion')
def cerrar_sesion():
    session.clear()
    return redirect('/')
