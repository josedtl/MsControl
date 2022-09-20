import json
from DataLayer.PersonaNatural_Data import *


class PersonaNatural_Business:
    def Get_PersonaNaturalItems():
        try:
            data = PersonaNatural_Data.Get_PersonaNaturalItems()
            jsonData = []

            for row in data:
                jsonStr = json.dumps(row.__dict__)
                jsonStr = json.loads(jsonStr)
                jsonData.append(jsonStr)

            return jsonData
        except Exception as e:
            print(e)