# coding=utf-8
# from flask_sqlalchemy import SQLAlchemy
import json
import sqlite3
import time
from datetime import timedelta

from flask import Flask, jsonify, render_template, request

# TODO 将服务器时间进入数据库


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + './newtest.db'
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = True


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
    tt = time.localtime()
    lctime = str(tt.tm_year)+'/'+str(tt.tm_mon)+'/' + \
        str(tt.tm_mday)+'/'+str(tt.tm_hour) + \
        '/'+str(tt.tm_min)+'/'+str(tt.tm_sec)
    # 写入数据库
    connection = sqlite3.connect('./newtest.db')
    cur = connection.cursor()
    sql = 'SELECT * FROM coochatable '+'where id='+str(idd)
    cur.execute(sql)
    see = cur.fetchall()
    iddd = []
    tempreture_1 = []
    longitude_1 = []
    latitude_1 = []
    jsondata = {}
    for data in see:
        iddd.append(data[0])
        tempreture_1.append(data[1])
        longitude_1.append(data[2])
        latitude_1.append(data[3])

    if longitude_1.count(float(lon)) == 0 or latitude_1.count(float(lat)) == 0:
        print(lctime)
        new_sql = "INSERT INTO coochatable" + \
            "(id,tempreture, " + \
            "longitude, latitude,lock,time)VALUES(" + \
            str(int(idd))+","+str(temp) + \
            ","+str(lon)+","+str(lat)+","+str(lock)+","+"'"+str(lctime)+"'"+")"
        cur.execute(new_sql)
        connection.commit()

    cur.close()
    connection.close()

    connection = sqlite3.connect('./newtest.db')
    cur = connection.cursor()
    sql = 'SELECT * FROM statelock'
    cur.execute(sql)
    see = cur.fetchall()
    lock = ('id not found!')
    for lockornot in see:
        if lockornot[0] == int(idd):
            lock = str(lockornot[1])
    print("=========成功 生成 index.html==============")
    jsondata['lock'] = '1'
    dataout = json.dumps(jsondata)
    return (dataout)


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
    idd = request.form.get('id')
    connection = sqlite3.connect('./newtest.db')
    cur = connection.cursor()
    sql = 'SELECT * FROM coochatable where id='+str(idd)
    cur.execute(sql)
    see = cur.fetchall()
    tempreture_1 = []
    jsonData = {}
    for data in see:
        tempreture_1.append(data[1])
    jsonData['tempreture_1'] = tempreture_1
    dataout = json.dumps(jsonData)
    cur.close()
    connection.close()
    return (dataout)


@app.route('/test', methods=['POST'])
def test():
    idd = request.form.get('id')
    connection = sqlite3.connect('./newtest.db')
    cur = connection.cursor()
    sql = 'SELECT * FROM coochatable where id='+str(idd)
    cur.execute(sql)
    see = cur.fetchall()
    id = []
    longitude_1 = []
    latitude_1 = []
    longitude_2 = []
    latitude_2 = []
    jsonData = {}
    for index, data in enumerate(see):
        if index != len(see)-1:
            longitude_1.append(data[2])
            latitude_1.append(data[3])
            longitude_2.append(see[index+1][2])
            latitude_2.append(see[index+1][3])
        if index == len(see)-1:
            pass

    jsonData['longitude_1'] = longitude_1
    jsonData['latitude_1'] = latitude_1
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
    app.run(host='0.0.0.0', port=8089, debug=True)
