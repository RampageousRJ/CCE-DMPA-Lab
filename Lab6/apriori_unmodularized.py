import pandas as pd
import itertools

def checkSubset(subset,main):
    for ele in subset:
        if ele not in main:
            return False
    return True

if __name__=='__main__':
    # Read from an excel file to store in a dataframe
    df = pd.read_excel('database.xlsx')
    df.index=df['TID']
    df=df.drop('TID',axis=1)

    # Store transactions in a list of lists and store unique items
    itemset=[]
    minsup=int(input("Enter minimum support: "))
    uniq={}
    l=[]
    
    for row in df['Itemsets']:
        transaction=[]
        for item in row:
            if item != ',':
                transaction.append(item)
                if item not in uniq:
                    uniq[item]=1
                else:
                    uniq[item]+=1
        itemset.append(transaction)
    for value,count in uniq.items():
        if count>=minsup:
            l.append(list(value))
    freq=[]
    for item in l:
        freq.append(l)    
    length=len(l)
    k=2
    while len(l)!=0:
        c=[]
        for i in range(0,len(l)-1):
            for j in range(i+1,len(l)):
                temp = list(set(l[i]+l[j]))
                ctemp = list(itertools.combinations(temp,k))
                if len(ctemp)>0:
                    for r in ctemp:
                        if r not in c:
                            r=list(r)
                            r.sort()
                            c.append(list(r))
        c1=[]
        for item in c:
            if item not in c1:
                c1.append(item)
        c=c1
        sup={}
        l=[]
        for item in c:
            sup[tuple(item)]=0
            for transaction in itemset:
                if checkSubset(item,transaction):
                    sup[tuple(item)]+=1
        for value,count in sup.items():
            if count>=minsup:
                l.append(list(value))
        for item in l:
            freq.append(l)
        k+=1
    c1=[]
    for item in freq:
        if item not in c1:
            c1.append(item)
    freq=c1
    print(freq)