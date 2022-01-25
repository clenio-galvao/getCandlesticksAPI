from datetime import datetime
from db import db

class CandleOneMinuteModel(db.Model):
  __tablename__ = 'candleoneminute'

  id = db.Column(db.integer, primary_hey=True)
  datetime = db.Column(db.datetime, nullable=False)
  open = db.Column(db.number, nullable=False)
  low = db.Column(db.number, nullable=False)
  high = db.Column(db.number, nullable=False)
  close = db.Column(db.number, nullable=False)

  def __init__(self, datetime, open, low, high, close):
    self.datetime = datetime
    self.open = open
    self.low = low
    self.high = high
    self.close = close

  def __repr__(self, ):
    return f'CandleOneMinuteModel(datetime={self.datetime}'

  def json(self, ):
    return {
      'datetime': self.datetime,
      'open': self.open,
      'low': self.low,
      'high': self.high,
      'close': self.close
    }

  @classmethod
  def find_by_datetime(cls, datetime):
    return cls.query.filter_by(datetime=datetime).first()

  @classmethod
  def find_all(cls):
    return cls.query.all()

  def save_to_db(self, ):
    db.session.add(self)
    db.session.commit()
