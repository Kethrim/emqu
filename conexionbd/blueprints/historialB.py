from datetime import datetime
from flask import Blueprint, request, jsonify
from main import db

from models.historialM import Historial
from schemas.historialS import HistorialEsquema

historial = Blueprint('historial',__name__)
historial_esquema = HistorialEsquema(many=True)

@historial.route('/agregar-registro', methods=['POST'])
def agregar_registro():
    '''
    Agrega un registro de prueba de latencia
    '''
    equipo = request.json['equipo_dir']
    ip_origen = request.json['ip']
    nuevo_registro = Historial(ip = ip_origen, equipo_dir = equipo, fecha = datetime.now())
    db.session.add(nuevo_registro)
    db.session.commit()
    try:
        return jsonify({'msg':'success'})    
    except:
        return jsonify({'msg':'error'})    

@historial.route('/obtener-registros-ip/<ip>', methods=['GET'])
def obtener_registros_ip(ip):
    '''
    Obtiene todos los registros dada una ip
    '''  
    registros = db.session.query(Historial).filter_by(ip).all()     
    return historial_esquema.jsonify(registros)


@historial.route('/obtener-registros', methods=['GET'])
def obtener_registros():
    '''
    Obtiene todos los registros
    ''' 
    registros = Historial.query.all()
     
    return historial_esquema.jsonify(registros)
    
