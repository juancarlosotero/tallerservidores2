from database.connector import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__ = 'clientes'
    codigo = Column(Integer, primary_key=True)
    direccion = Column(String(30))
    telefono = Column(String(15))
    cuentaBanco = Column(String(10))

    # Creamos  el campo y la relación con persona
    persona_id = Column(Integer, ForeignKey('personas.codigo'))
    persona = relationship('Persona')

class Persona(Base):
    __tablename__ = "personas"
    codigo = Column(Integer, primary_key=True)
    nombre = Column(String(30))
    apellido = Column(String(30))

    # Creamos la relación con cliente
    clientes = relationship(Cliente, backref="clientes")

    def serializar(self):
        data = {"id": self.codigo, "nombre": self.nombre, "apellido": self.apellido}
        return data





