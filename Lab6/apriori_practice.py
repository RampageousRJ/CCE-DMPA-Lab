import itertools as it
import pandas as pd
import numpy as np

def check_subset(subset,superset):
    for item1 in subset:
        if item1 not in superset:
            return False
    return True

def gen_candidate_set(l,k):
    c,c1=[],[]
    for index1,item1 in enumerate(l):
        for index2,item2 in enumerate(l):
            if index2<=index1:
                continue
            temp = list(set(item1+item2))
            ctemp = list(it.combinations(temp,k))
            temp = [list(item) for item in ctemp]
            for itemset_list in temp:
                if itemset_list not in c:
                    itemset_list.sort()
                    c.append(itemset_list)
    for items in c:
        if items not in c1:
            c1.append(items)
    return c1

def prune(l,k,c):
    remove_indices = []
    for index,value in enumerate(c):
        temp = list(it.combinations(value,k-1))
        temp_list = [list(item) for item in temp]
        for item in temp_list:
            if check_subset(item,l):
                if index not in remove_indices:
                    remove_indices.append(index)
    remove_indices.sort()
    remove_indices.reverse()
    for index in remove_indices:
        c.pop(index)

def gen_frequent_itemsets(c,df,minsup):
    support={}
    l=[]
    for item in c:
        support[tuple(item)]=0
    for item in support.keys():
        for index,row in df.iterrows():
            if check_subset(item,row['Itemsets']):
                support[tuple(item)]+=1
    for item,freq in support.items():
        if freq>=minsup:
            l.append(list(item))
    return l

def calculate_support(item,df):
    sup=0
    for index,row in df.iterrows():
        transaction = row['Itemsets'].split(',')
        if check_subset(item,transaction):
            sup+=1
    return sup

def calculate_confidence(df,frequent_itemsets):
    for item in frequent_itemsets:
        if len(item)<2:
            continue
        print(f"\nRULES FOR {item}")
        k = len(item)
        for i in range(1,k):
            combinations = list(it.combinations(item,i))
            listcomb = [list(temp) for temp in combinations]
            for comb in listcomb:
                print(f"Confidence: {''.join(list(set(comb)))} -> {''.join(list(set(item)-set(comb)))} = {round(calculate_support(df=df,item=item)/calculate_support(df=df,item=comb),2)}")

df = pd.read_excel('database.xlsx')
df.index = df['TID']
df.drop(['TID'],inplace=True,axis=1)
candidates = {}
minsup = int(input("Enter minimum support: "))

for index,transaction in df.iterrows():
    items = transaction['Itemsets'].split(',')
    for item in items:
        if item in candidates:
            candidates[item]+=1
        else:
            candidates[item]=1
l=[]
frequent_itemsets=[]
for item,freq in candidates.items():
    if freq>=minsup:
        l.append(list(item))
        frequent_itemsets.append(list(item))
k=2
while len(l)!=0:
    c = gen_candidate_set(l,k)
    prune(l,k,c)
    l=gen_frequent_itemsets(c,df,minsup)
    for item in l:
        frequent_itemsets.append(item)
    k+=1
c1=[]
for item in frequent_itemsets:
    if item not in c1:
        c1.append(item)
frequent_itemsets=c1
print(frequent_itemsets)
calculate_confidence(df,frequent_itemsets)