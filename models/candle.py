from db import db

class CandleModel(db.Model):
  __tablename__ = 'Candle'

  id = db.Column(db.Integer, primary_key=True)
  moeda = db.Column(db.String(50), nullable=False)
  periodicidade = db.Column(db.Integer, nullable=False)
  datetime = db.Column(db.Date, nullable=False)
  abertura = db.Column(db.Float, nullable=False)
  minima = db.Column(db.Float, nullable=False)
  maxima = db.Column(db.Float, nullable=False)
  fechamento = db.Column(db.Float, nullable=False)

  def __init__(self, moeda, periodicidade, datetime, abertura, minima, maxima, fechamento):
    self.datetime = datetime
    self.moeda = moeda
    self.periodicidade = periodicidade
    self.abertura = abertura
    self.minima = minima
    self.maxima = maxima
    self.fechamento = fechamento

  @classmethod
  def find_all(cls):
    return cls.query.all()

  def save_to_db(self, ):
    db.session.add(self)
    db.session.commit()
