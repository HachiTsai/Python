from flask import Flask, request, jsonify, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """Detects the dominant emotion from the provided text."""
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"})

    return jsonify(result)

@app.route('/')
def index():
    """Renders the index.html template."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)