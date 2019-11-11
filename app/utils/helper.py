from flask import json
def json_return(code, success, data, error):
    jsonData = {
        "code":code,
        "success": True if success else False,
        "data":data,
        "errors": __getErrorMessage(error)
    }
    result = json.dumps(jsonData)
    return result

def __getErrorMessage(error):
    if error:
        if type(error) is list:
            return [{"error":e} for e in error]
        else:
            return [{"error":error}]
    return None

def getVal(key, json):
    if key in json:
        if json[key]:
            return json[key]
        return 'NULL'
    return 'NULL'