from . import alumnos
import forms
from flask import Flask, render_template, request, redirect, url_for

from models import Alumnos
from models import db, Alumnos

@alumnos.route("/alumnos", methods = ['GET', 'POST'])
def lista_alumnos():
		create_form = forms.UserForm(request.form)
		alumno = Alumnos.query.all()
		return render_template("alumnos/listadoAlum.html", form = create_form, alumno = alumno)

@alumnos.route("/alumnos/insertar", methods = ['GET', 'POST'])
def insertar_alumnos():
			create_form = forms.UserForm(request.form)
			if request.method == 'POST':
				alum = Alumnos(nombre = create_form.nombre.data,
					apellidos = create_form.apellidos.data,
					email = create_form.email.data,
     				telefono = create_form.telefono.data)
				db.session.add(alum)
				db.session.commit()
				return redirect(url_for('alumnos.lista_alumnos'))
			return render_template("alumnos/Alumnos.html", form = create_form)

@alumnos.route("/alumnos/detalles", methods = ['GET', 'POST'])
def detalles():
    if request.method == 'GET':
        id = request.args.get('id')
        alumno = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        
    return render_template('alumnos/detalles.html', alumno=alumno)

@alumnos.route("/alumnos/modificar", methods = ['GET', 'POST'])
def modificar():
		create_form = forms.UserForm(request.form)
		if request.method=='GET':
			id=request.args.get('id')
			#select * from alumnos where id=id
			alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
			create_form.id.data=alum1.id
			create_form.nombre.data=alum1.nombre
			create_form.apellidos.data=alum1.apellidos
			create_form.email.data=alum1.email
			create_form.telefono.data=alum1.telefono
		if request.method == 'POST':
			id = create_form.id.data
			alum = db.session.query(Alumnos).filter(Alumnos.id==id).first()
			alum.nombre = create_form.nombre.data
			alum.apellidos = create_form.apellidos.data
			alum.email = create_form.email.data
			alum.telefono = create_form.telefono.data
			db.session.add(alum)
			db.session.commit()
			return redirect(url_for('alumnos.lista_alumnos'))
		return render_template("alumnos/modificar.html", form = create_form)

@alumnos.route("/alumnos/eliminar", methods = ['GET', 'POST'])
def eliminar():
	create_form = forms.UserForm(request.form)
	if request.method=='GET':
			id=request.args.get('id')
			#select * from alumnos where id=id
			alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
			create_form.id.data=alum1.id
			create_form.nombre.data=alum1.nombre
			create_form.apellidos.data=alum1.apellidos
			create_form.email.data=alum1.email
			create_form.telefono.data=alum1.telefono
	if request.method == 'POST':
		id = create_form.id.data
		alum = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		alum.nombre = create_form.nombre.data
		alum.apellidos = create_form.apellidos.data
		alum.email = create_form.email.data
		alum.telefono = create_form.telefono.data
		db.session.delete(alum)
		db.session.commit()
		return redirect(url_for('alumnos.lista_alumnos'))
	return render_template("alumnos/eliminar.html", form = create_form)