from main import db

class Historial(db.Model):
    __tablename__ = 'historial'
    id_hist = db.Column(db.Integer(), primary_key = True, autoincrement=True)
    ip = db.Column(db.String(15), nullable=False)
    equipo_dir = db.Column(db.String(15), db.ForeignKey('equipo.dir'))
    fecha = db.Column(db.DateTime(), nullable=False)

    def __init__(self, ip, equipo_dir, fecha):
        """
        Registra un historial
        
        Params:
            ip: ipección ipv4 del historial       
            equipo_dir: equipo_dir del historial
        """
        self.id_hist
        self.ip = ip
        self.equipo_dir = equipo_dir
        self.fecha = fecha