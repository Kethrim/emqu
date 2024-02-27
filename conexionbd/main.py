from flask import Flask  #bibliotecas de flask
from flask_cors import CORS #bibliotes de cors
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
from flask_mail import Mail

""" 
Primero se crean dos instancias de SQLAlchemy y de Mashmellow fuentes:
https://www.sqlalchemy.org/
https://marshmallow.readthedocs.io/en/stable/

SQLAlchemy es una aplcación para mapear Bases de Datos relacionales para SQL
Marshmallow es un ORM o framework para convertir tipos de datos y serializarlos 
"""

db = SQLAlchemy()
ma = Marshmallow()

from flask_wtf.csrf import CSRFProtect # para cifrar datos
from config import DevelopmentConfig # para la configuración de la aplicación

"""
Blueprint
Se implementa los blueprint para que el funcionamiento de flask
se reparta en distintos archivos
"""

from blueprints.inicio_sesion import inicio_sesion
from blueprints.crud_equipos import crud_equipos
from blueprints.historialB import historial

__author__ = "Trad Mateos Kethrim Guadalupe"
__credits__ = [""]
__license__ = ""
__version__ = "1.0"
__maintainer__ = "Trad Mateos Kethrim Guadalupe"
__email__ = "kethrim.tradmateos@gmail.com"
__status__ = "Development"

# Iniciamos una instanica de Flask

app = Flask(__name__)

# Iniciamos una instancia de CSRF para cifrar los datos 

csrf = CSRFProtect()

""" 
Los CORS (Intecambio de Recursos de Origen Cruzado) sirven para que el front end pueda concetarse con el backend,
pues el front end se encuetra en un dominio distinto a del backend,
en resumen es como un "permiso"
"""

CORS(app)

# Utlizamos la configuración de la app que esta en el archivo config.py

app.config.from_object(DevelopmentConfig)

# Configuramos una isntancia de Meil para poder mandar correos

mail = Mail()

mail.init_app(app)

app.register_blueprint(inicio_sesion)
app.register_blueprint(crud_equipos)
app.register_blueprint(historial)

# Iniciamos la app con la base de datos

db.init_app(app)

# solo es por si se compila main.py aunque podrá generar errores y busgs

if __name__ == '__main__':
    app.run(port=7000)    
    
    with app.app_context():
        db.create_all()
        ma.init_app(app)
