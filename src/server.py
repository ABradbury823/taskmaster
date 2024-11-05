from flask import *
from flask_restful import Api

from api.root import Root
from api.tasks import Tasks

app = Flask(__name__)
api = Api(app)

api.add_resource(Root, '/')
api.add_resource(Tasks, '/tasks')

if __name__ == '__main__':
  app.run(host='::', port=4500, debug=True)