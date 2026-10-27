from flask_app import app

from flask import render_template, redirect, flash, session, request
from flask_app.models.usuario import Usuario
from flask_app.models.mision import Mision
from datetime import date

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
#ver mision
@app.route('/mision/<int:id>/ver')
def ver_mision(id):
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para acceder a esta página", "error")
        return redirect('/')

    mision = Mision.get_by_id({'id': id})

    if not mision:
        flash("Misión no encontrada", "error")
        return redirect('/misiones')

    usuario = Usuario.get_by_id({'id': session['usuario_id']})

    return render_template('ver_mision.html', usuario=usuario, mision=mision)
#crear nuevo
@app.route('/mision/nuevo')
def nueva_mision():
    if 'usuario_id' not in session:
        flash("debes iniciar sesion primero para acceder a esta pagina", "error_mision")
        return redirect('/')
    usuario = Usuario.get_by_id({'id': session['usuario_id']})
    return render_template('nueva_mision.html', usuario=usuario, now_date=date.today().isoformat())

@app.route('/misiones/crear', methods=['POST'])
def crear_mision():
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para acceder a esta página", "error")
        return redirect('/')
    
    if not Mision.validar_mision(request.form):
        return redirect('/mision/nuevo')
    
    datos_mision = {
        'nombre': request.form['nombre'].strip(),
        'fecha': request.form['fecha'],
        'voluntario_necesario': int(request.form['voluntario_necesario']),
        'descripcion': request.form['descripcion'].strip(),
        'usuario_id': session['usuario_id']
    }

    resultado = Mision.save(datos_mision)
    if not resultado:
        flash("No se pudo guardar la mision","error")
        return redirect('/mision/nuevo')

    flash("Mision creada correctamente", "success")
    return redirect('/misiones')

@app.route('/mision/<int:id>/eliminar', methods=['POST'])
def eliminar_mision(id):
    if 'usuario_id' not in session:
        return redirect('/')

    mision = Mision.get_by_id({'id': id})

    if not mision:
        flash("Misión no encontrada", "error")
        return redirect('/misiones')

    if mision.usuario_id != session['usuario_id']:
        flash("No tienes permiso para eliminar esta misión", "error")
        return redirect('/misiones')

    Mision.eliminar({'id': id})

    flash("Misión eliminada correctamente", "success")
    return redirect('/misiones')



@app.route('/mision/<int:id>/editar')
def editar_mision(id):
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para acceder a esta página", "error")
        return redirect('/')

    mision = Mision.get_by_id({'id': id})

    if not mision:
        flash("Mision no encontrada", "error")
        return redirect('/misiones')

    if mision.usuario_id != session['usuario_id']:
        flash("No tienes permiso para editar esta mision", "error")
        return redirect('/misiones')

    usuario = Usuario.get_by_id({'id': session['usuario_id']})

    return render_template(
        'editar_mision.html',
        usuario=usuario,
        mision=mision,
        now_date=date.today().isoformat()
    )


@app.route('/mision/<int:id>/actualizar', methods=['POST'])
def actualizar_mision(id):
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para acceder a esta página", "error")
        return redirect('/')

    mision = Mision.get_by_id({'id': id})

    if not mision:
        flash("Mision no encontrada", "error")
        return redirect('/misiones')

    if mision.usuario_id != session['usuario_id']:
        flash("No tienes permiso para editar esta mision", "error")
        return redirect('/misiones')

    if not Mision.validar_mision(request.form):
        return redirect(f'/mision/{id}/editar')

    datos_mision = {
        'id': id,
        'nombre': request.form['nombre'].strip(),
        'fecha': request.form['fecha'],
        'voluntario_necesario': int(request.form['voluntario_necesario']),
        'descripcion': request.form['descripcion'].strip()
    }

    Mision.update(datos_mision)

    flash("Mision actualizada correctamente", "success")
    return redirect('/misiones')

    
    