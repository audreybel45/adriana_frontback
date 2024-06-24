import os
# /flask/app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS  # Importar CORS desde flask_cors

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar los módulos (blueprints)
    from app.usuarios.routes import usuarios_bp
    from app.turismo.routes import turismo_bp
    from app.restaurants.routes import restaurants_bp  
    from app.guias_turisticos.routes import guias_turisticos_bp

    app.register_blueprint(usuarios_bp, url_prefix='/api/usuarios')
    app.register_blueprint(turismo_bp, url_prefix='/api/turismo')
    app.register_blueprint(restaurants_bp, url_prefix='/api/restaurants')  
    app.register_blueprint(guias_turisticos_bp, url_prefix='/api/guias_turisticos')

    return app
