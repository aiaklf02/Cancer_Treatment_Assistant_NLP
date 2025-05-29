from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    # Ici on simule une réponse simple, tu pourras remplacer par un vrai modèle NLP plus tard
    if "cancer" in user_input.lower():
        reply = "Les options de traitement du cancer dépendent du type et du stade."
    elif "side effects" in user_input.lower():
        reply = "Les effets secondaires communs sont la fatigue, les nausées et la perte d’appétit."
    else:
        reply = "Pouvez-vous reformuler votre question ?"
    return jsonify({'response': reply})

if __name__ == '__main__':
    app.run(debug=True)
