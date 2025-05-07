from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple chatbot responses
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm functioning well! How about you?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "name" in user_input:
        return "I'm MiniBot, your friendly neighborhood chatbot!"
    elif "help" in user_input:
        return "I can respond to greetings, tell you my name, and say goodbye. Try saying 'hello' or 'what's your name?'"
    else:
        return "I'm not sure I understand. Try asking something else or say 'help'."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    bot_response = get_bot_response(user_input)
    return jsonify({"bot_response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)