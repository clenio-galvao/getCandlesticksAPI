from flask import jsonify
from marshmallow import ValidationError

from ma import ma
from db import db
from controllers.candle import CandleList

from server.instance import server
from util.candleMaker import candle_maker

api = server.api
app = server.app

@app.before_first_request
def create_tables():
  db.create_all()

api.add_resource(CandleList, '/Candles')

db.init_app(app)
ma.init_app(app)
server.run()

candle_maker(10, 'USDT_BTC')
