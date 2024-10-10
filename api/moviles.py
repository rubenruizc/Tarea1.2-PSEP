from flask import *

app = Flask(__name__)

# Lista de móviles
moviles = [
    {"idMóvil": 1, "Precio Coste Móvil": 200, "Precio Venta Móvil": 300, "idPersona": 1},
    {"idMóvil": 2, "Precio Coste Móvil": 250, "Precio Venta Móvil": 350, "idPersona": 2},
]

# Método para encontrar el próximo ID de móvil
def find_next_id():
    return max(movil["idMovil"] for movil in moviles) + 1

# Ruta principal
@app.route("/")
def index():
    return "¡Bienvenidos a la API de gestión de moviles!"

# Método GET para obtener todos los móviles
@app.get("/moviles")
def get_moviles():
    return jsonify(moviles)

# Método GET para obtener un móvil por su ID
@app.get("/moviles/<int:idMovil>")
def get_movil(idMóvil):
    for movil in moviles:
        if movil["idMovil"] == idMóvil:
            return jsonify(movil), 200
    return {"error": "Movil no encontrado"}, 404

# Método POST para agregar un nuevo móvil
@app.post("/moviles")
def add_movil():
    if request.is_json:
        nuevo_movil = request.get_json()
        nuevo_movil["idMovil"] = find_next_id()
        moviles.append(nuevo_movil)
        return jsonify(nuevo_movil), 201
    return {"error": "La solicitud debe ser en formato JSON"}, 415

# Método PUT para actualizar completamente un móvil
@app.put("/moviles/<int:idMovil>")
def update_movil(idMóvil):
    if request.is_json:
        movil_modificado = request.get_json()
        for movil in moviles:
            if movil["idMovil"] == idMóvil:
                movil.update(movil_modificado)
                return jsonify(movil), 200
        return {"error": "Movil no encontrado"}, 404
    return {"error": "La solicitud debe ser en formato JSON"}, 415

# Método PATCH para actualizar parcialmente un móvil
@app.patch("/moviles/<int:idMovil>")
def partial_update_movil(idMóvil):
    if request.is_json:
        datos_modificados = request.get_json()
        for movil in moviles:
            if movil["idMovil"] == idMóvil:
                movil.update(datos_modificados)
                return jsonify(movil), 200
        return {"error": "Movil no encontrado"}, 404
    return {"error": "La solicitud debe ser en formato JSON"}, 415

# Método DELETE para eliminar un móvil por su ID
@app.delete("/moviles/<int:idMovil>")
def delete_movil(idMóvil):
    for movil in moviles:
        if movil["idMovil"] == idMóvil:
            moviles.remove(movil)
            return {"mensaje": "Movil eliminado con éxito"}, 200
    return {"error": "Movil no encontrado"}, 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)