from main import ma
from marshmallow import fields

class HistorialEsquema(ma.Schema):
    """ Crea un esquema para un equipo"""
    id_hist = fields.Int()
    ip = fields.Str()
    equipo_dir = fields.Str()
    fecha = fields.DateTime()
    
    class Meta:
        """Formato de salida"""
        fields = ['id_hist','ip', 'equipo_dir','fecha']