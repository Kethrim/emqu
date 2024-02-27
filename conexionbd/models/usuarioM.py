from main import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuario'
    correo = db.Column(db.String(100),primary_key = True)
    contrasenia = db.Column(db.String(105), nullable=False)

    def __init__(self,correo,contrasenia):
        """
        Registra un usuario
        
        Params:
            correo: correo del administrador       
            contrasenia: contraseña del administrador
        """
        self.correo = correo
        self.contrasenia = self._encriptarContra(contrasenia)
        
    def _encriptarContra(self, contrasenia):
        """
        Hashea la contraseña del usuario actual
        
        Params:
            contrasenia: contraseña
        Returns: 
        contraseña hasheada
        """
        return generate_password_hash(contrasenia)
    
    def verificarContra(self, contrasenia):
        """
        Verifica que la contraseña ingresada coincida con la hasheada
        Params:
            contrasenia: contraseña que se desea ingresar
        Returns: booleano indicando si son iguales o no
        """
        return check_password_hash(self.contrasenia, contrasenia)