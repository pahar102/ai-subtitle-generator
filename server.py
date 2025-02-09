from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Subtitle Generator Backend is Running!"

@app.route('/generate-subtitles', methods=['POST'])
def generate_subtitles():
    # Abhi hum sirf ek dummy response bhej rahe hain
    return jsonify({"subtitles": ["Hello, this is a dummy subtitle!", "This is just for testing."]})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
