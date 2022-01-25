from flask import Flask, Blueprint
from flask_restplus import Api
import mysql.connector
class Server():
  def __init__(self, ):
    self.app = Flask(__name__)
    self.blueprint = Blueprint('api', __name__, url_prefix='/api')
    self.api = Api(self.blueprint, doc='/doc', title='Api para candleSticks')

    self.app.register_blueprint(self.blueprint)

    self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://clenio:Cgm2703.@localhost/candlesticks'
    self.app.config['PROPAGATE_EXCEPTIONS'] = True
    self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  
  def run(self, ):
    self.app.run(
      port=5000,
      debug=True,
      host='0.0.0.0'
    )

server = Server()
