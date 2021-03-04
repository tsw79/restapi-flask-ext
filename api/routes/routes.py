from .movie import init_movie_routes
from .auth import init_auth_routes

def init_routes(api):
  init_movie_routes(api)
  init_auth_routes(api)