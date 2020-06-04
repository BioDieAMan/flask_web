# coding=utf-8
# from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify
import sqlite3
import json
import sqlite3
from datetime import timedelta

from flask import Flask, jsonify, render_template, request


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + './newtest.db'
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = True


@app.route('/search', methods=['GET'])
def search():
    idd = request.args.get('id')
    connection = sqlite3.connect('./newtest.db')
    cur = connection.cursor()
    sql = 'SELECT * FROM info'
    cur.execute(sql)
    see = cur.fetchall()

    name_1 = []
    tempreture_1 = []
    longitude_1 = []
    latitude_1 = []
    for data in see:
        name_1.append(data[1])
        tempreture_1.append(data[2])
        longitude_1.append(data[3])
        latitude_1.append(data[4])


@app.route('/get', methods=['GET'])
def get():
    # connection = sqlite3.connect('./newtest.db')
    # cur = connection.cursor()
    # sql = 'SELECT * FROM info'
    # cur.execute(sql)
    # see = cur.fetchall()
    # print('-------------------------')
    # print(see)
    # print('-------------------------')
    print('请求方式为--------------------->', request.method)
    idd = request.args.get("id")
    temp = request.args.get('temp')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    lock = request.args.get('lock')
    time = request.args.get('time')

    print(idd, temp, lat, lon, lock, time)
    # 写入数据库
    connection = sqlite3.connect('./newtest.db')
    cur = connection.cursor()
    sql = 'SELECT * FROM info'
    cur.execute(sql)
    see = cur.fetchall()
    print('-------------------------')
    print(see)
    print('-------------------------')
    id = []
    name_1 = []
    tempreture_1 = []
    longitude_1 = []
    latitude_1 = []
    jsondata = {}
    for data in see:
        name_1.append(data[1])
        tempreture_1.append(data[2])
        longitude_1.append(data[3])
        latitude_1.append(data[4])

    jsondata = json.dumps(jsondata)
    if longitude_1.find(lon) != -1 and latitude_1.find(lat) != -1:
        new_sql = "INSERT INTO info" + \
            "(id, name, tempreture, " + \
            "longitude, latitude,lock,time)VALUES(" + \
            str(idd)+","+"'newplace'"+","+str(temp) + \
            ","+str(lon)+","+str(lat)+","+str(lock)+","+str(time)+")"
        cur.execute(new_sql)

    cur.close()
    connection.close()

    print("=========成功 生成 index.html==============")
    return jsonify(lock=1)


@app.route('/temp', methods=['POST'])
def temp():
    connection = sqlite3.connect('./newtest.db')
    cur = connection.cursor()
    sql = 'SELECT * FROM coocha'
    cur.execute(sql)
    see = cur.fetchall()
    print('-------------------------')
    print(see)
    print('-------------------------')
    tempreture_1 = []
    jsonData = {}
    for data in see:
        tempreture_1.append(data[2])
    jsonData['tempreture_1'] = tempreture_1
    dataout = json.dumps(jsonData)
    cur.close()
    connection.close()
    return (dataout)


@app.route('/test', methods=['GET'])
def test():
    print('请求方式为--------------------->', request.method)
    idd = request.args.get("id")
    temp = request.args.get('temp')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    lock = request.args.get('lock')
    time = request.args.get('time')

    print(idd, temp, lat, lon, lock, time)
    connection = sqlite3.connect('./newtest.db')
    cur = connection.cursor()
    sql = 'SELECT * FROM coocha'
    cur.execute(sql)
    see = cur.fetchall()
    print('-------------------------')
    print(see)
    print('-------------------------')
    id = []
    name_1 = []
    tempreture_1 = []
    longitude_1 = []
    latitude_1 = []
    name_2 = []
    tempreture_2 = []
    longitude_2 = []
    latitude_2 = []
    jsonData = {}
    for index, data in enumerate(see):
        if index != len(see)-1:
            name_1.append(data[1])
            tempreture_1.append(data[2])
            longitude_1.append(data[3])
            latitude_1.append(data[4])
            name_2.append(see[index+1][1])
            tempreture_2.append(see[index+1][2])
            longitude_2.append(see[index+1][3])
            latitude_2.append(see[index+1][4])
        if index == len(see)-1:
            pass

    jsonData['name_1'] = name_1
    jsonData['tempreture_1'] = tempreture_1
    jsonData['longitude_1'] = longitude_1
    jsonData['latitude_1'] = latitude_1
    jsonData['name_2'] = name_2
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
    app.run(host='0.0.0.0', port=8090, debug=True)
