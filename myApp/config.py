import os

# class Config(object):
#     SECRET_KEY = os.environ.get("SECRET_KEY")
#     SQLALCHEMY_DATABASE_URI = 'mysql://root:Info51987@127.0.0.1/movie_db'
#     DEBUG = True
#     CSRF_ENABLED = True

class Config(object):
    # SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Info51987@127.0.0.1/mydatabase'
    DEBUG = True
    CSRF_ENABLED = True

# class Config(object):
#     SECRET_KEY = os.environ.get("SECRET_KEY")
#     SQLALCHEMY_DATABASE_URI = 'mysql://root:' + str(SECRET_KEY) + '@127.0.0.1/movie_db'
#     DEBUG = True
#     CSRF_ENABLED = True