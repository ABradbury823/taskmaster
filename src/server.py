from flask import *
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
  app.run(host='::', port=4500, debug=True)