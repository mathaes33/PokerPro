# backend/models.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    ocr_text = db.Column(db.Text)
    recommendation = db.Column(db.String(50))
    image_path = db.Column(db.String(200))