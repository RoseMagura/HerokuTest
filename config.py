import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True 

SQLALCHEMY_DATABASE_URI = 'postgres://postgres:1@localhost:5432/newherokutest'
# SQLALCHEMY_DATABASE_URI = 'postgres://rbzkztrfwjyghb:96e6932b69f21b236db0420120ac32818cd3d99d9b00f8d1fc6e4a20d8c7bb71@ec2-52-22-216-69.compute-1.amazonaws.com:5432/d75ujhmqfldjfu'
SQLALCHEMY_TRACK_MODIFICATIONS = False