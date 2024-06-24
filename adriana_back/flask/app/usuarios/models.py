# /flask/app/usuarios/models.py

from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foto_perfil = db.Column(db.String(255))
    correo = db.Column(db.String(255), unique=True)
    dni = db.Column(db.String(8))
    nombre = db.Column(db.String(255))
    apellido = db.Column(db.String(255))
    fecha_nacimiento = db.Column(db.Date)
    nombre_usuario = db.Column(db.String(255))
    clave = db.Column(db.String(255))
    confirmar_clave = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'foto_perfil': self.foto_perfil,
            'correo': self.correo,
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'fecha_nacimiento': self.fecha_nacimiento,
            'nombre_usuario': self.nombre_usuario,
            'clave': self.clave,
            'confirmar_clave': self.confirmar_clave
        }
