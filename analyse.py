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
    tarea=0
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
    tarea=0
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
data=[3,4,1,7,3,2,6,4,2,1,6,3,4,5,2,5,4,3,4]
freq(data)
firstquatertile(data)
thirdquatertile(data)
print iqr(data)