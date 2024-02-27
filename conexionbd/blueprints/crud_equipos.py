from flask import Blueprint, request, jsonify
from models.equipoM import Equipo
from schemas.equipoS import EquipoEsquema
from main import db
import os


crud_equipos = Blueprint('crud_equipos',__name__)
esquema_equipos = EquipoEsquema(many=True)
esquema_equipo = EquipoEsquema()


@crud_equipos.route('/registrar-equipo', methods=['POST'])
def registrar_equipo():
    '''
    Agrega un equipo
    '''
    nombre = request.json['nombre']
    direccion = request.json['dir']    
    equipo = Equipo.query.get(direccion)
    if (equipo is None):
        nuevo_equipo = Equipo(direccion, nombre)
        db.session.add(nuevo_equipo)
        db.session.commit()
        return jsonify({'msg':'success'})    
    
    return jsonify({'msg':'error'})    

@crud_equipos.route('/actualizar-equipo', methods=['PUT'])
def actualizar_equipo():
    '''
    Actualiza un equipo
    '''
    nombre = request.json['nombre']
    direccion = request.json['dir']    
    equipo = Equipo.query.get(direccion)
    if (equipo is not None):
        equipo.nombre = nombre
        db.session.commit()
        return jsonify({'msg':'success'})        
    return jsonify({'msg':'error'}) 

@crud_equipos.route('/eliminar-equipo', methods=['DELETE'])
def eliminar_equipo():
    '''
    Elimina un equipo
    '''
    direccion = request.json['dir'] 
    try:   
        equipo = Equipo.query.get(direccion)
        if (equipo is not None):
            db.session.delete(equipo)
            db.session.commit()
            return jsonify({'msg':'success'}) 
    except Exception as e:       
        return jsonify({'msg':'error'})
    
@crud_equipos.route('/obtener-equipos', methods=['GET'])
def obtener_equipos():
    '''
    Obtiene todos los equipos registrados    
    '''       
    equipos = Equipo.query.all()
    return esquema_equipos.jsonify(equipos)


@crud_equipos.route('/obtener-equipo/<dir>', methods=['GET'])
def obtener_equipo(dir):
    '''
    Obtiene la información de un equipo mediante su dirección ip
    Regresa un json vacío si el equipo no está en el sistema
    '''
    equipo = Equipo.query.get(dir)      
    return esquema_equipo.jsonify(equipo)

@crud_equipos.route('/probar-latencia', methods=['POST'])
def probar_latencia():
    '''
    Obtiene la información de un equipo mediante su dirección ip
    Regresa un json vacío si el equipo no está en el sistema
    '''   
    direccion = request.json['dir']
    response = os.system("ping -c 1 " + direccion)         
    if response == 0:
        return jsonify({'msg':'success'})
    else:
        return jsonify({'msg':'error'})