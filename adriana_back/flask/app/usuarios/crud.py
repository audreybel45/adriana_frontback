# /flask/app/usuarios/routes.py

# /flask/app/usuarios/crud.py

from app import db
from app.usuarios.models import Usuario

def create_usuario(data):
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
    return nuevo_usuario

def get_usuario(usuario_id):
    return Usuario.query.get_or_404(usuario_id)

def get_all_usuarios():
    return Usuario.query.all()

def update_usuario(usuario_id, data):
    usuario = get_usuario(usuario_id)
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
    return usuario

def delete_usuario(usuario_id):
    usuario = get_usuario(usuario_id)
    db.session.delete(usuario)
    db.session.commit()
    return usuario
