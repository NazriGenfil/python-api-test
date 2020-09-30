from .movie import MoviesApi, MovieApi
from .auth import SignupApi

#jalur API
def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movies/<id>')

    api.add_resource(SignupApi, '/api/auth/signup')