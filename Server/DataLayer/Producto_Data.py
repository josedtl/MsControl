from xmlrpc.client import Boolean
import pymysql
from sqlalchemy import true
from DataLayer.configMysql import mysql
from EntityLayer.ProductoEntity import *


class Producto_Data:
    def Get_ProductoItems():
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("sp_ProductoSelectAll")
            Rows = cursor.fetchall()

            listProductos = []

            for row in Rows:
                # Data_ent= ProductoEntity()
                # Data_ent.ProductoId=row['ProductoId']
                # Data_ent.Nombre = row['Nombre']
                # listProductos.append(Data_ent)

                Data_ent = ProductoEntity.Cargar(row)
                listProductos.append(Data_ent)

            return listProductos
        except Exception as e:
            print(e)

    def Get_ProductoItem(Id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("sp_ProductoItem", [Id])
            empRows = cursor.fetchall()

            ListaEmpresa = []

            for row in empRows:
                Data_ent = ProductoEntity()
                Data_ent._ProductoId = row['ProductoId']
                Data_ent._Nombre = row['Nombre']
                ListaEmpresa.append(Data_ent)

            return ListaEmpresa
        except Exception as e:
            print(e)

    def SaveProducto(Producto: ProductoEntity):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("sp_Producto_Insert", [
                            Producto._Nombre, Producto._TipoProductoId, Producto._Usuario, Producto._Estado])
            conn.commit()

            # sqlQuery = "INSERT INTO emp(name, email, phone, address) VALUES(%s, %s, %s, %s)"
            # bindData = (_name, _email, _phone, _address)
            # cursor.execute(sqlQuery, bindData)
            # conn.commit()

            return true
        except Exception as e:
            print(e)

    def DeleteProducto(ProductoId: int):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("sp_PersonalDelete", [ ProductoId])
            conn.commit()

            # sqlQuery = "INSERT INTO emp(name, email, phone, address) VALUES(%s, %s, %s, %s)"
            # bindData = (_name, _email, _phone, _address)
            # cursor.execute(sqlQuery, bindData)
            # conn.commit()

            return true
        except Exception as e:
            print(e)
