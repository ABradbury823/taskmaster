from flask import *
from flask_restful import Api

from api.root import Root
from api.users import Users, User
from api.tasks import Tasks
from api.sessions import Login, Logout
from api.task import Task

app = Flask(__name__)
api = Api(app)

api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout/<int:user_id>')
api.add_resource(Root, '/')
api.add_resource(Tasks, '/tasks')
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(Task, '/tasks/<int:id>')

if __name__ == '__main__':
  app.run(host='::', port=4500, debug=True)