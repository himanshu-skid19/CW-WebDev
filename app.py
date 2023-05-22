from flask import Flask, render_template, request
from flask_session import Session
import requests
import json

app = Flask(__name__)
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=['GET'])
def index():
    req = requests.get("https://www.coursehubiitg.in/api/codingweek/contributions")
    data = req.content
    json_data = json.loads(data)
    l = {}
    j=1
    for i in json_data:
        l[i['points']] = j
        j+=1
    top3 = []
    rest = []
    sorted_points = sorted(l.keys(), reverse=True)
    k=1
    for i in sorted_points:
        if k < 4:
            top3.append(l[i])
            k+=1
        else:
            rest.append(l[i])
            k+=1
            
    return "hello"