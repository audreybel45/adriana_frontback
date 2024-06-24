# /flask/app/guias_turisticos/models.py

from app import db
import json

class GuiaTuristico(db.Model):
    __tablename__ = 'guias_turisticos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    contacto = db.Column(db.JSON, nullable=False)  # Campo JSON para email y teléfono
    ubicacion = db.Column(db.String(100), nullable=False)
    servicios = db.Column(db.Text, nullable=False)
    precio = db.Column(db.String(50), nullable=False)
    idiomas = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'contacto': self.contacto,
            'ubicacion': self.ubicacion,
            'servicios': self.servicios,
            'precio': self.precio,
            'idiomas': self.idiomas
        }
