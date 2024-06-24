# /flask/app/restaurantes/crud.py

from app import db
from app.restaurants.models import Restaurant

def create_restaurant(data):
    nuevo_restaurant = Restaurant(
        nombre=data.get('nombre'),
        valoracion=data.get('valoracion'),
        telefono=data.get('telefono'),
        sitio_web=data.get('sitio_web'),
        horario_atencion=data.get('horario_atencion'),
        comentarios=data.get('comentarios'),
        hacer_reserva=data.get('hacer_reserva'),
        foto=data.get('foto')
    )
    db.session.add(nuevo_restaurant)
    db.session.commit()
    return nuevo_restaurant

def get_restaurant(restaurant_id):
    return Restaurant.query.get_or_404(restaurant_id)

def get_all_restaurants():
    return Restaurant.query.all()

def update_restaurant(restaurant_id, data):
    restaurant = get_restaurant(restaurant_id)
    restaurant.nombre = data.get('nombre', restaurant.nombre)
    restaurant.valoracion = data.get('valoracion', restaurant.valoracion)
    restaurant.telefono = data.get('telefono', restaurant.telefono)
    restaurant.sitio_web = data.get('sitio_web', restaurant.sitio_web)
    restaurant.horario_atencion = data.get('horario_atencion', restaurant.horario_atencion)
    restaurant.comentarios = data.get('comentarios', restaurant.comentarios)
    restaurant.hacer_reserva = data.get('hacer_reserva', restaurant.hacer_reserva)
    restaurant.foto = data.get('foto', restaurant.foto)
    
    db.session.commit()
    return restaurant

def delete_restaurant(restaurant_id):
    restaurant = get_restaurant(restaurant_id)
    db.session.delete(restaurant)
    db.session.commit()
    return restaurant
