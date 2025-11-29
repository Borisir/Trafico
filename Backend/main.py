from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ruta principal
@app.route("/")
def home():
    return "<h1>¡Bienvenido a mi aplicación Flask!</h1>"

# Ejemplo de ruta que devuelve JSON
@app.route("/api/saludo")
def saludo():
    return jsonify({
        "mensaje": "Hola desde la API Flask",
        "estado": "ok"
    })

if __name__ == "__main__":
    # debug=True reinicia el servidor automáticamente cuando detecta cambios
    app.run(debug=True, host="0.0.0.0", port=5000)
