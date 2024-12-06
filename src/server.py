from flask import *
from flask_restful import Api
from flask_cors import CORS

from api.root import Root
from api.users import Users, User
from api.tasks import Tasks
from api.sessions import Login, Logout
from api.task import Task
from api.taskboards import Taskboards
from api.taskboard import Taskboard
from api.categories import Categories
from api.teams import Teams

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout/<int:user_id>')
api.add_resource(Root, '/')
api.add_resource(Tasks, '/tasks')
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(Task, '/tasks/<int:id>')
api.add_resource(Taskboards, '/taskboards')
api.add_resource(Taskboard, '/taskboards/<int:id>')
api.add_resource(Categories, '/categories')
api.add_resource(Teams, '/teams')

if __name__ == '__main__':
  app.run(host='::', port=4500, debug=True)