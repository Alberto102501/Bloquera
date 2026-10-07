from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "ok", "mensaje": "API de Bloquera corriendo"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)