import json
from DataLayer.Producto_Data import *


class Producto_Business:
    def Get_ProductoItems():
        try:
            data = Producto_Data.Get_ProductoItems()
            jsonData = []

            for row in data:
                jsonStr = json.dumps(row.__dict__)
                jsonStr = json.loads(jsonStr)
                jsonData.append(jsonStr)

            return jsonData
        except Exception as e:
            print(e)

    def Get_ProductoItem(Id):
        try:
            data = Producto_Data.Get_ProductoItem(Id)
            jsonData = []

            for row in data:
                jsonStr = json.dumps(row.__dict__)
                jsonStr = json.loads(jsonStr)
                jsonData.append(jsonStr)

            return jsonData
        except Exception as e:
            print(e)

    def SaveProducto(Producto: ProductoEntity):
        try:
            data = Producto_Data.SaveProducto(Producto)
            return data
        except Exception as e:
            print(e)

    def DeleteProducto(ProductoId: int):
        try:
            data = Producto_Data.DeleteProducto(ProductoId)
            return data
        except Exception as e:
            print(e)
