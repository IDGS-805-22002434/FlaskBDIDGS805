from . import cursos
import forms
from flask import Flask, render_template, request, redirect, url_for

from models import db, Curso, Maestros, Alumnos

@cursos.route("/cursos", methods=['GET', 'POST'])
def lista_cursos():
        cursos_lista = Curso.query.all()
        return render_template("cursos/listadoCursos.html", cursos=cursos_lista)

@cursos.route("/cursos/insertar", methods=['GET', 'POST'])
def insertar_cursos():
            maestros_disp = Maestros.query.all()
            
            if request.method == 'POST':
                nuevo_curso = Curso(
                    nombre=request.form.get('nombre'),
            		descripcion=request.form.get('descripcion'),
            		maestro_id=request.form.get('maestro_id') 
                )
                db.session.add(nuevo_curso)
                db.session.commit()
                return redirect(url_for('cursos.lista_cursos'))
                
            return render_template("cursos/insertarCursos.html", maestros=maestros_disp)

@cursos.route("/cursos/detalles", methods=['GET', 'POST'])
def detalles():
    if request.method == 'GET':
        id = request.args.get('id')
        curso = db.session.query(Curso).filter(Curso.id==id).first()
        
    return render_template('cursos/detallesCursos.html', curso=curso)

@cursos.route("/cursos/inscribir", methods=['GET', 'POST'])
def inscribir_alumno():
    if request.method == 'POST':
        curso_id = request.form.get('curso_id')
        alumno_id = request.form.get('alumno_id')
        
        curso = db.session.query(Curso).filter(Curso.id == curso_id).first()
        alumno = db.session.query(Alumnos).filter(Alumnos.id == alumno_id).first()
        
        if curso and alumno:
            if alumno not in curso.alumnos:
                curso.alumnos.append(alumno)
                db.session.commit()
                
        return redirect(url_for('cursos.lista_cursos'))
        
    cursos_lista = Curso.query.all()
    alumnos_lista = Alumnos.query.all()
    return render_template("cursos/inscribir.html", cursos=cursos_lista, alumnos=alumnos_lista)