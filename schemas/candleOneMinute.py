from ma import ma
from models.candleOneMinute import CandleOneMinuteModel

class CandleOneMinuteSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = CandleOneMinuteModel
    load_instance = True
