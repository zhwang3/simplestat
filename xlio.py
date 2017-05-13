import xlrd
#file address
data=xlrd.open_workbook("")
table=data.sheet_by_index(0)
lnum=table.nrows
datalist=[]
for i in range(1,lnum):
    datalist.append(table.row_values(i))
varname=table.row_values(0)
dataset=[]
data0={}
c=0
vn=0
while c<len(datalist):
    ro = datalist[c]
    while vn<len(varname):
        data0[varname[vn]] = ro[vn]
        vn = vn + 1
    dataset.append(data0)
    c = c + 1
    vn=0
    data0={}
print dataset