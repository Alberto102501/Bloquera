from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    telefono = db.Column(db.String(20), nullable=True)
    password_hash = db.Column(db.String(255), nullable=False)
    
    # Rol del usuario: 'admin' o 'cliente'
    rol = db.Column(db.String(20), nullable=False, default='cliente')
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Métodos para encriptar y verificar contraseñas
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Convierte el objeto a diccionario para responder JSON a React"""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "telefono": self.telefono,
            "rol": self.rol,
            "created_at": self.created_at.isoformat()
        }