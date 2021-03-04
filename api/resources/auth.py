from flask import Response, request, render_template
from flask_jwt_extended import create_access_token, decode_token
from api.models.user import User
from flask_restful import Resource
import datetime
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from .errors import SchemaValidationError, EmailAlreadyExistsError, EmailNotExistsError, UnauthorizedError, InternalServerError, BadTokenError
from jwt.exceptions import ExpiredSignatureError, DecodeError, InvalidTokenError
from infrastructure.emailer import send_email

# Signup class
class SignupApi(Resource):
 def post(self):
  try:
    body = request.get_json()
    user = User(**body)
    user.hash_password()
    user.save()
    id = user.id
    return {'id': str(id)}, 200
  except FieldDoesNotExist:
    raise SchemaValidationError
  except NotUniqueError:
    raise EmailAlreadyExistsError
  except Exception as e:
    raise InternalServerError

# Login class
class LoginApi(Resource):
  def post(self):
    try:
      body = request.get_json()
      user = User.objects.get(email=body.get('email'))
      authorized = user.check_password(body.get('password'))

      if not authorized:
        return {'error': 'Email or password invalid'}, 401

      expires = datetime.timedelta(days=7)
      access_token = create_access_token(identity=str(user.id), expires_delta=expires)
      return {'token': access_token}, 200
    except (UnauthorizedError, DoesNotExist):
      raise UnauthorizedError
    except Exception as e:
      raise InternalServerError

# Forgot password class
class ForgotPasswordApi(Resource):
  def post(self):
    url = request.host_url + 'reset/'
    try:
      body = request.get_json()
      email = body.get('email')
      if not email:
        raise SchemaValidationError

      user = User.objects.get(email=email)
      if not user:
        raise EmailNotExistsError

      expires = datetime.timedelta(hours=24)
      access_token = create_access_token(identity=str(user.pk), expires_delta=expires)

      return send_email(
        '[MoviesDB] Reset Your Password',
        sender = 'me@moviesdb.com',
        recipients = [user.email],
        body_text = render_template('email/password_reset.txt', url=url + access_token),
        body_html = render_template('email/password_reset.html', url=url + access_token)
      )
    except SchemaValidationError:
      raise SchemaValidationError
    except EmailNotExistsError:
        raise EmailNotExistsError
    except Exception as e:
      raise InternalServerError

# Reset password class
class ResetPasswordApi(Resource):
  def post(self):
    url = request.host_url + 'reset/'
    try:
      body = request.get_json()
      access_token = body.get('access_token')
      password = body.get('password')

      if not access_token or not password:
        raise SchemaValidationError

      user_id = decode_token(access_token)['sub']
      user = User.objects.get(pk=user_id)
      user.modify(password=password)
      user.hash_password()
      user.save()

      return send_email(
        '[MoviesDB] Password reset successful',
        sender = 'support@moviesdb.com',
        recipients = [user.email],
        body_text = 'Password reset was successful',
        body_html = '<p>Password reset was successful</p>'
      )
    except SchemaValidationError:
      raise SchemaValidationError
    except ExpiredSignatureError:
      raise ExpiredTokenError
    except (DecodeError, InvalidTokenError):
      raise BadTokenError
    except Exception as e:
      raise InternalServerError