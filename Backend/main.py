# trafico/backend/main.py
from flask import Flask, jsonify
from flask_cors import CORS
from modelos.redondel import Redondel
import time

app = Flask(__name__)
CORS(app)

# Instancia global del redondel
simulacion = Redondel(num_carros=12)

@app.route("/api/estado")
def obtener_estado():
    # Avanzamos un paso la simulación cada vez que el frontend pregunta
    # (O podrías usar un hilo separado, pero esto es más simple para empezar)
    simulacion.siguiente_paso()
    return jsonify(simulacion.obtener_estado())

@app.route("/api/frenar/<id>", methods=["POST"])
def evento_frenar(id):
    simulacion.frenar_carro(id)
    return jsonify({"mensaje": f"Carro {id} frenando"})

@app.route("/api/reiniciar", methods=["POST"])
def reiniciar():
    global simulacion
    simulacion = Redondel(num_carros=12)
    return jsonify({"mensaje": "Simulación reiniciada"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)