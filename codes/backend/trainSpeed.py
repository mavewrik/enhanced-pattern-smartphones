
# coding: utf-8



import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import pandas as pd

def train(deviceId):
    data1 = []
    data2 = []
    for i in range(1,10):
        for j in range(i+1,11):
            data11 = pd.read_csv(deviceId+"/train/speed"+str(i)+".csv")
            data21 = pd.read_csv(deviceId+"/train/speed"+str(j)+".csv")
            data1.append(data11)
            data2.append(data21)
    x = []
    y = []
    for k in range(0,45):
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
        for i in range(0,len(x2)):
            #a = [x2[i],x4[i]]
            a = [x2[i]]
            x5.append(a)
        for i in range(0,len(y2)):
            #b = [y2[i],y4[i]]
            b = [y2[i]]
            y5.append(b)
        x11 = np.array(x5)
        y11 = np.array(y5)
        x.append(x11)
        y.append(y11)
    distance = []
    path = []
    for i in range(0,45):
        distance11,path11 = fastdtw(x[i], y[i], radius=10,  dist=euclidean)
        distance.append(distance11)
        path.append(path11)
    euc = []
    for j in range(0,45):
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
    print(maxi)
    print(mini)
    for i in euc:
        if maxi-len(i) > 0:
            for j in range(0,maxi-len(i)):
                i.append(0)
    euclid = np.array(euc)
    out = euclid.std(0)
    print(out)
    print(len(out))
    out = out.tolist()

    #Thresholding
    finalValues = []
    for per in range(11,21):
        data1 = []
        data2 = []
        for j in range(1,11):
            data11 = pd.read_csv(deviceId+"/train/speed"+str(per)+".csv")
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
    # mini = min(finalValues)
    # maxi = np.amax(finalValues)
    # interval = (maxi-mini) / 5
    # hist,bins = np.histogram(finalValues,bins = [mini,mini+interval,mini+2*interval,mini+3*interval,mini+4*interval,maxi])
    # print(hist,bins)
    # max = hist[4]
    # index = 4
    # for i in range(3,-1,-1):
    #     if hist[i] > max:
    #         max = hist[i]
    #         index = i
    # a = bins[index]
    # b = bins[index+1]
    # sum = 0
    # for fr in finalValues:
    #     if fr >= a and fr <= b:
    #         sum += fr
    # threshold = sum/max
    
    meanF = np.mean(finalValues) * 1.0
    stdF = np.std(finalValues) *1.0
    for zzz in finalValues:
        z = (zzz - meanF)/stdF
        if z > 2.0:
            finalValues.remove(zzz)
    threshold1 = max(finalValues)
    meanF = np.mean(finalValues) * 1.0
    stdF = np.std(finalValues) * 1.0
    threshold2 = 2.5*stdF + meanF
    threshold = min(threshold1,threshold2)
    print(threshold)
    fileOpen = open(deviceId+"/speedThreshold.txt","w+")
    fileOpen.write(str(threshold))
    fileOpen.write("\n")
    for out1 in out:
        fileOpen.write(str(out1))
        fileOpen.write("\n")
    fileOpen.close()
    fileOpen = open(deviceId+"/validSpeed.txt","w+")
    for val in finalValues:
        fileOpen.write(str(val))
        fileOpen.write("\n")
    fileOpen.close()

#train("1332443d1016771a")