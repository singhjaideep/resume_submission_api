from flask import Flask
from flask import request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    if request.args.get("q")=='Puzzle':
        return solvePuzzle(request.args.get("d"))
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
    #1 Construct basic string
    puzzle_input = puzzle_input[32:]
    puzzle_input = puzzle_input.replace('A','').replace('B','').replace('C','').replace('D','').replace('\n','')
    #2 Assign weights
    w = {0:0,1:0,2:0,3:0}
    for i in range(0,len(puzzle_input),4):
        for j in range(0,4):
            #if > then increase weight otherwise if < then decrease
            if puzzle_input[i+j] in ('<','>'):
                if puzzle_input[i+j] == '>':
                    w[i/4]+=w[j]
                    w[i/4]+=1
                else:
                    w[i/4]-=w[j]
                    w[i/4]-=1
    #3 Construct correct output
    puzzle_output = ['']*16
    for i in range(0,len(puzzle_input),4):
        for j in range(0,4):
            #output '=' if diagonal
            if i/4==j:
                puzzle_output[i+j] = '='
            #output same character if not -
            elif puzzle_input[i+j] != '-':
                puzzle_output[i+j] = puzzle_input[i+j]
            #output > or < based on weights
            else:
                if w[i/4] > w[j]:
                    puzzle_output[i+j] = '>'
                else:
                    puzzle_output[i+j] = '<'
    #merge list to string
    puzzle_output = ''.join(puzzle_output)
    #add correct format to string
    puzzle_output = ' ABCD\nA'+puzzle_output[0:4]+'\nB'+puzzle_output[4:8]+'\nC'+puzzle_output[8:12]+'\nD'+puzzle_output[12:16]
    return puzzle_output


