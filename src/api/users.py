from flask_restful import Resource, reqparse, request

from db.users.get_user import get_all_users, get_user
from db.users.create_user import create_user
from db.users.update_user import update_user
from db.users.delete_user import delete_user
from db.sessions.get_session import SessionExpiredError, get_session

# TODO: remove password from GET request
def user_tuple_to_object(user: tuple):
  """
  Converts a tuple containing user data to a JSON-serializable object.

  Parameters: 
    user (tuple) - user information in the format
    (user_id, account_name, email, password, display_name, bio)

  Returns:
    user_obj (dict) - user information in the format
    {id: user_id, name: account_name, email: email,
    display_name: display_name, bio: bio}
  """
  if(user is None or len(user) == 0):
    return {"message": f"Provided user data is null or empty."} 

  return {
    "name": user[1],
    "email": user[2],
    "display_name": user[4],
    "bio": user[5]
  }

class Users(Resource):
  def get(self):
    users = get_all_users()

    userList = []
    for user in users:
      userList.append(user_tuple_to_object(user))

    # include total number of users
    return {
      "count": len(userList),
      "result": userList
    }
  
  def post(self):
    user_parser = reqparse.RequestParser(bundle_errors=True)
    user_parser.add_argument(
      'name', type=str, location='json', required=True, 
      help="Name is a required field"
    )
    user_parser.add_argument(
      'email', type=str, location='json', required=True, 
      help="Email is a required field"
    )
    user_parser.add_argument(
      'password', type=str, location='json', required=True,
      help='Password is a required field'
    )
    user_parser.add_argument(
      'display_name', type=str, location='json',
      help='Name that is shown when viewing the account'
    )
    user_parser.add_argument(
      'bio', type=str, location='json',
      help='A description about the user'
    )
    args = user_parser.parse_args(strict=True)
    new_user = create_user(args['name'], args['email'], args['password'], args['display_name'], args['bio'])
    return user_tuple_to_object(new_user)

  
class User(Resource):
  def get(self, user_id):
    user = get_user(user_id)

    if(user is None):
      return {"message": f"Could not find a user with the id {user_id}"}

    return user_tuple_to_object(user)
  
  def put(self, user_id):

    # validate session
    session_id = request.headers.get('session-id')

    if not session_id:
      return {'message': 'Session ID required.'}, 400
    
    try:
      logout_result = get_session(session_id)
    except SessionExpiredError as e:
      return {'message': 'The session has expired. Please re-enter your credentials.'}, e.args[1]
      
    if(logout_result is None or user_id != logout_result[0]):
      return {'message': 'Invalid credentials. Access denied.'}, 401

    user_parser = reqparse.RequestParser(bundle_errors=True)
    user_parser.add_argument(
      'name', type=str, location='json', 
      help="Name is a required field"
    )
    user_parser.add_argument(
      'email', type=str, location='json', 
      help="Email is a required field"
    )
    user_parser.add_argument(
      'password', type=str, location='json',
      help='Password is a required field'
    )
    user_parser.add_argument(
      'display_name', type=str, location='json',
      help='Name that is shown when viewing the account'
    )
    user_parser.add_argument(
      'bio', type=str, location='json',
      help='A description about the user'
    )
    args = user_parser.parse_args(strict=True)
    updated_user = update_user(user_id, args)
    return user_tuple_to_object(updated_user)
  
  def delete(self, user_id):
    # validate session
    session_id = request.headers.get('session-id')

    if not session_id:
      return {'message': 'Session ID required.'}, 400
    
    try:
      logout_result = get_session(session_id)
    except SessionExpiredError as e:
      return {'message': 'The session has expired. Please re-enter your credentials.'}, e.args[1]

    if(logout_result is None or user_id != logout_result[0]):
      return {'message': 'Invalid credentials. Access denied.'}, 401

    deleted_user = delete_user(user_id)

    return user_tuple_to_object(deleted_user)





