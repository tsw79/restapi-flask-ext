from api.resources.movie import MoviesApi, MovieApi

def init_movie_routes(api):
  api.add_resource(MoviesApi, '/api/v1/movies')
  api.add_resource(MovieApi, '/api/v1/movies/<id>')