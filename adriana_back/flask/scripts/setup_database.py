import mysql.connector
from mysql.connector import Error
import json 

def setup_database():
    try:
        # Establecer la conexión con el servidor MySQL
        connection = mysql.connector.connect(
            host='localhost',
            user='audrey45',       # Reemplaza el usuario de MySQL
            password='Agusandy136'  # Reemplaza la contraseña de MySQL
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Crear la base de datos
            cursor.execute("CREATE DATABASE IF NOT EXISTS el_nomada")
            print("Base de datos 'el_nomada' creada o ya existe.")

            # Usar la base de datos
            cursor.execute("USE el_nomada")

            # Crear la tabla 'usuarios'
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    foto_perfil VARCHAR(255),  -- URL del archivo de imagen
                    correo VARCHAR(255),
                    dni VARCHAR(8),
                    nombre VARCHAR(255),
                    apellido VARCHAR(255),
                    fecha_nacimiento DATE,
                    nombre_usuario VARCHAR(255),
                    clave VARCHAR(255),
                    confirmar_clave VARCHAR(255)
                )
            """)
            print("Tabla 'usuarios' creada.")

            # Crear la tabla 'turismo'
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS turismo (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre_del_sitio VARCHAR(255),
                    provincia VARCHAR(100),
                    pais VARCHAR(100),
                    descripcion_de_los_atractivos TEXT,
                    foto_del_lugar VARCHAR(255),  -- URL del archivo de imagen
                    medios_de_transporte TEXT,
                    forma_de_llegar TEXT
                )
            """)
            print("Tabla 'turismo' creada.")

            # Crear la tabla 'restaurants'
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS restaurants (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255),
                    valoracion INT,  -- Valoración en puntos de 1 a 5
                    telefono VARCHAR(20),
                    sitio_web VARCHAR(255),
                    horario_atencion TEXT,
                    comentarios TEXT,
                    hacer_reserva BOOLEAN,  -- Indica si se puede hacer reserva
                    foto VARCHAR(255)  -- URL del archivo de imagen
                )
            """)
            print("Tabla 'restaurants' creada.")

            # Crear la tabla 'guias_turisticos'
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS guias_turisticos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255),
                    foto VARCHAR(255),  -- URL del archivo de imagen
                    contacto JSON,  -- Campo JSON para almacenar email y teléfono
                    ubicacion VARCHAR(100),
                    servicios TEXT,
                    precio VARCHAR(50),
                    idiomas TEXT
                )
            """)
            print("Tabla 'guias_turisticos' creada.")

    except Error as e:
        print(f"Error al conectar con MySQL: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión con MySQL cerrada.")

if __name__ == "__main__":
    setup_database()
