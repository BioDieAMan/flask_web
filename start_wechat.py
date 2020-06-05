# coding=utf-8
# from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify
import sqlite3
import json
import sqlite3
from datetime import timedelta

import time

from flask import Flask, jsonify, render_template, request


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + './newtest.db'
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = True


@app.route('/get-wechat', methods=['GET'])
def get_wechat():
    print('请求方式为------->', request.method)
    # args = request.args.get("name")
    form = request.args.get('number')
    print(form)
    print(type(form))

    connection = sqlite3.connect('./newtest.db')
    cur = connection.cursor()
    sql = 'SELECT * FROM coocha where id='+str(form)
    cur.execute(sql)
    see = cur.fetchall()

    id = []
    name = []
    tempreture = []
    longitude = []
    latitude = []
    jsonData = {}
    for index, data in enumerate(see):
        tempreture.append(data[2])
        longitude.append(data[3])
        latitude.append(data[4])
    jsonData['tempreture'] = tempreture
    jsonData['longitude'] = longitude
    jsonData['latitude'] = latitude
    jsonData['lock'] = ['0']
    dataout = json.dumps(jsonData)
    cur.close()
    connection.close()

    print("=========成功 生成 index.html==============")
    return jsonify(data=(dataout))


@app.route('/search', methods=['GET'])
def search():
    idd = request.args.get('id')
    print(idd)

    connection = sqlite3.connect('./newtest.db')
    cur = connection.cursor()
    sql = 'SELECT * FROM coocha where id='+str(idd)
    cur.execute(sql)
    see = cur.fetchall()
    print(see)

    tempreture = []
    longitude = []
    latitude = []
    lock = []
    time = []
    jsonData = {}

    for data in see:
        tempreture.append(data[2])
        longitude.append(data[3])
        latitude.append(data[4])
        lock.append(data[5])
        time.append(data[6])
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
    sql = 'SELECT * FROM coocha'
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
    sql = 'SELECT * FROM coocha'
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
            tempreture_1.append(data[2])
            longitude_1.append(data[3])
            latitude_1.append(data[4])
            tempreture_2.append(see[index+1][2])
            longitude_2.append(see[index+1][3])
            latitude_2.append(see[index+1][4])
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
