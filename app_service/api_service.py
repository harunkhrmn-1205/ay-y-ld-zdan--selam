from flask import Flask, request,jsonify
from flask_cors import CORS
import psycopg2, os


app = Flask(__name__)
CORS(app)


DATABASE_URL = so.getenv(
"DATABASE_URL",
  "
