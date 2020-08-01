from flask import Flask, jsonify, request
from database.dml import DML

app = Flask(__name__)
app.config['DEBUG'] = True

dml = DML()


@app.route('/', methods=['GET'])
def home():
    return "<h1> Mi API >.< </h1>"


# ENDPOINT
# API VETERINARIA
# http://api.veterinaria.com/v1/persona
# http://api.veterinaria.com/v1/cliente
# http://api.veterinaria.com/v1/animal
# http://api.veterinaria.com/v1/veterinaria

@app.route('/v1/personas', methods=['GET'])
def personas():
    data = dml.getPersona()
    return jsonify(data)


@app.route('/v1/persona', methods=['POST'])
def persona():
    print('Request info ==> ', request.args['nombre'])

    # get params Request
    nombre = request.args['nombre']
    apellido = request.args['apellido']
    print(nombre, apellido)
    data = dml.addPersona(nombre, apellido)
    return jsonify({'data': data})


@app.route('/v1/persona/<int:persona_id>', methods=['DELETE'])
def eliminarPersona(persona_id):
    print('Id a eliminar ', persona_id)
    data = dml.delPersona(persona_id)
    return jsonify({'status': data})


@app.route('/v1/persona/<int:persona_id>', methods=['PUT'])
def actualizarPersona(persona_id):
    print('Request info ==> ', request.args['nombre'])

    # get params Request
    nombre = request.args['nombre']
    apellido = request.args['apellido']

    data = dml.updatePersona(persona_id, nombre, apellido)
    return jsonify({'data': data})
