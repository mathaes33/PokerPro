from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import re
from io import BytesIO

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr_image():
    file = request.files.get('image')
    if not file:
        return jsonify({"error": "No image uploaded"}), 400

    image = Image.open(file.stream)
    text = pytesseract.image_to_string(image)

    parsed = parse_poker_text(text)
    return jsonify({
        "raw_text": text,
        "parsed": parsed
    })

def parse_poker_text(text):
    players = re.findall(r'Player\s\d+: \$(\d+)', text)
    pot = re.search(r'Pot: \$([0-9.]+)', text)
    return {
        "players": players,
        "pot": float(pot.group(1)) if pot else 0
    }

if __name__ == '__main__':
    app.run(debug=True)