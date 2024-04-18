from flask import Blueprint, request, jsonify
from model.predio import Predio
from utils.db import db
predio=Blueprint('predio',__name__)

@predio.route('/predio/v1', methods = ['GET'])
def getMensaje():
    result={}
    result["data"]='flask-crud-backend'
    return jsonify(result)

@predio.route('/predio/v1/listar', methods = ['GET'])
def getPredio():
    result={}
    predio = Predio.query.all()
    result["data"]=predio
    result["status_code"]=200
    result["msg"]="Se recupero los predios sin inconvenientes"
    return jsonify(result),200

@predio.route('/predio/v1/insertar', methods = ['POST'])
def insert():
    result = {}
    body = request.get_json()
    id_tipo_predio = body.get('id_tipo_predio')
    descripcion = body.get('descripcion')
    ruc = body.get('ruc')
    telefono = body.get('telefono')
    correo = body.get('correo')
    direccion = body.get('direccion')
    idubigeo = body.get('idubigeo')
    
    if not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo:
        result["status_code"]=400
        result["msg"]="Faltan Datos"
        return jsonify(result),400
    
    predio= Predio(id_tipo_predio, descripcion, ruc, telefono,correo, direccion, idubigeo)
    db.session.add(predio)
    db.session.commit()
    result["data"]=predio
    result["status_code"]=201
    result["msg"]="Se agrego Correctamente"
    return jsonify(result),201



@predio.route('/predio/v1/update', methods = ['POST'])
def update():
    result = {}
    body = request.get_json()
    id_predio = body.get('id_predio')
    id_tipo_predio = body.get('id_tipo_predio')
    descripcion = body.get('descripcion')
    ruc = body.get('ruc')
    telefono = body.get('telefono')
    correo = body.get('correo')
    direccion = body.get('direccion')
    idubigeo = body.get('idubigeo')
    
    if not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo:
        result["status_code"]=400
        result["msg"]="Faltan Datos"
        return jsonify(result),400
    
    predio = Predio.query.get(id_predio)
    if not predio:
        result["status_code"]=400
        result["msg"]="Predio NO Existe"
        return jsonify(result),400 
    
    predio.id_tipo_predio=id_tipo_predio
    predio.descripcion=descripcion
    predio.ruc=ruc
    predio.telefono=telefono
    predio.correo=correo
    predio.direccion=direccion
    predio.idubigeo=idubigeo
    
    db.session.commit()
    
    result["data"]=predio
    result["status_code"]=202
    result["msg"]="Se modificó el predio"
    return jsonify(result),202

@predio.route('/predio/v1/delete', methods = ['DELETE'])
def delete():
    result={}
    body = request.get_json()
    id_predio = body.get('id_predio')
    if not id_predio:
        result["status_code"]=400
        result["msg"]="Debe consignar un id_predio válido"
        return jsonify(result),400
    
    predio = Predio.query.get(id_predio)
    if not predio:
        result["status_code"]=400
        result["msg"]="Predio NO Existe"
        return jsonify(result),400
    
    db.session.delete(predio)
    db.session.commit()
    
    result["data"]=predio
    result["status_code"]=200
    result["msg"]="Se eliminó el predio"
    return jsonify(result),200