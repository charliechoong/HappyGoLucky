import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/clean_floor', methods=['POST'])
def evaluateFloor():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    answer = {}
    for item in data.get("tests"):
        list1 = data.get("tests").get(item).get("floor")
        answer[item] = solve(list1,list1)
        # return json.dumps(data.get("tests").get(item).get("floor"))
    return json.dumps({"answers" : answer})

def solve(current_state, initial_state, pos=0, num_actions=0, min_steps=float('inf')):
    if sum(current_state) == 0 or (initial_state == current_state and pos==0 and num_actions>0):
        if num_actions < min_steps:
            min_steps = num_actions
        return min_steps
    # move left.
    tmp_state = current_state[:]
    if pos > 0:
        if tmp_state[pos-1] == 0:
            tmp_state[pos-1] += 1
        else:
            tmp_state[pos-1] -= 1
        min_steps = solve(tmp_state, initial_state, pos-1, num_actions+1, min_steps) 
    # move right.
    tmp_state = current_state[:]
    if pos < len(current_state) - 1:
        if tmp_state[pos+1] == 0:
            tmp_state[pos+1] += 1
        else:
            tmp_state[pos+1] -= 1
        min_steps = solve(tmp_state, initial_state, pos+1, num_actions+1, min_steps) 
    return min_steps




