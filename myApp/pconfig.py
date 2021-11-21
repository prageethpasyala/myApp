import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Info51987@127.0.0.1/movie_db'
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:' + SECRET_KEY + '@127.0.0.1/movie_db'
    DEBUG = True
    CSRF_ENABLED = True