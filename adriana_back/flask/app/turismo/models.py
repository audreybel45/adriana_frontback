# /flask/app/turismo/models.py

from app import db

class Turismo(db.Model):
    __tablename__ = 'turismo'

    id = db.Column(db.Integer, primary_key=True)
    nombre_del_sitio = db.Column(db.String(255), nullable=False)
    provincia = db.Column(db.String(100), nullable=False)
    pais = db.Column(db.String(100), nullable=False)
    descripcion_de_los_atractivos = db.Column(db.Text, nullable=False)
    foto_del_lugar = db.Column(db.String(255))  # URL de la imagen
    medios_de_transporte = db.Column(db.Text, nullable=False)
    forma_de_llegar = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre_del_sitio': self.nombre_del_sitio,
            'provincia': self.provincia,
            'pais': self.pais,
            'descripcion_de_los_atractivos': self.descripcion_de_los_atractivos,
            'foto_del_lugar': self.foto_del_lugar,
            'medios_de_transporte': self.medios_de_transporte,
            'forma_de_llegar': self.forma_de_llegar
        }
