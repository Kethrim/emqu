from main import ma
from marshmallow import fields

class UsuarioEsquema(ma.Schema):
    """Esquema para el modelo de un usuario"""
    nombre = fields.Str()
    contrasenia = fields.Str()
    
    class Meta:
        """Formato de salida"""
        fields = ("nombre", "contrasenia")