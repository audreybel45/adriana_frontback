# /flask/app/guias_turisticos/crud.py

import json 

from app import db
from app.guias_turisticos.models import GuiaTuristico

def create_guia_turistico(data):
    try:
        # Validar y asegurar que 'contacto' sea un diccionario antes de convertirlo a JSON
        contacto = data.get('contacto')
        if not isinstance(contacto, dict):
            raise ValueError("El campo 'contacto' debe ser un diccionario.")

        nuevo_guia = GuiaTuristico(
            nombre=data.get('nombre'),
            contacto=json.dumps(contacto),  # Convertimos el dict a string JSON
            ubicacion=data.get('ubicacion'),
            servicios=data.get('servicios'),
            precio=data.get('precio'),
            idiomas=data.get('idiomas')
        )
        db.session.add(nuevo_guia)
        db.session.commit()
        return nuevo_guia
    except Exception as e:
        # Manejo de errores de conversión o de base de datos
        print(f"Error al crear el guía turístico: {e}")
        return None

def get_guia_turistico(guia_id):
    return GuiaTuristico.query.get_or_404(guia_id)

def get_all_guias_turisticos():
    return GuiaTuristico.query.all()

def update_guia_turistico(guia_id, data):
    guia = get_guia_turistico(guia_id)
    
    contacto = data.get('contacto')
    if contacto and isinstance(contacto, dict):
        guia.contacto = json.dumps(contacto)  # Solo actualiza si 'contacto' es un dict

    guia.nombre = data.get('nombre', guia.nombre)
    guia.ubicacion = data.get('ubicacion', guia.ubicacion)
    guia.servicios = data.get('servicios', guia.servicios)
    guia.precio = data.get('precio', guia.precio)
    guia.idiomas = data.get('idiomas', guia.idiomas)
    
    db.session.commit()
    return guia

def delete_guia_turistico(guia_id):
    guia = get_guia_turistico(guia_id)
    db.session.delete(guia)
    db.session.commit()
    return guia
