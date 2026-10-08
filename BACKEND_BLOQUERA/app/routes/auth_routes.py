from flask import Blueprint, request, jsonify
from app import db
from app.models.usuario import Usuario
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/registro', methods=['POST'])
def registro():
    data = request.get_json() or {}

    # Validaciones básicas
    if not data.get('nombre') or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Nombre, email y password son obligatorios"}), 400

    if Usuario.query.filter_by(email=data['email']).first():
        return jsonify({"error": "El correo ya se encuentra registrado"}), 409

    # Crear nuevo usuario (por defecto rol cliente)
    nuevo_usuario = Usuario(
        nombre=data['nombre'],
        email=data['email'],
        telefono=data.get('telefono'),
        rol='cliente'
    )
    nuevo_usuario.set_password(data['password'])

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({
        "mensaje": "Usuario registrado exitosamente",
        "usuario": nuevo_usuario.to_dict()
    }), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email y contraseña requeridos"}), 400

    usuario = Usuario.query.filter_by(email=email).first()

    # Verificar credenciales
    if not usuario or not usuario.check_password(password):
        return jsonify({"error": "Credenciales inválidas"}), 401

    # Crear token JWT guardando el ID y el ROL del usuario
    token = create_access_token(
        identity=str(usuario.id),
        additional_claims={"rol": usuario.rol, "nombre": usuario.nombre}
    )

    return jsonify({
        "mensaje": "Inicio de sesión correcto",
        "token": token,
        "usuario": usuario.to_dict()
    }), 200