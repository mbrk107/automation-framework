import json


def parse_json(jfile):
    with open(jfile) as json_file:  
        jdata = json.load(json_file)
    return jdata

