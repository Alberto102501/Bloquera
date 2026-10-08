from flask import Blueprint, jsonify

productos_bp = Blueprint('productos_bp', __name__)

@productos_bp.route('/', methods=['GET'])
def listar_productos():
    # Más adelante aquí haremos: productos = Producto.query.all()
    # y devolveremos lo que el Admin haya guardado en PostgreSQL.
    return jsonify({
        "status": "success",
        "data": []
    }), 200