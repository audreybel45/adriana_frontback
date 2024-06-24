# /flask/app/guias_turisticos/routes.py

from flask import Blueprint, request, jsonify
from app.guias_turisticos.crud import (
    create_guia_turistico,
    get_guia_turistico,
    get_all_guias_turisticos,
    update_guia_turistico,
    delete_guia_turistico
)

guias_turisticos_bp = Blueprint('guias_turisticos', __name__)

# Ruta para obtener todos los guías turísticos
@guias_turisticos_bp.route('/', methods=['GET'])
def list_guias_turisticos():
    guias = get_all_guias_turisticos()
    return jsonify([guia.to_dict() for guia in guias])

# Ruta para obtener un guía turístico por ID
@guias_turisticos_bp.route('/<int:id>', methods=['GET'])
def retrieve_guia_turistico(id):
    guia = get_guia_turistico(id)
    return jsonify(guia.to_dict())

# Ruta para crear un nuevo guía turístico
@guias_turisticos_bp.route('/', methods=['POST'])
def add_guia_turistico():
    data = request.json
    nuevo_guia = create_guia_turistico(data)
    return jsonify(nuevo_guia.to_dict()), 201

# Ruta para actualizar un guía turístico existente
@guias_turisticos_bp.route('/<int:id>', methods=['PUT'])
def modify_guia_turistico(id):
    data = request.json
    guia_actualizado = update_guia_turistico(id, data)
    return jsonify(guia_actualizado.to_dict())

# Ruta para eliminar un guía turístico
@guias_turisticos_bp.route('/<int:id>', methods=['DELETE'])
def remove_guia_turistico(id):
    guia_eliminado = delete_guia_turistico(id)
    return jsonify({'message': 'Guía turístico eliminado'}), 204
