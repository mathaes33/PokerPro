from flask import Flask, request, jsonify
from flask_cors import CORS
from ocr_parser import parse_image_ocr  # your OCR logic
from strategy_engine import recommend_action  # your strategy logic

app = Flask(__name__)
CORS(app)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    image = request.files['image']
    game_state = parse_image_ocr(image)
    return jsonify({'game_state': game_state})

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if 'game_state' not in data:
        return jsonify({'error': 'No game_state provided'}), 400
    action = recommend_action(data['game_state'])
    return jsonify({'recommended_action': action})

if __name__ == '__main__':
    app.run(debug=True)