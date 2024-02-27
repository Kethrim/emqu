from main import ma
from marshmallow import fields

class EquipoEsquema(ma.Schema):
    """ Crea un esquema para un equipo"""
    dir = fields.Str()
    nombre = fields.Str()
    
    class Meta:
        """Formato de salida"""
        fields = ['dir', 'nombre']