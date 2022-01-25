from flask import Request
from flask_restplus import Resource, fields

from models.candleOneMinute import CandleOneMinuteModel
from schemas.candleOneMinute import CandleOneMinuteSchema

from server.instance import server

candle_ns = server.candle_ns
candle_schema = CandleOneMinuteSchema()

class CandleOneMinute(Resource):
  def get(self, datetime):
    candle_data = CandleOneMinuteModel.find_by_datetime(datetime)
    if candle_data:
      return candle_schema.dump(candle_data), 200
    
    return {'message': 'Datetime not found!'}, 404
