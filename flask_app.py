from flask import Flask
from flask import request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    if request.args.get("q")=='Puzzle':
        return solvePuzzle(request.get("d"))
    elif request.args.get("q")=='Name':
        return 'Jaideep Singh'
    elif request.args.get("q")=='Email Address':
        return 'jd@jaideepsingh.in'
    elif request.args.get("q")=='Phone':
        return '765-337-7543'
    elif request.args.get("q")=='Position':
        return 'Engineer'
    elif request.args.get("q")=='Years':
        return '5'
    elif request.args.get("q")=='Referrer':
        return 'Online'
    elif request.args.get("q")=='Degree':
        return 'BS in CS from Purdue University'
    elif request.args.get("q")=='Resume':
        return 'https://drive.google.com/file/d/0ByVqCuHG6OISZlJIVFU2UVNleEE/view?usp=sharing'
    elif request.args.get("q")=='Status':
        return 'Yes'
    elif request.args.get("q")=='Source':
        return 'https://github.com/singhjaideep/resume_submission_api'
    else:
        return 'OK'

def solvePuzzle(puzzle_input):
    puzzle_output = ''
    logging.info(puzzle_input)
    #Format: " ABCD\nA=>>>\nB<=<<\nC<>=>\nD<><="
    return puzzle_output
