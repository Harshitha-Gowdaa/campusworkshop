"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi82at269vf5qbdb14g-a.oregon-postgres.render.com",
        database="todo_pr5a",
        user="root",
        password="EjnIzzphPCqLOzw3eh4h1lPqLk5Sm0BN")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
