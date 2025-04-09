import mysql.connector
from config import Config
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

load = load_dotenv()


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

#MysQL configuration
mysql_config = {
    'host': os.getenv('MYSQL_HOST'),
    'port': app.config["MYSQL_PORT"],
    'user': app.config["DATABASE_USER"],
    'password': app.config["DATABASE_PWD"],
    'database': app.config["DATABASE"],
    'raise_on_warnings': True
}

#Connect to server
cnx = mysql.connector.connect(**mysql_config)

@app.route("/getprojects")
def getprojects():
    if  cnx.is_connected():
        cur = cnx.cursor(dictionary=True, buffered=True)
    else:
        cnx.reconnect()
        cur = cnx.cursor(dictionary=True, buffered=True)
    try:
        query=("SELECT * from heanlab.project ;")
        cur.execute(query)
        return jsonify(cur.fetchall())
    finally:
        cur.close()



@app.route('/getabout')
def getabout():
    if cnx.is_connected():
        cur = cnx.cursor(dictionary = True, buffered = True)
    else:
        cnx.reconnect()
        cur = cnx.cursor(dictionary = True, buffered = True)
    try :
        query =  f"SELECT * FROM {app.config['DATABASE']}.about;"
        cur.execute(query)
        return jsonify(cur.fetchone())
    finally:
        cur.close()