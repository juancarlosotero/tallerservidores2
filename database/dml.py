from database.connector import *

from model.cliente import Cliente
from model.mascota import Mascota
from model.veterinaria import Veterinaria
from model.cliente import Persona

class DML():
    def getPersona(self):
        """ Query de Persona """
        query = session.query(Persona)

        data = query.all()
        informacion = []
        for info in data:
            temp = {}
            temp['codigo'] = info.codigo
            temp['nombre'] = info.nombre
            temp['apellido'] = info.apellido

            informacion.append(temp)
            print(temp)

        return informacion
    def addPersona(self, nom, ape):
        """ Agregar a una persona """
        new = Persona(nombre=nom, apellido=ape)

        session.add(new)
        session.commit()
        print("New persona ", new)
        return new.serializar()

    def delPersona(self, id):
        """ Metodo para eliminar una persona """
        query = session.query(Persona).filter_by(codigo=id)
        print('SQL ===> ', query)
        temp = query.first()
        print('RESULTADO ==> ', temp)

        if temp is None:
            return 'el usuario con el ID No existe '

        session.delete(temp)
        session.commit()
        return True
    def updatePersona(self, id, nom, ape):
        """Metodo para actualizar información de una persona"""
        query = session.query(Persona).filter_by(codigo=id)
        print(query)
        temp = query.first()
        print('Resultado ', temp)

        temp.nombre = nom
        temp.apellido = ape

        session.add(temp)
        session.commit()
        return True