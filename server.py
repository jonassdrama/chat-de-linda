from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Ruta para la página de inicio (evita error 404 en "/")
@app.route("/")
def home():
    return "<h1>Linda está en línea ✅</h1><p>Para hablar con Linda, usa la ruta /chat.</p>"

# Configurar la API de OpenAI
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



