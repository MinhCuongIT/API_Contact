from app.utils import helper

def getAllPersons():
    import app.utils.db as db
    cursor =  db.getCursor().cursor()
    cursor.execute('[dbo].[sp_getAllPersons]')
    result = [{'id':item[0],'name':item[1],'phone':item[2],'address':item[3],'note':item[4],} for item in cursor]
    return result
def addPersons(json):
    import app.utils.db as db
    cnn = db.getCursor()
    with cnn.cursor(as_dict = True) as cur:
        query = "[dbo].[sp_addPerson] @Name=N'{0}',@Phone='{1}',@Address=N'{2}',@Note=N'{3}'".format(helper.getVal('name', json), helper.getVal('phone', json), helper.getVal('address', json), helper.getVal('note', json))
        cur.execute(query)
        result = [item for item in cur]
        cnn.commit()
        cnn.close()
        return result
def updatePersons(json):
    import app.utils.db as db
    cnn =  db.getCursor()
    with cnn.cursor(as_dict=True) as cursor:
        sqlString = "[dbo].[sp_updatePerson] @Id = {0}, @Name = N'{1}',@Phone = '{2}',@Address = N'{3}',@Note = N'{4}'".format(json['id'] ,json['name'] ,json['phone'] ,json['address'] ,json['note'])
        cursor.execute(sqlString)
        result = [item for item in cursor]
        cnn.commit()
        cnn.close()
        return result
def deletePersons(json):
    import app.utils.db as db
    cnn =  db.getCursor()
    with cnn.cursor(as_dict = True) as cur:
        sqlString = "[dbo].[sp_deletePerson] @Id = {0}".format(json['id'])
        cur.execute(sqlString)
        result = [item for item in cur]
        cnn.commit()
        cnn.close()
        return result