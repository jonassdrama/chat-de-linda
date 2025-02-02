from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Carga la API Key desde las variables de entorno de Render
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("message", "")

    if not mensaje:
        return jsonify({"response": "Por favor, escribe un mensaje."})

    try:
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

respuesta = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[{"role": "system", "content": "Eres Linda, una asesora de modelos de contenido digital."},
              {"role": "user", "content": mensaje}]
        )

        return jsonify({"response": respuesta["choices"][0]["message"]["content"]})

    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

