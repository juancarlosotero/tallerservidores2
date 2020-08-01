from database.connector import *
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship

from model.veterinaria import Veterinaria


class Mascota(Base):
    __tablename__ = "mascotas"
    codigo = Column(Integer, primary_key=True)
    alias = Column(String(30))
    especies = Column(String(30))
    raza = Column(String(30))
    colorPelo = Column(String(30))
    fechaNacimiento = Column(Date())
    peso = Column(Float)
    historial = Column(String(50))
    calendario = Column(Date())

    # Creamos la relación con Veterinaria
    veterinaria = relationship(Veterinaria, backref="veterinarias")









