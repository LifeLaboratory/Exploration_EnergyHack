import json


def to_json(data):
    result = None
    try:
        result = json.loads(data)
    except:
        data = data.replace("\'", "\"")
        data = data.replace("None", '"None"')
        result = json.loads(data)
    return result
