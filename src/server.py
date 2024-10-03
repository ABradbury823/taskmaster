from flask import *
from flask_restful import Api

from api.root import Root

app = Flask(__name__)
api = Api(app)

api.add_resource(Root, '/')

if __name__ == '__main__':
  app.run(host='::', port=4500, debug=True)