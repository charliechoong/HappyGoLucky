import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/revisitgeometry', methods=['POST'])
def evaluate():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    
    shapeCoordinates = data.get("shapeCoordinates")
    lineCoordinates = data.get("lineCoordinates")

    scoord_list = []
    for sCoord in shapeCoordinates:
        scoord_list.append([coord for coord in sCoord.values()])

    lcoord_list = []
    for lCoord in lineCoordinates:
        lcoord_list.append([coord for coord in lCoord.values()])


    extra_coord10 = lcoord_list[0][0] - 100*(lcoord_list[0][0]-lcoord_list[1][0])
    extra_coord11 = lcoord_list[0][1] - 100*(lcoord_list[0][1]-lcoord_list[1][1])
    lcoord_list.append([extra_coord10, extra_coord11])

    extra_coord20 = lcoord_list[0][0] + 100*(lcoord_list[0][0]-lcoord_list[1][0])
    extra_coord21 = lcoord_list[0][1] + 100*(lcoord_list[0][1]-lcoord_list[1][1])
    lcoord_list.append([extra_coord20, extra_coord21])

    l = LineString(lcoord_list)
    p = Polygon(scoord_list)

    linestring = l.intersection(p)
    #print(shape(linestring))
    points = list(shape(linestring).coords)
    
    ans = []
    for point in points:
        x = round(point[0],2)
        y = round(point[1],2)
        a_dict = { "x": x, "y": y }
        ans.append(a_dict)
    return json.dumps(ans)
      
