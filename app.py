from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a root route to handle requests to "/"
@app.route('/')
def home():
    return "Welcome to the AIOTICS DevOps Chatbot!", 200

# Define a chatbot endpoint
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No input provided'}), 400

    # Simple chatbot response logic
    responses = {
        "hello": "Hello! How can I assist you with DevOps today?",
        "jenkins": "Jenkins is an automation server used for building CI/CD pipelines.",
        "docker": "Docker is a platform for containerizing applications."
    }
    response = responses.get(user_input.lower(), "I'm sorry, I didn't understand that. Can you rephrase?")
    return jsonify({'response': response}), 200

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)

