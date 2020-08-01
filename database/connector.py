from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conectores de base datos

# Base datos local
# engine = create_engine('sqlite:///mydb.db')

# Base datos relacional
engine = create_engine('mysql+pymysql://root:1234567890@juanotero.ga/tallerdb2')

Base = declarative_base()

# Manejo de las sesiones
Sesion = sessionmaker(bind=engine)
session = Sesion()
