# /flask/app/turismo/crud.py

from app import db
from app.turismo.models import Turismo

def create_turismo(data):
    nuevo_turismo = Turismo(
        nombre_del_sitio=data.get('nombre_del_sitio'),
        provincia=data.get('provincia'),
        pais=data.get('pais'),
        descripcion_de_los_atractivos=data.get('descripcion_de_los_atractivos'),
        foto_del_lugar=data.get('foto_del_lugar'),
        medios_de_transporte=data.get('medios_de_transporte'),
        forma_de_llegar=data.get('forma_de_llegar')
    )
    db.session.add(nuevo_turismo)
    db.session.commit()
    return nuevo_turismo

def get_turismo(turismo_id):
    return Turismo.query.get_or_404(turismo_id)

def get_all_turismos():
    return Turismo.query.all()

def update_turismo(turismo_id, data):
    turismo = get_turismo(turismo_id)
    turismo.nombre_del_sitio = data.get('nombre_del_sitio', turismo.nombre_del_sitio)
    turismo.provincia = data.get('provincia', turismo.provincia)
    turismo.pais = data.get('pais', turismo.pais)
    turismo.descripcion_de_los_atractivos = data.get('descripcion_de_los_atractivos', turismo.descripcion_de_los_atractivos)
    turismo.foto_del_lugar = data.get('foto_del_lugar', turismo.foto_del_lugar)
    turismo.medios_de_transporte = data.get('medios_de_transporte', turismo.medios_de_transporte)
    turismo.forma_de_llegar = data.get('forma_de_llegar', turismo.forma_de_llegar)
    
    db.session.commit()
    return turismo

def delete_turismo(turismo_id):
    turismo = get_turismo(turismo_id)
    db.session.delete(turismo)
    db.session.commit()
    return turismo
