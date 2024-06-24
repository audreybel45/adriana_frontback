# /flask/app/usuarios/routes.py

from flask import Blueprint, request, jsonify
from app import db
from app.usuarios.models import Usuario

usuarios_bp = Blueprint('usuarios', __name__)

# Leer todos los usuarios
@usuarios_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios])

# Leer un usuario por ID
@usuarios_bp.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify(usuario.to_dict())

# Crear un nuevo usuario
@usuarios_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    nuevo_usuario = Usuario(
        foto_perfil=data.get('foto_perfil'),
        correo=data.get('correo'),
        dni=data.get('dni'),
        nombre=data.get('nombre'),
        apellido=data.get('apellido'),
        fecha_nacimiento=data.get('fecha_nacimiento'),
        nombre_usuario=data.get('nombre_usuario'),
        clave=data.get('clave'),
        confirmar_clave=data.get('confirmar_clave')
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify(nuevo_usuario.to_dict()), 201

# Actualizar un usuario existente
@usuarios_bp.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.json

    usuario.foto_perfil = data.get('foto_perfil', usuario.foto_perfil)
    usuario.correo = data.get('correo', usuario.correo)
    usuario.dni = data.get('dni', usuario.dni)
    usuario.nombre = data.get('nombre', usuario.nombre)
    usuario.apellido = data.get('apellido', usuario.apellido)
    usuario.fecha_nacimiento = data.get('fecha_nacimiento', usuario.fecha_nacimiento)
    usuario.nombre_usuario = data.get('nombre_usuario', usuario.nombre_usuario)
    usuario.clave = data.get('clave', usuario.clave)
    usuario.confirmar_clave = data.get('confirmar_clave', usuario.confirmar_clave)

    db.session.commit()
    return jsonify(usuario.to_dict())

# Eliminar un usuario
@usuarios_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'message': 'Usuario eliminado'}), 204
