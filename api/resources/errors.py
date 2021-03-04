class InternalServerError(Exception):
  pass

class SchemaValidationError(Exception):
  pass

class MovieAlreadyExistsError(Exception):
  pass

class UpdatingMovieError(Exception):
  pass

class DeletingMovieError(Exception):
  pass

class MovieNotExistsError(Exception):
  pass

class EmailAlreadyExistsError(Exception):
  pass

class UnauthorizedError(Exception):
  pass

class EmailNotExistsError(Exception):
  pass

class BadTokenError(Exception):
  pass

errors = {
  "MovieNotExistsError": {
    "message": "Movie with given id doesn't exists",
    "status": 400
  },
  "EmailNotExistsError": {
    "message": "Email not found",
    "status": 400
  },
  "EmailAlreadyExistsError": {
    "message": "User with given email address already exists",
    "status": 400
  },
  "SchemaValidationError": {
    "message": "Request is missing required fields",
    "status": 400
  },
  "MovieAlreadyExistsError": {
    "message": "Movie with given name already exists",
    "status": 400
  },
  "UnauthorizedError": {
    "message": "Invalid username or password",
    "status": 401
  },
  "BadTokenError": {
    "message": "Token not valid",
    "status": 403
  },
  "UpdatingMovieError": {
    "message": "Updating movie added by other is forbidden",
    "status": 403
  },
  "DeletingMovieError": {
    "message": "Deleting movie added by other is forbidden",
    "status": 403
  },
  "InternalServerError": {
    "message": "Something went wrong",
    "status": 500
  },
}