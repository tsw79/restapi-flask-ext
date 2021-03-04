import logging
import click
from api.models.user import User
from flask.cli import AppGroup

log = logging.getLogger(__name__)
user_cli = AppGroup('user', short_help="Run user commands in the app context.")

#
# Register all functions
def register(app):

  @user_cli.command('create')
  @click.argument('name')
  @click.argument('username')
  @click.argument('email')
  @click.argument('password')
  def new_user(name, username, email, password):
    user = User()
    user.name = name
    user.username = username
    user.email = email
    user.password = password
    user.hash_password()
    try:
      user.save()
      print("User with username `%s` has been added successfully." % (username))
    except Exception as e:
      log.error("Failed to add new user, %s. Error: %s" % (username, e))
        
  app.cli.add_command(user_cli)
    