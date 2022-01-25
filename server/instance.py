from distutils.log import debug
from flask import Flask, Blueprint
from flask_restplus import Api

class Server():
  def __init__(self, ):
    self.app = Flask(__name__)
    self.blueprint = Blueprint('api', __name__, url_prefix='/api')
    self.api = Api(self.blueprint, doc='/doc', title='Api para candleSticks')

    self.app.register_blueprint(self.blueprint)

    self.app.config['SQLALCHEMI_DATABASE_URI'] = 'mysql/root'
    self.app.config['PROPAGATE_EXCEPTIONS'] = True
    self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    self.candle_ns = self.candle_ns()

  def candle_ns(self, ):
    return self.api.namespace(name='Candles', description='candles related operations', path='/')
  
  def run(self, ):
    self.app.run(
      port=5000,
      debug=True,
      host='0.0.0.0'
    )

server = Server()
