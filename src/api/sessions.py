from flask_restful import Resource, request, reqparse

from db.sessions.get_session import get_session,validate_user_creds
from db.sessions.create_session import create_session
from db.sessions.delete_session import delete_session

class Login(Resource):
  def post(self):
    # define parser and request args
    parser = reqparse.RequestParser()
    parser.add_argument(
      'username', type=str, location='json', required=True, 
      help='Username is a required field'
    )
    parser.add_argument(
      'password', type=str, location='json', required=True,
      help='Password is a required field'
    )
    parser.add_argument(
     'expires_at', type=str, location='json', required=False,
     help='The time when the session expires, in ISO format. Default = never expires' 
    )
    args = parser.parse_args(strict=True)

    username = args['username']
    password = args['password']
    if('expires_at' in args and args['expires_at'] is not None): expires_at = args['expires_at']
    else: expires_at = 'infinity'

    return log_in(username, password, expires_at)
  
def log_in(username: str, password: str, expires_at: str):
  """
  Processes a user log-in request.

  Parameters:
    username (str) - The inputted username.
    password (str) - The inputted password.
    expires_at (str) - When the session id expires.

  Returns:
    login_results (dict) - A dictionary with information on whether the login attempt was successful.
  """

  # check db for valid username and password
  user_id = validate_user_creds(username, password)

  login_results = {}

  if(user_id is None):
    login_results['message'] = 'Invalid credentials. Access denied.'
  # generate session key and set it on user
  else:
    session_id = create_session(user_id, expires_at)
    login_results['message'] = 'Log-in successful. A session id has been made.'
    login_results['user_id'] = user_id
    login_results['session_id'] = session_id
    login_results['expires_at'] = expires_at

  return login_results

class Logout(Resource):
  def post(self, user_id):

    session_id = request.headers.get('session-id')

    if not session_id:
      return {'message': 'Session ID required.'}, 400
    
    logout_result = get_session(session_id)

    if(logout_result is None or user_id != logout_result):
      return {'message': 'Invalid credentials. Access denied.'}, 401

    return logout(session_id, user_id)

def logout(session_id: str, user_id: int):
  """Attempt to log out a user, give result as dictionary."""
  
  delete_session(session_id)

  return {'message': 'Logout successful.'}, 200