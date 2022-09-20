

class ProductoEntity:
    ProductoId: int
    Nombre: str
    TipoProductoId: int
    Usuario: str
    Estado: bool

    # data[]: any
    # def __init__(self, ProductoId: int,Nombre: str,TipoProductoId: int,Usuario: str,Estado: bool):
    #     self.ProductoId = ProductoId
    #     self.Nombre = Nombre
    #     self.TipoProductoId = TipoProductoId
    #     self.Usuario = Usuario
    #     self.Estado = Estado

    # def __init__(self):
    #     self.ProductoId = 0
    #     self.Nombre = ''
    #     self.TipoProductoId = 0

    def Cargar(_json: any):
        Data_ent = ProductoEntity()
        Data_ent.ProductoId = _json['ProductoId']
        Data_ent.Nombre = _json['Nombre']
        return Data_ent

# class DataEntity:
#     ProductoId: int

#     def __init__(self):
#         self.ProductoId: 0

    # def Cargar(_json: int):
    #     Data_ent = DataEntity()
    #     Data_ent.ProductoId = _json
    #     return Data_ent
