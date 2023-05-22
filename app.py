from flask import Flask, render_template, request
from flask_session import Session
import requests

app = Flask(__name__)
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=['GET'])
def index():
    req = requests.get("https://www.coursehubiitg.in/api/codingweek/contributions")
    print(req.content)
    return 'hello'