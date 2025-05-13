from sqlalchemy import Column, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
import uuid
import datetime

Base = declarative_base()

class PokerSession(Base):
    __tablename__ = 'poker_sessions'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    source = Column(String)

class Player(Base):
    __tablename__ = 'players'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String, ForeignKey('poker_sessions.id'))
    name = Column(String)
    stack = Column(Float)

class ImageRecord(Base):
    __tablename__ = 'images'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String, ForeignKey('poker_sessions.id'))
    base64_data = Column(Text)
