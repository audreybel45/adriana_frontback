# /flask/app/restaurantes/models.py

from app import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    valoracion = db.Column(db.Integer)  # Valoración en puntos de 1 a 5
    telefono = db.Column(db.String(20))
    sitio_web = db.Column(db.String(255))
    horario_atencion = db.Column(db.Text)
    comentarios = db.Column(db.Text)
    hacer_reserva = db.Column(db.Boolean)  # Indica si se puede hacer reserva
    foto = db.Column(db.String(255))  # URL del archivo de imagen

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'valoracion': self.valoracion,
            'telefono': self.telefono,
            'sitio_web': self.sitio_web,
            'horario_atencion': self.horario_atencion,
            'comentarios': self.comentarios,
            'hacer_reserva': self.hacer_reserva,
            'foto': self.foto
        }
