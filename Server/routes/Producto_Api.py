
import json
from BusinessLayer.Producto_Business import *
from app import app
from flask import Blueprint, request, jsonify
from requests import get
from function_jwt import validate_token
import requests


# @app.before_request
# def verify_token_middleware():
#     token = request.headers['Authorization'].split(" ")[1]
#     return validate_token(token,output=False)

@app.route('/producto')
def producto_Items():
    jsonData = Producto_Business.Get_ProductoItems()
    respone = jsonify(jsonData)
    respone.status_code = 200
    return respone
    # return jsonify(jsonData)


@app.route('/producto/<Id>')
def producto_Item(Id):
    jsonData = Producto_Business.Get_ProductoItem(Id)
    respone = jsonify(jsonData)
    respone.status_code = 200
    return respone


class EmpresaModel:
    def __init__(self, EmpresaId, Nombre, Ruc):
        self.EmpresaId = EmpresaId
        self.Nombre = Nombre
        self.Ruc = Ruc


@app.route('/create', methods=['POST'])
def create_emp():
    try:
        _json = request.json
        _Nombre = _json['Nombre']
        _TipoProductoId = _json['TipoProductoId']
        _Usuario = _json['Usuario']
        _Estado = _json['Estado']
        if _Nombre and _TipoProductoId and _Usuario and _Estado and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO cat_producto(Nombre, TipoProductoId, Usuario, Estado) VALUES(%s, %s, %s, %s)"
            bindData = (_Nombre, _TipoProductoId, _Usuario, _Estado)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Employee added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/SaveProducto', methods=['POST'])
def Save():
    _json = request.json
    _Nombre = _json['Nombre']
    _TipoProductoId = _json['TipoProductoId']
    _Usuario = _json['Usuario']
    _Estado = _json['Estado']

    Producto = ProductoEntity()
    Producto._Nombre = _Nombre
    Producto._TipoProductoId = _TipoProductoId
    Producto._Usuario = _Usuario
    Producto._Estado = _Estado

    jsonData = Producto_Business.SaveProducto(Producto)
    respone = jsonify('Producto registrado!')
    respone.status_code = 200
    return respone


@app.route('/SaveProductoAlter', methods=['POST'])
def SaveAlter(Producto: ProductoEntity):

    jsonData = Producto_Business.SaveProducto(Producto)
    # if(jsonData):
    respone = jsonify('Producto registrado!')
    respone.status_code = 200
    # else:
    #     respone = jsonify('Producto Error!')
    #     respone.status_code = 204
    return respone


@app.route('/DeleteProducto/<ProductoId>', methods=['DELETE'])
def DeleteProducto(ProductoId):
    jsonData = Producto_Business.DeleteProducto(ProductoId)
    respone = jsonify('Producto Eliminado!')
    respone.status_code = 200
    return respone
