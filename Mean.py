import csv
with open("HeightWeight.csv",newline='') as F:
    reader=csv.reader(F)
    fileData=list(reader)

fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    height=fileData[i][1]
    newData.append(float(height))

n=len(newData)

total=0
for i in newData:
    total=total+i

mean=total/n
print('mean='+str(mean))
