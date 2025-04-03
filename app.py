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


#Connect to server
cnx = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            port=app.config["MYSQL_PORT"],
            user=app.config["DATABASE_USER"],
            password=app.config["DATABASE_PWD"],
            database=app.config["DATABASE"]
        )

@app.route("/getprojects")
def getprojects():
    cur = cnx.cursor(dictionary=True)
    try:
        query=("SELECT * from heanlab.project ;")
        cur.execute(query)
        return jsonify(cur.fetchall())
    finally:
        cur.close()

    return []


@app.route('/getabout')
def getabout():
    cur = cnx.cursor(dictionary = True)
    try :
        query =  f"SELECT * FROM {app.config['DATABASE']}.about;"
        cur.execute(query)
        return jsonify(cur.fetchone())
    finally:
        cur.close()

    pass