import pandas as pd
import math

def calculate_distance(x1,x2,y1,y2):
    return math.fabs(y2-y1)+math.fabs(x2-x1)

def initialiseClusters():
    n = int(input("Enter number of clusters: "))
    k=0
    for i in range(n):
        clusters.append([i+1])
        centroid[i+1]=[(float)(df.iloc[i]['Height']),(float)(df.iloc[i]['Weight'])]
        k+=1
    return n

def clusteringAlgorithm():
    flag=False
    for i in range(len(df.index)):
        minDist = 999999
        minDistCluster = -1
        x1 = df.iloc[i]['Height']
        y1 = df.iloc[i]['Weight']
        for index,cluster in centroid.items():
            x2=cluster[0]
            y2=cluster[1]
            dist = calculate_distance(x1,x2,y1,y2)
            if dist<minDist:
                minDist = dist
                minDistCluster = index-1
        if i+1 not in clusters[minDistCluster]:
            clusters[minDistCluster].append(i+1)
            centroid[minDistCluster+1][0] = (centroid[minDistCluster+1][0] + x1)/2
            centroid[minDistCluster+1][1] = (centroid[minDistCluster+1][1] + y1)/2
            flag=True
    return flag
            
if __name__=='__main__':
    df = pd.read_excel('database.xlsx')
    df.index=df['ID']
    df.drop(['ID'],inplace=True,axis=1)
    clusters=[]
    centroid={}
    n = initialiseClusters()
    flag = True
    while flag:
        flag = clusteringAlgorithm()
    print("CLUSTERS: ", clusters)
    print("CENTROIDS: ", centroid)