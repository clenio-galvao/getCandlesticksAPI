from flask import request
from flask_restplus import Resource, fields

from models.candleOneMinute import CandleOneMinuteModel
from schemas.candleOneMinute import CandleOneMinuteSchema

from server.instance import server

candle_schema = CandleOneMinuteSchema()
candle_list_schema = CandleOneMinuteSchema(many=True)

class CandleOneMinuteList(Resource):
  def get(self, ):
    candle_data = CandleOneMinuteModel.find_all()
    if candle_data:
      return candle_schema.dump(candle_data), 200
    
    return {'message': 'no candles sorry!'}, 404
  
  def post(self, ):
    candle_json = request.get_json()
    candle_data = candle_schema.load(candle_json)

    candle_data.save_to_db()

    return candle_schema.dump(candle_data), 201
