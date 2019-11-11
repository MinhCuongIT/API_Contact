from app.models import person_model as model
def getAllPersons():
    result = model.getAllPersons()
    return result
def addPerson(json):
    if not 'name' in json or not 'phone' in json:
        return (600, 'json invalid')
    else:
        result = model.addPersons(json)
        return (200,{'id':result[0]['id']})
def updatePerson(json):
    if not 'id' in json:
        return (600, 'json invalid')
    else:
        result = model.updatePersons(json)
        if result[0]['status'] == 200:
            return (200,{'id':result[0]['id']})
        else:
           return (600, result[0]['mess'])

def deletePerson(json):
    if not 'id' in json:
        return (600, 'json invalid')
    else:
        result = model.deletePersons(json)
        if result[0]['status'] == 200:
            return (200,{'id':result[0]['id']})
        else:
            return (600,result[0]['mess'])
