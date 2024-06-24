# /flask/app/turismo/routes.py

from flask import Blueprint, request, jsonify
from app.turismo.crud import (
    create_turismo,
    get_turismo,
    get_all_turismos,
    update_turismo,
    delete_turismo
)

turismo_bp = Blueprint('turismo', __name__)

# Ruta para obtener todos los puntos turísticos
@turismo_bp.route('/', methods=['GET'])
def list_turismos():
    turismos = get_all_turismos()
    return jsonify([turismo.to_dict() for turismo in turismos])

# Ruta para obtener un punto turístico por ID
@turismo_bp.route('/<int:id>', methods=['GET'])
def retrieve_turismo(id):
    turismo = get_turismo(id)
    return jsonify(turismo.to_dict())

# Ruta para crear un nuevo punto turístico
@turismo_bp.route('/', methods=['POST'])
def add_turismo():
    data = request.json
    new_turismo = create_turismo(data)
    return jsonify(new_turismo.to_dict()), 201

# Ruta para actualizar un punto turístico existente
@turismo_bp.route('/<int:id>', methods=['PUT'])
def modify_turismo(id):
    data = request.json
    updated_turismo = update_turismo(id, data)
    return jsonify(updated_turismo.to_dict())

# Ruta para eliminar un punto turístico
@turismo_bp.route('/<int:id>', methods=['DELETE'])
def remove_turismo(id):
    deleted_turismo = delete_turismo(id)
    return jsonify({'message': 'Punto turístico eliminado'}), 204
