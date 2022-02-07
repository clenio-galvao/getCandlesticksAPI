from ma import ma
from models.candle import CandleModel

class CandleSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = CandleModel
    load_instance = True
