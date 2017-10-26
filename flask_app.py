from flask import Flask
import logging
from flask import request

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    out = 'OK'
    logging.info(request.args)#.get("q")) #also d
    if request.args.get("q")=='Puzzle':
        out = " ABCD\nA=>>>\nB<=<<\nC<>=>\nD<><="
    elif request.args.get("q")=='Name':
        out = 'Jaideep Singh'
    elif request.args.get("q")=='Email Address':
        out = 'jd@jaideepsingh.in'
    elif request.args.get("q")=='Phone':
        out = '765-337-7543'
    elif request.args.get("q")=='Position':
        out = 'Engineer'
    elif request.args.get("q")=='Years':
        out = '5'
    elif request.args.get("q")=='Referrer':
        out = 'Online'
    elif request.args.get("q")=='Degree':
        out = 'BS in CS from Purdue University'
    elif request.args.get("q")=='Resume':
        out = 'https://drive.google.com/file/d/0ByVqCuHG6OISZlJIVFU2UVNleEE/view?usp=sharing'
    elif request.args.get("q")=='Status':
        out = 'Yes'
    elif request.args.get("q")=='Source':
        out = 'https://github.com/singhjaideep/resume_submission_api'
    return out

