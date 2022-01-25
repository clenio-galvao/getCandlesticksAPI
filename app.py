from flask import jsonify
from marshmallow import ValidationError

from ma import ma
from db import db
from controllers.candleOneMinute import CandleOneMinute

from server.instance import server

api = server.api
app = server.app

@app.before_first_request
def create_table():
  db.create_all()

api.add_resource(CandleOneMinute, '/CandleOneMinute')

if __name__ == '__main__':
  db.init_app(app)
  ma.init_app(app)
  server.run()
