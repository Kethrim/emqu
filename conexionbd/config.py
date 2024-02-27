class Config(object):
    SECRET_KEY="my_secret_key"

class DevelopmentConfig(Config):
    DEBUG= True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://pruebatest:pruebatest@localhost/gestion_equipos'        
    SQLALCHEMY_TRACK_MODIFICATIONS = False