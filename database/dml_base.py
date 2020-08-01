from database.connector import *

from model.cliente import Cliente
from model.mascota import Mascota
from model.veterinaria import Veterinaria
from model.cliente import Persona


class DML():
    """ Clase manejo de consulta de datos"""
    def getCliente(self):
        query = session.query(Cliente)
        print('_____IMPRESION DE DATOS DE CLIENTES_____')
        # el objeto __dict__ permite imprimir las clave valor de la consulta
        # De igual forma uno puedo especificar un campo especifico que desee
        for data in query.all():
            print(data.__dict__)
        print('\n___________________________________\n')

    def getMascotas(self):
        query = session.query(Mascota)
        print('_____IMPRESION DE DATOS DE LAS MASCOTAS_____')
        for data in query.all():
            print(data.__dict__)
        print('\n________________________________\n')

    def getVistiasVeterinaria(self):
        # Consultando las tablas relacionada y realizamos un join
        query = session.query(Veterinaria, Cliente, Mascota) \
            .join(Cliente, Cliente.codigo == Veterinaria.cliente_id) \
            .join(Mascota, Mascota.codigo == Veterinaria.mascota_id) \
            .all()
        print('_____IMPRESION DE HISTORIA_____')
        for data in query:
            for item in data:
                print(item.__dict__)
            print()

        print('\n_______________________________\n')

    def getUniversal(self, Modelo):
        query = session.query(Modelo)
        print('\n_____IMPRESION DE UNIVERSAL {0}_____'.format(Modelo))
        for data in query.all():
            print(data.__dict__)
        print('\n____________FIN_________________\n')


