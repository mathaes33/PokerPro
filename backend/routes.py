# backend/routes.py

from flask import Flask, request, jsonify
from models import db, Session
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokerpro.db'
db.init_app(app)

@app.route('/ocr', methods=['POST'])
def ocr():
    image = request.files['image']
    image_path = os.path.join('uploads', image.filename)
    image.save(image_path)

    # Perform OCR and strategy analysis here
    ocr_text = perform_ocr(image_path)
    recommendation = analyze_strategy(ocr_text)

    session = Session(ocr_text=ocr_text, recommendation=recommendation, image_path=image_path)
    db.session.add(session)
    db.session.commit()

    return jsonify({'ocr_text': ocr_text, 'recommendation': recommendation})