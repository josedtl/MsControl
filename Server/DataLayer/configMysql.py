from flask import Flask
from flask_cors import CORS, cross_origin   
from flaskext.mysql import MySQL

app = Flask(__name__)

CORS(app)  
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'abcde1F'
app.config['MYSQL_DATABASE_DB'] = 'ad_controlacceso'
app.config['MYSQL_DATABASE_HOST'] = '190.187.52.107'
mysql.init_app(app)