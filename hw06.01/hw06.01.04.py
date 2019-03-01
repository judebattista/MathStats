import math
catCount = 8
buff = 0.5

with open('hw06.01.04.txt','r') as infile:
    data = []
    for line in infile:
        data.extend(line.strip().split())
intData = sorted([int(strValue) for strValue in data])
print(intData)
length = len(intData)
maxData = intData[length-1]
minData = intData[0]
rangeData = maxData - minData
dataFloor = minData - buff
dataCeil = maxData + buff
width = math.ceil((dataCeil - dataFloor) / catCount)
print('The width is %f' % width)
mean = sum(intData)*1.0 / length
print('The mean is %f.' % mean)
s2 = 0.0
for datum in intData:
    s2 += (datum - mean) ** 2
s2 /= (length - 1)
s = math.sqrt(s2)
print('variance is %f. std dev is %f' % (s2, s))
categories = [dataFloor + i*width for i in range(0,catCount)]
categoryMeans = [floor + width / 2 for floor in categories]
print('The category means are:')
print(categoryMeans)
oneSdFloor = mean - s
oneSdCeil = mean + s
twoSdFloor = mean - s - s
twoSdCeil = mean + s + s
print('mean - s: %f, mean + s: %f, mean - 2s: %f, mean + 2s: %f' % (oneSdFloor, oneSdCeil, twoSdFloor, twoSdCeil))

oneSdCount = 0
twoSdCount = 0
dataDict = {}
for cmean in categoryMeans:
    dataDict[cmean] = 0
for datum in intData:
    for cmean in categoryMeans:
        if datum > cmean - width /2 and datum <= cmean + width / 2:
            dataDict[cmean] += 1
    if datum >= twoSdFloor and datum <= twoSdCeil:
        twoSdCount += 1
        if datum >= oneSdFloor and datum <= oneSdCeil:
            oneSdCount += 1
    
print('The frequencies are:')
print(dataDict)

print('Count within one std dev: %d, count within two std devs: %d' % (oneSdCount, twoSdCount))
