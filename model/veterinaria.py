from database.connector import *
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship

class Veterinaria(Base):
    __tablename__ = "veterinarias"
    codigo = Column(Integer, primary_key=True)
    descripcion = Column(String(200), nullable=False)

    # Creamos  los campo y la relación con cliente y mascota
    cliente_id = Column(Integer, ForeignKey('clientes.codigo'), nullable=False)
    mascota_id = Column(Integer, ForeignKey('mascotas.codigo'), nullable=False)
    # Indicamos las referencia a los modelo
    cliente = relationship('Cliente')
    mascota = relationship('Mascota')