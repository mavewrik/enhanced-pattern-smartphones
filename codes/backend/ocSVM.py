# Python method to implement One-Class SVM after training on a set of triples
# Description: create triples of (speed, xy, pressure), train the SVM model and test for a new triple

# Import dependencies
import numpy as np
from sklearn.svm import OneClassSVM as OCSVM

def trainSVM(deviceId: str, speed1: float, xy1: float, pressure1: float):
    # create triples
    filenames = [deviceId+'/validSpeed.txt', deviceId+'/validXY.txt', deviceId+'/validPressure.txt']
    speed = []
    XY = []
    pressure = []
    
    file = open(filenames[0],'r')
    if file.mode == 'r':
        f1 = file.readlines()
        for f in f1:
            speed.append([float(f)])
    file = open(filenames[1],'r')
    if file.mode == 'r':
        f1 = file.readlines()
        for f in f1:
            XY.append([float(f)])
    file = open(filenames[2],'r')
    if file.mode == 'r':
        f1 = file.readlines()
        for f in f1:
            pressure.append([float(f)])
    
    length = len(speed)
    
    # train SVM and test for a new triple
    clf = OCSVM(kernel="rbf", nu = 0.1, gamma=0.1)
    print("Model Trained")
    clf.fit(speed)
    speedResult = False
    if clf.predict([[speed1]])[0] == 1:
        speedResult = True
    clf.fit(XY)
    xyResult = False
    if clf.predict([[xy1]])[0] == 1:
        xyResult = True
    clf.fit(pressure)
    pressureResult = False
    if clf.predict([[pressure1]])[0] == 1:
        pressureResult = True
    
    if (speedResult and xyResult):
        fileOpen = open(deviceId+"/validSpeed.txt","a+")
        fileOpen.write(str(speed1))
        fileOpen.write("\n")
        fileOpen.close()
        fileOpen = open(deviceId+"/validXY.txt","a+")
        fileOpen.write(str(xy1))
        fileOpen.write("\n")
        fileOpen.close()
        return "1"
    elif (speedResult and pressureResult):
        return "2"
    elif (xyResult and pressureResult):
        return "3"
    else:
        return "0"

#print(trainSVM("1332443d1016771a",0.024743295917981755,0.911296714102347,0.0029524541124482406))