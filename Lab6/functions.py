import itertools as it
minsup=2

def checkSubset(subset,main):
    for i in subset:
        if i not in main:
            return False
    return True

def gen_candidate_itemsets(l,k):
    c,c1=[],[]
    for index1,item1 in enumerate(l):
        for index2,item2 in enumerate(l):
            if index2<=index1:
                continue
            joined_list = list(set(item1+item2))
            temp_combinations = list(it.combinations(joined_list,k))
            combination_list = [list(value) for value in temp_combinations]
            if combination_list:
                for item in combination_list:
                    item.sort()
                    if item not in c:
                        c.append(item)     
    for item in c:
        if item not in c1:
           c1.append(item)
    return c1

def prune(l,c,k):
    remove_indices=[]
    for index,item in enumerate(c):
        combinations = list(it.combinations(item,k-1)) 
        combination_list = [list(value) for value in combinations] 
        for items in combination_list:
            if checkSubset(items,l):
                if index not in remove_indices:
                    remove_indices.append(index)
    remove_indices.sort()
    remove_indices.reverse()
    for index in remove_indices:
        c.pop(remove_indices)
        
def generate_frequent_itemsets(l,c,df):
    support={}
    for item in c:
        support[tuple(item)]=0
        for transaction in df:
            if checkSubset(item,transaction):
                support[tuple(item)]+=1
    for value,count in support.items():
        if count>=minsup:
            l.append(list(value))
    return l