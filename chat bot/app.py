from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.json["msg"].lower()

    # Rule-based responses
    if user_input in ["hi", "hello", "hey"]:
        response = "Hello! How can I help you?"
    elif "how are you" in user_input:
        response = "I'm doing well, thank you! 😊"
    elif "your name" in user_input:
        response = "I'm your rule-based chatbot, coded by Sparsh!"
    elif "bye" in user_input:
        response = "Goodbye! Take care. 👋"
    elif "help" in user_input:
        response = "Try asking me: 'your name', 'how are you', 'bye', etc."
    else:
        response = "Sorry, I didn't get that. Try asking something else."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
