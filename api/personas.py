from flask import *

app = Flask(__name__)

# Lista de personas
personas = [
    {"id": 1, "DNI": "12345678A", "nombre": "Rubén", "apellidos": "Ruiz Castaño", "teléfono": 123456789, "correo": "ruben@example.com"},
    {"id": 2, "DNI": "23456789B", "nombre": "Laura", "apellidos": "García López", "teléfono": 987654321, "correo": "laura@example.com"},
]

# Método para encontrar el próximo ID
def find_next_id():
    return max(persona["id"] for persona in personas) + 1

# Ruta principal
@app.route("/")
def index():
    return "¡Bienvenidos a la API de personas!"

# Método GET para obtener todas las personas
@app.get("/personas")
def get_personas():
    return jsonify(personas)

# Método GET para obtener una persona por su ID
@app.get("/personas/<int:id>")
def get_persona(id):
    for persona in personas:
        if persona["id"] == id:
            return jsonify(persona), 200
    return {"error": "Persona no encontrada"}, 404

# Método POST para agregar una nueva persona
@app.post("/personas")
def add_persona():
    if request.is_json:
        nueva_persona = request.get_json()
        nueva_persona["id"] = find_next_id()
        personas.append(nueva_persona)
        return jsonify(nueva_persona), 201
    return {"error": "La solicitud debe ser en formato JSON"}, 415

# Método PUT para actualizar una persona completa
@app.put("/personas/<int:id>")
def update_persona(id):
    if request.is_json:
        persona_modificada = request.get_json()
        for persona in personas:
            if persona["id"] == id:
                persona.update(persona_modificada)
                return jsonify(persona), 200
        return {"error": "Persona no encontrada"}, 404
    return {"error": "La solicitud debe ser en formato JSON"}, 415

# Método PATCH para actualizar parcialmente una persona
@app.patch("/personas/<int:id>")
def partial_update_persona(id):
    if request.is_json:
        datos_modificados = request.get_json()
        for persona in personas:
            if persona["id"] == id:
                persona.update(datos_modificados)
                return jsonify(persona), 200
        return {"error": "Persona no encontrada"}, 404
    return {"error": "La solicitud debe ser en formato JSON"}, 415

# Método DELETE para eliminar una persona por su ID
@app.delete("/personas/<int:id>")
def delete_persona(id):
    for persona in personas:
        if persona["id"] == id:
            personas.remove(persona)
            return {"mensaje": "Persona eliminada con éxito"}, 200
    return {"error": "Persona no encontrada"}, 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)