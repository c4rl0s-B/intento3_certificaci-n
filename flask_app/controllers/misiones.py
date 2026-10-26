from flask_app import app

from flask import render_template, redirect, flash, session, request
from flask_app.models.usuario import Usuario
from flask_app.models.mision import Mision

@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/')
    return redirect('/misiones')

@app.route('/misiones')
def misiones():
    if 'usuario_id' not in session:
        flash("debes iniciar sesion primero para acceder a esta pagina")
        return redirect('/')

    usuario = Usuario.get_by_id({'id': session['usuario_id']})
    misiones = Mision.get_all()
    return render_template('dashboard.html', usuario= usuario, misiones = misiones)

@app.route('/mision/nuevo', methods=['POST'])
def nueva_mision():
    if 'usuario_id' not in session:
        flash("debes iniciar sesion primero para acceder a esta pagina", "error_mision")
        return redirect('/')