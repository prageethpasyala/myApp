# import os
# import mysql.connector

# class Config(object):
#     mydb1 = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Info51987",
#         database="mydatabase"
#         )



import os

class Config(object):
    SECRET_KEY = "my-secret-pw"
    SQLALCHEMY_DATABASE_URI = 'mysql://root:' + 'Info51987' + '@127.0.0.1/book_db'
    DEBUG = True
    CSRF_ENABLED = True