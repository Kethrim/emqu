from main import db

class Equipo(db.Model):
    __tablename__ = 'equipo'
    dir = db.Column(db.String(15),primary_key = True)
    nombre = db.Column(db.String(100))

    def __init__(self,dir,nombre):
        """
        Registra un equipo
        
        Params:
            dir: dirección ipv4 del equipo       
            nombre: nombre del equipo
        """
        self.dir = dir
        self.nombre = nombre
        
    