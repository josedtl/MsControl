
import json
from BusinessLayer.PersonaNatural_Business import *
from app import app
from flask import Blueprint, request, jsonify
from requests import get
from function_jwt import validate_token
import requests


# @app.before_request
# def verify_token_middleware():
#     token = request.headers['Authorization'].split(" ")[1]
#     return validate_token(token,output=False)

@app.route('/Get_PersonaNaturalItems')
def Get_PersonaNaturalItems():
    try:
        jsonData = PersonaNatural_Business.Get_PersonaNaturalItems()
        respone = jsonify(jsonData)
        respone.status_code = 200
        return respone
    except:
        print("An exception occurred")
