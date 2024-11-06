from flask import *
from flask_restful import Api

from api.root import Root
from api.tasks import Tasks
from api.taskboards import Taskboards
from api.taskboard import Taskboard
from api.categories import Categories
from api.teams import Teams

app = Flask(__name__)
api = Api(app)

api.add_resource(Root, '/')
api.add_resource(Tasks, '/tasks')
api.add_resource(Taskboards, '/taskboards')
api.add_resource(Taskboard, '/taskboards/<int:id>')
api.add_resource(Categories, '/categories')
api.add_resource(Teams, '/teams')

if __name__ == '__main__':
  app.run(host='::', port=4500, debug=True)