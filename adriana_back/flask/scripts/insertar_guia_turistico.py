import mysql.connector
import json

def insert_guia_turistico():
    try:
        # Establecer la conexión con el servidor MySQL
        connection = mysql.connector.connect(
            host='localhost',
            database='el_nomada',
            user='audrey45',       # Reemplaza con tu usuario de MySQL
            password='Agusandy136'  # Reemplaza con tu contraseña de MySQL
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Datos de contacto como un diccionario
            contacto = {
                "email": "guia@example.com",
                "telefono": "+543885273263"
            }

            # Convertir el diccionario a JSON
            contacto_json = json.dumps(contacto)

            # Insertar un nuevo registro en la tabla 'guias_turisticos'
            cursor.execute("""
                INSERT INTO guias_turisticos (nombre, contacto, ubicacion, servicios, precio, idiomas)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, ('Guía Ejemplo', contacto_json, 'Buenos Aires', 'recepcion, itinerario', 'medio', 'espanol, ingles'))

            connection.commit()
            print("Guía turístico agregado.")

    except Error as e:
        print(f"Error al conectar con MySQL: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión con MySQL cerrada.")

if __name__ == "__main__":
    insert_guia_turistico()
