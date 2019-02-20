import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("postgres://dewhywnwipxige:edfaaefb6b15c6ea1608e1148e6f53deb735f3cb9c113a402244bf9df19220f8@ec2-54-83-44-4.compute-1.amazonaws.com:5432/da24557a866a9j"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("postgres://dewhywnwipxige:edfaaefb6b15c6ea1608e1148e6f53deb735f3cb9c113a402244bf9df19220f8@ec2-54-83-44-4.compute-1.amazonaws.com:5432/da24557a866a9j"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"
