import json
import os
import shutil

from flask import Flask, request

import trainSpeed, trainXY, trainPressure, testApp

app = Flask(__name__)


@app.route("/upload", methods=['POST'])
def getData():
    data = request.get_data()
    data1 = json.loads(data)
    mode = data1['mode']
    deviceId = data1['deviceId']
    xy = data1['xy']
    speed = data1['speed']
    pressure = data1['pressure']
    if not os.path.isdir(deviceId):
        os.mkdir(deviceId)
    if mode == 'train':
        if not os.path.isdir(deviceId + '/train'):
            os.mkdir(deviceId + '/train')
        count = len([name for name in os.listdir(deviceId + '/train') if os.path.isfile(deviceId + '/train/' + name)])
        count = int(count / 3)
        count = count + 1
        fileOpen = open(deviceId + '/train/' + "xy" + str(count) + ".csv", "w+")
        fileOpen.write(xy)
        fileOpen.close()
        fileOpen = open(deviceId + '/train/' + "speed" + str(count) + ".csv", "w+")
        fileOpen.write(speed)
        fileOpen.close()
        fileOpen = open(deviceId + '/train/' + "pressure" + str(count) + ".csv", "w+")
        fileOpen.write(pressure)
        fileOpen.close()
    if mode == 'test':
        if not os.path.isdir(deviceId + '/test'):
            os.mkdir(deviceId + '/test')
        count = len([name for name in os.listdir(deviceId + '/test') if os.path.isfile(deviceId + '/test/' + name)])
        count = int(count / 3)
        count = count + 1
        fileOpen = open(deviceId + '/test/' + "xy" + str(count) + ".csv", "w+")
        fileOpen.write(xy)
        fileOpen.close()
        fileOpen = open(deviceId + '/test/' + "speed" + str(count) + ".csv", "w+")
        fileOpen.write(speed)
        fileOpen.close()
        fileOpen = open(deviceId + '/test/' + "pressure" + str(count) + ".csv", "w+")
        fileOpen.write(pressure)
        fileOpen.close()
    return "1"


@app.route("/testing", methods=['POST'])
def testing():
    data = request.get_data()
    data1 = json.loads(data)
    print(data1['mode'])
    return data


@app.route("/count", methods=['POST'])
def count():
    data = request.get_data()
    data1 = json.loads(data)
    deviceId = data1['deviceId']
    return str(len([name for name in os.listdir(deviceId + '/train') if os.path.isfile(deviceId + '/train/' + name)]))


@app.route("/train", methods=['POST'])
def training():
    data = request.get_data()
    data1 = json.loads(data)
    deviceId = data1['deviceId']
    print(deviceId)
    trainSpeed.train(deviceId)
    trainXY.train(deviceId)
    trainPressure.train(deviceId)
    return "Successful"


@app.route("/test", methods=['POST'])
def test():
    data = request.get_data()
    data1 = json.loads(data)
    mode = data1['mode']
    deviceId = data1['deviceId']
    xy = data1['xy']
    speed = data1['speed']
    pressure = data1['pressure']
    if not os.path.isdir(deviceId):
        os.mkdir(deviceId)
    if not os.path.isdir(deviceId + '/test'):
        os.mkdir(deviceId + '/test')
    count = len([name for name in os.listdir(deviceId + '/test') if os.path.isfile(deviceId + '/test/' + name)])
    count = int(count / 3)
    count = count + 1
    fileOpen = open(deviceId + '/test/' + "xy" + str(count) + ".csv", "w+")
    fileOpen.write(xy)
    fileOpen.close()
    fileOpen = open(deviceId + '/test/' + "speed" + str(count) + ".csv", "w+")
    fileOpen.write(speed)
    fileOpen.close()
    fileOpen = open(deviceId + '/test/' + "pressure" + str(count) + ".csv", "w+")
    fileOpen.write(pressure)
    fileOpen.close()
    result = testApp.test1(deviceId, count, count + 1)
    print(result)
    return result

@app.route("/reset",methods=['POST'])
def reset():
    data = request.get_data()
    data1 = json.loads(data)
    deviceId = data1['deviceId']
    if os.path.isdir(deviceId):
        shutil.rmtree(deviceId)
        return "Reset_Successful"
    else:
        return "No_Previous_Records"



if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded='true')
