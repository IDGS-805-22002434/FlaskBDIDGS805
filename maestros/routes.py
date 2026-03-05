from . import maestros
import forms
from flask import Flask, render_template, request, redirect, url_for

from models import Maestros
from models import db, Maestros

@maestros.route("/maestros", methods = ['GET','POST'])
def lista_maestros():
		create_form = forms.MaestrosForm(request.form)
		maestros = Maestros.query.all()
		return render_template("maestros/listadoMest.html", form = create_form, maestros = maestros)

@maestros.route("/maestros/insertar", methods = ['GET', 'POST'])
def insertar_maestro():
			create_form = forms.MaestrosForm(request.form)
			if request.method == 'POST':
				maes = Maestros(nombre = create_form.nombre.data,
					apellidos = create_form.apellidos.data,
					email = create_form.email.data,
     				especialidad = create_form.especialidad.data)
				db.session.add(maes)
				db.session.commit()
				return redirect(url_for('maestros.lista_maestros'))
			return render_template("maestros/insertarMest.html", form = create_form)

@maestros.route("/maestros/detalles", methods = ['GET', 'POST'])
def detalles_maestro():
    if request.method=='GET':
        matricula=request.args.get('matricula')
        maes1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
        nombre=maes1.nombre
        apellidos=maes1.apellidos
        especialidad=maes1.especialidad
        email=maes1.email
    return render_template('maestros/detallesMest.html',matricula=matricula,nombre=nombre,apellidos=apellidos,email=email,especialidad=especialidad)

@maestros.route("/maestros/modificar", methods = ['GET', 'POST'])
def modificar_maestro():
		create_form = forms.MaestrosForm(request.form)
		if request.method=='GET':
			matricula=request.args.get('matricula')
			maes1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
			create_form.matricula.data=maes1.matricula
			create_form.nombre.data=maes1.nombre
			create_form.apellidos.data=maes1.apellidos
			create_form.especialidad.data=maes1.especialidad
			create_form.email.data=maes1.email
		if request.method == 'POST':
			matricula = create_form.matricula.data
			maes = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
			maes.nombre = create_form.nombre.data
			maes.apellidos = create_form.apellidos.data
			maes.email = create_form.email.data
			maes.especialidad = create_form.especialidad.data
			db.session.add(maes)
			db.session.commit()
			return redirect(url_for('maestros.lista_maestros'))
		return render_template("maestros/modificarMest.html", form = create_form)

@maestros.route("/maestros/eliminar", methods = ['GET', 'POST'])
def eliminar_maestro():
	create_form = forms.MaestrosForm(request.form)
	if request.method=='GET':
			matricula=request.args.get('matricula')
			maes1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
			create_form.matricula.data=maes1.matricula
			create_form.nombre.data=maes1.nombre
			create_form.apellidos.data=maes1.apellidos
			create_form.email.data=maes1.email
			create_form.especialidad.data=maes1.especialidad
	if request.method == 'POST':
		matricula = create_form.matricula.data
		maes = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		maes.nombre = create_form.nombre.data
		maes.apellidos = create_form.apellidos.data
		maes.email = create_form.email.data
		maes.especialidad = create_form.especialidad.data
		db.session.delete(maes)
		db.session.commit()
		return redirect(url_for('maestros.lista_maestros'))
	return render_template("maestros/eliminarMest.html", form = create_form)