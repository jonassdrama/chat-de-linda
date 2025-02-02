from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Permite CORS para todas las conexiones

# Ruta para evitar error 404
@app.route("/")
def home():
    return "<h1>Linda está en línea ✅</h1><p>Para hablar con Linda, usa la ruta /chat.</p>"

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("message", "")

    if not mensaje:
        return jsonify({"response": "Por favor, escribe un mensaje."})

    try:
        respuesta = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "Eres Linda, una asesora de modelos de contenido digital."},
                {"role": "user", "content": mensaje}
            ]
        )

        return jsonify({"response": respuesta.choices[0].message.content})

    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)




