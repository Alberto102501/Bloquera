from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Permitir peticiones desde React
    CORS(app)

    # Inicializar Base de Datos, Migraciones y JWT
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Registrar rutas (Blueprints)
    from app.routes.auth_routes import auth_bp
    from app.routes.productos_routes import productos_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(productos_bp, url_prefix='/api/productos')

    return app