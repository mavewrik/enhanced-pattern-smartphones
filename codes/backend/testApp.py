import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import pandas as pd
import ocSVM


def test1(deviceId,range1,range2):
    out = []
    threshold = 0
    fileOpen = open(deviceId+"/speedThreshold.txt","r")
    if fileOpen.mode == "r":
        f1 = fileOpen.readlines()
        f1 = f1[1:]
        for out1 in f1:
            out.append(float(out1))
    fileOpen.close()


    finalValues = []
    for per in range(range1,range2):
        data1 = []
        data2 = []
        for j in range(1,11):
            data11 = pd.read_csv(deviceId+"/test/speed"+str(per)+".csv")
            data21 = pd.read_csv(deviceId+"/train/speed"+str(j)+".csv")
            data1.append(data11)
            data2.append(data21)



        x = []
        y = []
        for k in range(0,10):
            x1 = data1[k].iloc[:,0]
            x2 = [i for i in x1]
            x3 = data1[k].iloc[:,1]
            x4 = [i for i in x3]
            y1 = data2[k].iloc[:,0]
            y2 = [i for i in y1]
            y3 = data2[k].iloc[:,1]
            y4 = [i for i in y3]
            x5 = []
            y5 = []
            for j in range(0,len(x2)):
                #a = [x2[j],x4[j]]
                a = [x2[j]]
                x5.append(a)
            for j in range(0,len(y2)):
                #b = [y2[j],y4[j]]
                b = [y2[j]]
                y5.append(b)
            x11 = np.array(x5)
            y11 = np.array(y5)
            x.append(x11)
            y.append(y11)



        distance = []
        path = []
        for i in range(0,10):
            distance11,path11 = fastdtw(x[i], y[i], radius=2,  dist=euclidean)
            distance.append(distance11)
            path.append(path11)


        euc = []
        for j in range(0,10):
            e = []
            path11 = path[j]
            for i in path11:
                xSeries = x[j][i[0]]
                ySeries = y[j][i[1]]
                e.append(euclidean(xSeries, ySeries))
            euc.append(e)


        maxi = 0
        mini = 1000
        for i in euc:
            if len(i) > maxi:
                maxi = len(i)
            if len(i) < mini:
                mini = len(i)
        #print(maxi)
        #print(mini)



        for i in euc:
            if maxi-len(i) > 0:
                for j in range(0,maxi-len(i)):
                    i.append(0)




        euclid = np.array(euc)



        outCheck = euclid.std(0)
        #print(outCheck)
        #print(len(outCheck))
        outCheck = outCheck.tolist()

        '''out = [ 0.,7.6222888,1.28909351,0.50313601,0.40823923,0.52276039,0.68409885,
            0.47100917,0.5943060,0.50712524,0.63647946,0.88343757,1.26877159,0.88593596,
            0.58420113,0.55849572,1.11861177,0.58354765,0.45349692,3.91306162,1.02630051,
            1.69594541,1.60207398,0.66616407,0.60337481,1.33028231,1.13255606,0.99607701,
            0.97148844,0.50141571,4.50667912,11.25857005,19.13872895,27.67476316,35.37868321,41.67506706]'''
        #print(out)
        #print(len(out))


        if len(out) > len(outCheck):
            for i in range(0,len(out)-len(outCheck)):
                outCheck.append(0)
        else:
            for i in range(0,len(outCheck)-len(out)):
                out.append(0)

        result = []
        result.append(out)
        result.append(outCheck)
        result1 = np.array(result)
        result2 = result1.std(0)
        finalResult = np.std(result2)
        print(finalResult)
        #test1 = np.std(out)
        #test2 = np.std(outCheck)
        #print(test1-test2)
        finalValues.append(finalResult)
    fileOpen = open(deviceId+"/speedThreshold.txt","r")
    if fileOpen.mode == "r":
        f1 = fileOpen.readlines()
        threshold = float(f1[0])
    fileOpen.close()
    print(threshold)
    speed = False
    speed1 = False
    if finalResult <= threshold:
        speed = True
    if not speed:
        errorAllowed = threshold/10
        errorCalc = finalResult - threshold
        if errorCalc <= errorAllowed:
            speed1 = True
    
    speedResult = finalResult

    # XY 
    out = []
    fileOpen = open(deviceId+"/xyThreshold.txt","r")
    if fileOpen.mode == "r":
        f1 = fileOpen.readlines()
        f1 = f1[1:]
        for out1 in f1:
            out.append(float(out1))
    fileOpen.close()


    finalValues = []
    for per in range(range1,range2):
        data1 = []
        data2 = []
        for j in range(1,11):
            data11 = pd.read_csv(deviceId+"/test/xy"+str(per)+".csv")
            data21 = pd.read_csv(deviceId+"/train/xy"+str(j)+".csv")
            data1.append(data11)
            data2.append(data21)



        x = []
        y = []
        for k in range(0,10):
            x1 = data1[k].iloc[:,0]
            x2 = [i for i in x1]
            x3 = data1[k].iloc[:,1]
            x4 = [i for i in x3]
            x6 = data1[k].iloc[:,2]
            x7 = [i for i in x6]
            y1 = data2[k].iloc[:,0]
            y2 = [i for i in y1]
            y3 = data2[k].iloc[:,1]
            y4 = [i for i in y3]
            y6 = data2[k].iloc[:,2]
            y7 = [i for i in y6]
            x5 = []
            y5 = []
            for i in range(0,len(x2)):
                #a = [x2[i],x4[i],x7[i]]
                a = [x2[i],x4[i]]
                x5.append(a)
            for i in range(0,len(y2)):
                #b = [y2[i],y4[i],y7[i]]
                b = [y2[i],y4[i]]
                y5.append(b)
            x11 = np.array(x5)
            y11 = np.array(y5)
            x.append(x11)
            y.append(y11)



        distance = []
        path = []
        for i in range(0,10):
            distance11,path11 = fastdtw(x[i], y[i], radius=2,  dist=euclidean)
            distance.append(distance11)
            path.append(path11)


        euc = []
        for j in range(0,10):
            e = []
            path11 = path[j]
            for i in path11:
                xSeries = x[j][i[0]]
                ySeries = y[j][i[1]]
                e.append(euclidean(xSeries, ySeries))
            euc.append(e)


        maxi = 0
        mini = 1000
        for i in euc:
            if len(i) > maxi:
                maxi = len(i)
            if len(i) < mini:
                mini = len(i)
        #print(maxi)
        #print(mini)



        for i in euc:
            if maxi-len(i) > 0:
                for j in range(0,maxi-len(i)):
                    i.append(0)




        euclid = np.array(euc)



        outCheck = euclid.std(0)
        #print(outCheck)
        #print(len(outCheck))
        outCheck = outCheck.tolist()

        '''out = [ 0.,7.6222888,1.28909351,0.50313601,0.40823923,0.52276039,0.68409885,
            0.47100917,0.5943060,0.50712524,0.63647946,0.88343757,1.26877159,0.88593596,
            0.58420113,0.55849572,1.11861177,0.58354765,0.45349692,3.91306162,1.02630051,
            1.69594541,1.60207398,0.66616407,0.60337481,1.33028231,1.13255606,0.99607701,
            0.97148844,0.50141571,4.50667912,11.25857005,19.13872895,27.67476316,35.37868321,41.67506706]'''
        #print(out)
        #print(len(out))


        if len(out) > len(outCheck):
            for i in range(0,len(out)-len(outCheck)):
                outCheck.append(0)
        else:
            for i in range(0,len(outCheck)-len(out)):
                out.append(0)

        result = []
        result.append(out)
        result.append(outCheck)
        result1 = np.array(result)
        result2 = result1.std(0)
        finalResult = np.std(result2)
        print(finalResult)
        #test1 = np.std(out)
        #test2 = np.std(outCheck)
        #print(test1-test2)
        finalValues.append(finalResult)
    fileOpen = open(deviceId+"/xyThreshold.txt","r")
    if fileOpen.mode == "r":
        f1 = fileOpen.readlines()
        threshold = float(f1[0])
    fileOpen.close()
    print(threshold)
    xyC = False
    xy1 = False
    if finalResult <= threshold:
        xyC = True
    if not xyC:
        errorAllowed = threshold/10
        errorCalc = finalResult - threshold
        if errorCalc <= errorAllowed:
            xy1 = True

    xyResult = finalResult

    #Pressure
    
    out = []
    fileOpen = open(deviceId+"/pressureThreshold.txt","r")
    if fileOpen.mode == "r":
        f1 = fileOpen.readlines()
        f1 = f1[1:]
        for out1 in f1:
            out.append(float(out1))
    fileOpen.close()


    finalValues = []
    for per in range(range1,range2):
        data1 = []
        data2 = []
        for j in range(1,11):
            data11 = pd.read_csv(deviceId+"/test/pressure"+str(per)+".csv")
            data21 = pd.read_csv(deviceId+"/train/pressure"+str(j)+".csv")
            data1.append(data11)
            data2.append(data21)



        x = []
        y = []
        for k in range(0,10):
            x1 = data1[k].iloc[:,0]
            x2 = [i for i in x1]
            x3 = data1[k].iloc[:,1]
            x4 = [i for i in x3]
            y1 = data2[k].iloc[:,0]
            y2 = [i for i in y1]
            y3 = data2[k].iloc[:,1]
            y4 = [i for i in y3]
            x5 = []
            y5 = []
            for j in range(0,len(x2)):
                #a = [x2[j],x4[j]]
                a = [x2[j]]
                x5.append(a)
            for j in range(0,len(y2)):
                #b = [y2[j],y4[j]]
                b = [y2[j]]
                y5.append(b)
            x11 = np.array(x5)
            y11 = np.array(y5)
            x.append(x11)
            y.append(y11)



        distance = []
        path = []
        for i in range(0,10):
            distance11,path11 = fastdtw(x[i], y[i], radius=2,  dist=euclidean)
            distance.append(distance11)
            path.append(path11)


        euc = []
        for j in range(0,10):
            e = []
            path11 = path[j]
            for i in path11:
                xSeries = x[j][i[0]]
                ySeries = y[j][i[1]]
                e.append(euclidean(xSeries, ySeries))
            euc.append(e)


        maxi = 0
        mini = 1000
        for i in euc:
            if len(i) > maxi:
                maxi = len(i)
            if len(i) < mini:
                mini = len(i)
        #print(maxi)
        #print(mini)



        for i in euc:
            if maxi-len(i) > 0:
                for j in range(0,maxi-len(i)):
                    i.append(0)




        euclid = np.array(euc)



        outCheck = euclid.std(0)
        #print(outCheck)
        #print(len(outCheck))
        outCheck = outCheck.tolist()

        '''out = [ 0.,7.6222888,1.28909351,0.50313601,0.40823923,0.52276039,0.68409885,
            0.47100917,0.5943060,0.50712524,0.63647946,0.88343757,1.26877159,0.88593596,
            0.58420113,0.55849572,1.11861177,0.58354765,0.45349692,3.91306162,1.02630051,
            1.69594541,1.60207398,0.66616407,0.60337481,1.33028231,1.13255606,0.99607701,
            0.97148844,0.50141571,4.50667912,11.25857005,19.13872895,27.67476316,35.37868321,41.67506706]'''
        #print(out)
        #print(len(out))


        if len(out) > len(outCheck):
            for i in range(0,len(out)-len(outCheck)):
                outCheck.append(0)
        else:
            for i in range(0,len(outCheck)-len(out)):
                out.append(0)

        result = []
        result.append(out)
        result.append(outCheck)
        result1 = np.array(result)
        result2 = result1.std(0)
        finalResult = np.std(result2)
        print(finalResult)
        #test1 = np.std(out)
        #test2 = np.std(outCheck)
        #print(test1-test2)
        finalValues.append(finalResult)

    fileOpen = open(deviceId+"/pressureThreshold.txt","r")
    if fileOpen.mode == "r":
        f1 = fileOpen.readlines()
        threshold = float(f1[0])
    fileOpen.close()
    print(threshold)
    pressure = False
    if finalResult <= threshold:
        pressure = True
    
    pressureResult = finalResult

# SVM CALL
    fileOpen = open(deviceId+"/validSpeed.txt","r")
    num = 0
    if fileOpen.mode == "r":
        f1 = fileOpen.readlines()
        num = len(f1)
    fileOpen.close()
    if num >= 8:
        resultSVM = ocSVM.trainSVM(deviceId,speedResult,xyResult,pressureResult)
        print("SVM")
        if resultSVM == "1":
            return "1"
        elif resultSVM == "2":
            fileOpen = open(deviceId+"/xyThreshold.txt","r")
            if fileOpen.mode == "r":
                f1 = fileOpen.readlines()
                threshold = float(f1[0])
            fileOpen.close()
            if xyResult <= threshold:
                fileOpen = open(deviceId+"/validSpeed.txt","a+")
                fileOpen.write(str(speedResult))
                fileOpen.write("\n")
                fileOpen.close()
                fileOpen = open(deviceId+"/validXY.txt","a+")
                fileOpen.write(str(xyResult))
                fileOpen.write("\n")
                fileOpen.close()
                fileOpen = open(deviceId+"/validPressure.txt","a+")
                fileOpen.write(str(pressureResult))
                fileOpen.write("\n")
                fileOpen.close()
                return "1"
            else:
                return "0"
        elif resultSVM == "3":
            fileOpen = open(deviceId+"/speedThreshold.txt","r")
            if fileOpen.mode == "r":
                f1 = fileOpen.readlines()
                threshold = float(f1[0])
            fileOpen.close()
            if speedResult <= threshold:
                fileOpen = open(deviceId+"/validSpeed.txt","a+")
                fileOpen.write(str(speedResult))
                fileOpen.write("\n")
                fileOpen.close()
                fileOpen = open(deviceId+"/validXY.txt","a+")
                fileOpen.write(str(xyResult))
                fileOpen.write("\n")
                fileOpen.close()
                fileOpen = open(deviceId+"/validPressure.txt","a+")
                fileOpen.write(str(pressureResult))
                fileOpen.write("\n")
                fileOpen.close()
                return "1"
            else:
                return "0"
        else:
            return "0"
        
# Testing
    if xyC and speed:
        fileOpen = open(deviceId+"/validSpeed.txt","a+")
        fileOpen.write(str(speedResult))
        fileOpen.write("\n")
        fileOpen.close()
        fileOpen = open(deviceId+"/validXY.txt","a+")
        fileOpen.write(str(xyResult))
        fileOpen.write("\n")
        fileOpen.close()
        if pressure:
            fileOpen = open(deviceId+"/validPressure.txt","a+")
            fileOpen.write(str(pressureResult))
            fileOpen.write("\n")
            fileOpen.close()
        return "1"
    elif not xyC and not speed:
        return "0"
    elif pressure and (speed1 or xy1):
        if speed1:
            fileOpen = open(deviceId+"/validSpeed.txt","a+")
            fileOpen.write(str(speedResult))
            fileOpen.write("\n")
            fileOpen.close()
        if xy1:
            fileOpen = open(deviceId+"/validXY.txt","a+")
            fileOpen.write(str(xyResult))
            fileOpen.write("\n")
            fileOpen.close()
        fileOpen = open(deviceId+"/validPressure.txt","a+")
        fileOpen.write(str(pressureResult))
        fileOpen.write("\n")
        fileOpen.close()
        return "1"
    else:
        return "0"
    # if (speed and xyC):
    #     fileOpen = open(deviceId+"/validSpeed.txt","a+")
    #     fileOpen.write(str(speedResult))
    #     fileOpen.write("\n")
    #     fileOpen.close()
    #     fileOpen = open(deviceId+"/validXY.txt","a+")
    #     fileOpen.write(str(xyResult))
    #     fileOpen.write("\n")
    #     fileOpen.close()
    #     return "1"
    # elif (speed and pressure):
    #     fileOpen = open(deviceId+"/validSpeed.txt","a+")
    #     fileOpen.write(str(speedResult))
    #     fileOpen.write("\n")
    #     fileOpen.close()
    #     fileOpen = open(deviceId+"/validPressure.txt","a+")
    #     fileOpen.write(str(pressureResult))
    #     fileOpen.write("\n")
    #     fileOpen.close()
    #     return "1"
    # elif (xyC and pressure):
    #     fileOpen = open(deviceId+"/validXY.txt","a+")
    #     fileOpen.write(str(xyResult))
    #     fileOpen.write("\n")
    #     fileOpen.close()
    #     fileOpen = open(deviceId+"/validPressure.txt","a+")
    #     fileOpen.write(str(pressureResult))
    #     fileOpen.write("\n")
    #     fileOpen.close()
    #     return "1"
    # else:
    #     return "0"
