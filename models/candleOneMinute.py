from db import db

class CandleOneMinuteModel(db.Model):
  __tablename__ = 'CandleOneMinute'

  id = db.Column(db.Integer, primary_key=True)
  datetime = db.Column(db.Date, nullable=False)
  open = db.Column(db.Float, nullable=False)
  low = db.Column(db.Float, nullable=False)
  high = db.Column(db.Float, nullable=False)
  close = db.Column(db.Float, nullable=False)

  def __init__(self, datetime, open, low, high, close):
    self.datetime = datetime
    self.open = open
    self.low = low
    self.high = high
    self.close = close

  def json(self, ):
    return {
      'datetime': self.datetime,
      'open': self.open,
      'low': self.low,
      'high': self.high,
      'close': self.close
    }

  @classmethod
  def find_all(cls):
    return cls.query.all()

  def save_to_db(self, ):
    db.session.add(self)
    db.session.commit()
