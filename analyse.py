import math
def mean(data):
    sum=0.0
    i=0
    while i<len(data):
        sum=sum+data[i]
        i=i+1
    a=sum/len(data)
    return a
def devi(data):
    m=mean(data)
    devdata=[]
    i=0
    while i<len(data):
        devdata.append(data[i]-m)
        i=i+1
    return devdata
def ss(data):
    de=devi(data)
    i=0
    s=[]
    while i<len(de):
        s.append(de[i]*de[i])
        i=i+1
    sums=0.0
    p=0
    while p<len(s):
        sums=sums+s[p]
        p=p+1
    return sums
def vari(data,type):
    va=0.0
    if type=="sample":
        sums = ss(data)
        va = sums / len(data) - 1
    elif type=="popu":
        sums=ss(data)
        va=sums/len(data)
    else:
        print "unexpected variance type"
    return va
def sd(data,type):
    sdevi=0.0
    if type=="sample":
        v=vari(data,"sample")
        sdevi=math.sqrt(v)
    elif type=="popu":
        v=vari(data,"popu")
        sdevi=math.sqrt(v)
    else:
        print "unexpected sd type"
    return sdevi
def freq(data):
    b={}
    for a in data:
        if a in b:
            b[a]=b[a]+1
        else:
            b[a]=1
    print b
    return b
def firstquatertile(data):
    data0=freq(data)
    tarea=0.0
    for c in data0:
        tarea=tarea+data0[c]
    print tarea
    firstquaterarea=0.25*tarea
    squarearea=0.0
    i=0
    while squarearea<firstquaterarea:
        if i in data0:
            squarearea=squarearea+data0[i]
            if squarearea>firstquaterarea:
                break
            else:
                i=i+1
        else:
            i=i+1
    deltaarea=firstquaterarea-squarearea
    x=deltaarea/data[i]
    fr=x+i
    print fr
    return fr
def thirdquatertile(data):
    data0=freq(data)
    tarea=0.0
    for c in data0:
        tarea=tarea+data0[c]
    print tarea
    thirdquaterarea=0.75*tarea
    squarearea=0.0
    i=0
    while squarearea<thirdquaterarea:
        if i in data0:
            squarearea=squarearea+data0[i]
            if squarearea>thirdquaterarea:
                break
            else:
                i=i+1
        else:
            i=i+1
    deltaarea=thirdquaterarea-squarearea
    x=deltaarea/data[i]
    th=x+i
    print th
    return th
def iqr(data):
    delta=thirdquatertile(data)-firstquatertile(data)
    return delta
def zscore(data):
    m=mean(data)
    sde=sd(data,"popu")
    i=0
    zs=[]
    while i<len(data):
        zs.append((data[i]-m)/sde)
        i=i+1
    return zs
data=[10,20,30,40,50,60,70,80,90]
print devi(data)
print ss(data)
print vari(data,"popu")
print sd(data,"popu")
print zscore(data)