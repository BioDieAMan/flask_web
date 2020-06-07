# coding=utf-8
# from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify
import sqlite3
import json
from datetime import timedelta

import time


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + './newtest.db'
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = True


@app.route('/get-lock', methods=['GET'])
def get_lock():
    get = request.args.get('lock')
    idd = request.args.get('number')
    connection = sqlite3.connect('./newtest.db')
    cur = connection.cursor()
    sql = 'SELECT * FROM statelock where id='+str(idd)
    cur.execute(sql)
    see = cur.fetchall()
    done = 'no need to change the state'
    if see[0][1] != int(get):
        print(get)
        print(idd)
        new_sql = "update statelock set lock=" + \
            str(get)+" where id="+str(idd)
        cur.execute(new_sql)
        connection.commit()
        done = 'changed'
    cur.close()
    connection.close()
    return done


@app.route('/get-wechat', methods=['GET'])
def get_wechat():
    # args = request.args.get("name")
    form = request.args.get('number')

    connection = sqlite3.connect('./newtest.db')
    cur = connection.cursor()
    sql = 'SELECT * FROM coochatable where id='+str(form)
    cur.execute(sql)
    see = cur.fetchall()

    id = []
    name = []
    tempreture = []
    longitude = []
    latitude = []
    lock = []
    timme = []
    jsonData = {}
    for index, data in enumerate(see):
        tempreture.append(data[1])
        longitude.append(data[2])
        latitude.append(data[3])
        lock.append(data[4])
        timme.append(data[5])

    jsonData['tempreture'] = tempreture
    jsonData['longitude'] = longitude
    jsonData['latitude'] = latitude
    jsonData['lock'] = lock
    jsonData['time'] = timme
    dataout = json.dumps(jsonData)
    cur.close()
    connection.close()

    return jsonify(data=(dataout))


@app.route('/search', methods=['GET'])
def search():
    idd = request.args.get('id')

    connection = sqlite3.connect('./newtest.db')
    cur = connection.cursor()
    sql = 'SELECT * FROM coochatable where id='+str(idd)
    cur.execute(sql)
    see = cur.fetchall()

    tempreture = []
    longitude = []
    latitude = []
    lock = []
    time = []
    jsonData = {}

    for data in see:
        tempreture.append(data[1])
        longitude.append(data[2])
        latitude.append(data[3])
        lock.append(data[4])
        time.append(data[5])
    jsonData['tempreture'] = tempreture
    jsonData['longitude'] = longitude
    jsonData['latitude'] = latitude
    jsonData['lock'] = lock
    jsonData['time'] = time
    dataout = json.dumps(jsonData)
    return (dataout)


@app.route('/temp', methods=['POST'])
def temp():
    connection = sqlite3.connect('./newtest.db')
    cur = connection.cursor()
    sql = 'SELECT * FROM coochatable where id=16'
    cur.execute(sql)
    see = cur.fetchall()
    tempreture_1 = []
    jsonData = {}
    for data in see:
        tempreture_1.append(data[2])
    jsonData['tempreture_1'] = tempreture_1
    dataout = json.dumps(jsonData)
    cur.close()
    connection.close()
    return (dataout)


@app.route('/test', methods=['POST'])
def test():
    connection = sqlite3.connect('./newtest.db')
    cur = connection.cursor()
    sql = 'SELECT * FROM coochatable where id='+'16'
    cur.execute(sql)
    see = cur.fetchall()
    id = []
    tempreture_1 = []
    longitude_1 = []
    latitude_1 = []
    tempreture_2 = []
    longitude_2 = []
    latitude_2 = []
    jsonData = {}
    for index, data in enumerate(see):
        if index != len(see)-1:
            tempreture_1.append(data[1])
            longitude_1.append(data[2])
            latitude_1.append(data[3])
            tempreture_2.append(see[index+1][1])
            longitude_2.append(see[index+1][2])
            latitude_2.append(see[index+1][3])
        if index == len(see)-1:
            pass

    jsonData['tempreture_1'] = tempreture_1
    jsonData['longitude_1'] = longitude_1
    jsonData['latitude_1'] = latitude_1
    jsonData['tempreture_2'] = tempreture_2
    jsonData['longitude_2'] = longitude_2
    jsonData['latitude_2'] = latitude_2
    dataout = json.dumps(jsonData)
    cur.close()
    connection.close()
    return (dataout)


@app.route('/')
def index():
    return render_template('index_baidu.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090, ssl_context=(
        './3905801_www.coocha.top.pem', './3905801_www.coocha.top.key'))
