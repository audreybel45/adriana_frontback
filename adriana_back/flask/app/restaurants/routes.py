# /flask/app/restaurants/routes.py

from flask import Blueprint, request, jsonify
from app.restaurants.crud import (
    create_restaurant,
    get_restaurant,
    get_all_restaurants,
    update_restaurant,
    delete_restaurant
)

restaurants_bp = Blueprint('restaurants', __name__)

# Ruta para obtener todos los restaurantes
@restaurants_bp.route('/', methods=['GET'])
def list_restaurants():
    restaurants = get_all_restaurants()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])

# Ruta para obtener un restaurante por ID
@restaurants_bp.route('/<int:id>', methods=['GET'])
def retrieve_restaurant(id):
    restaurant = get_restaurant(id)
    return jsonify(restaurant.to_dict())

# Ruta para crear un nuevo restaurante
@restaurants_bp.route('/', methods=['POST'])
def add_restaurant():
    data = request.json
    new_restaurant = create_restaurant(data)
    return jsonify(new_restaurant.to_dict()), 201

# Ruta para actualizar un restaurante existente
@restaurants_bp.route('/<int:id>', methods=['PUT'])
def modify_restaurant(id):
    data = request.json
    updated_restaurant = update_restaurant(id, data)
    return jsonify(updated_restaurant.to_dict())

# Ruta para eliminar un restaurante
@restaurants_bp.route('/<int:id>', methods=['DELETE'])
def remove_restaurant(id):
    deleted_restaurant = delete_restaurant(id)
    return jsonify({'message': 'Restaurante eliminado'}), 204
