from flask import Blueprint, request, jsonify
from main import db

from models.usuarioM import Usuario

inicio_sesion = Blueprint('inicio_sesion',__name__)

@inicio_sesion.route('/registrarse', methods=['POST'])
def registrar_usuario():
    '''
    Agrega un usuario a los administradores
    '''
    correo = request.json['correo']
    contrasenia = request.json['contra']    
    usuario = Usuario.query.get(correo)
    if (usuario is None):
        nuevo_usuario = Usuario(correo, contrasenia)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify({'msg':'success'})    
    
    return jsonify({'msg':'error'})    

@inicio_sesion.route('/ingresar', methods=['POST'])
def iniciar_sesion():
    '''
    Agrega un usuario a los administradores
    '''
    correo = request.json['correo']
    contrasenia = request.json['contra']    
    usuario = Usuario.query.get(correo)
    # print(jsonify(usuario))
    if (usuario is not None):
        print(usuario.correo)
        print(usuario.contrasenia)
        print(usuario._encriptarContra(contrasenia))
        if(usuario.correo == correo and usuario.verificarContra(contrasenia)):
            return jsonify({'msg':'success'})    
    
    return jsonify({'msg':'error'}) 
