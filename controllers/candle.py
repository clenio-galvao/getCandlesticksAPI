from flask import request
from flask_restplus import Resource, fields

from models.candle import CandleModel
from schemas.candle import CandleSchema

from server.instance import server

candle_schema = CandleSchema()
candle_list_schema = CandleSchema(many=True)

class CandleList(Resource):
  def get(self, ):
    candle_data = CandleModel.find_all()
    if candle_data:
      return candle_schema.dump(candle_data), 200
    
    return {'message': 'no candles sorry!'}, 404

  def post(candle_info):
    candle_json = candle_info
    candle_data = candle_schema.load(candle_json)

    candle_data.save_to_db()

    return candle_schema.dump(candle_data), 201
    