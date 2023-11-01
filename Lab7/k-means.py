import math
import pandas as pd

df=pd.read_excel('database.xlsx')
dataset={}
for index,row in df.iterrows():
    dataset[row['ID']]=[row['Height'],row['Weight']]

def calcDistance(x1,y1,x2,y2):
    return math.sqrt((math.pow((x1-x2),2))+(math.pow((y2-y1),2)))

def contain(value,cluster):
    for temp in cluster:
        if value in temp:
            return True
    return False

cluster=[]
centroid={}
temp=1
k = int(input('Enter number of clusters: '))
for i in range(k):
    centroid[temp]=dataset[temp]
    cluster.append([])
    temp+=1

while True:
    flag=0
    for value,point1 in dataset.items():
        minDist=9999999999
        minDistCluster=-1
        for i in range(0,k):
            point2 = centroid[i+1]
            dist = calcDistance(point1[0],point1[1],point2[0],point2[1])
            if minDist>dist:
                minDist=dist
                minDistCluster=i+1
        if value in cluster[minDistCluster-1]:
            flag=1
        cluster[minDistCluster-1].append(value)
        for i in range(2):
            centroid[minDistCluster][i] = (centroid[minDistCluster][i]+point1[i])/2
    if flag==0:
        break
print("CENTROID: ",centroid)
print("CLUSTER: ",cluster)