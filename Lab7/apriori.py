from itertools import combinations,permutations
from collections import OrderedDict
import pandas as pd
import re
k = 2
transactions = {'T1' : '134',
                'T2' : '235',
                'T3' : '1235',
                'T4' : '25',
                'T5' : '135'}
for i in transactions.keys():
    transactions[i] = ''.join(sorted(transactions[i]))

def checkSubset(sset,set):
    if len(sset) > len(set):
        return False
    newSet = []
    for num,item in enumerate(list(permutations(set))):
        newSet.append(''.join(list(item)))
    for itemset in newSet:
        if sset in itemset:
            return True
    return False

def calculateSupport(itemset, transactions):
    support_itemset = 0
    for i in transactions.values():
        if checkSubset(itemset,i):
            support_itemset += 1
    return support_itemset

candidateSet = {}
for i in transactions.values():
    for j in i:
        if j not in candidateSet.keys():
            candidateSet[j] = calculateSupport(j,transactions)
minSup = int(input("Enter the minimum support : "))

freqSet = {}
def generateFreqSet(candidateSet):
    for i in candidateSet.keys():
        if candidateSet[i] >= minSup:
            freqSet[i] = candidateSet[i]
    return freqSet

def removeDuplicates(word):
    word = ''.join(sorted(list(set(word))))
    return word

def generateCandidateSet(freqSet,K):
    new_keys = list(combinations(freqSet.keys(),K))
    for num,i in enumerate(new_keys):
        new_keys[num] = list(set(i))
        res = removeDuplicates(''.join(new_keys[num]))
        new_keys[num] = res
    candidateSet = {}
    for i in new_keys:
        i = ''.join(sorted(i))
        candidateSet[i] = calculateSupport(i,transactions)
    return candidateSet

def pruneFreqSet(freqSet):
    rm_arr = []
    for i in freqSet.keys():
        newSet_keys = list(freqSet.keys())
        newSet_keys.remove(i)
        for j in newSet_keys:
            if checkSubset(i,j):
                rm_arr.append(i)
    for i in rm_arr:
        freqSet.pop(i)
    return freqSet

while len(candidateSet.keys()) > 0:    
    candidateSet = generateCandidateSet(freqSet,k)
    for cand_item in candidateSet.keys():
        rm_keys = []
        for freq_item in freqSet.keys():
            if re.search(f'[{freq_item}]',cand_item):
                rm_keys.append(freq_item)
            list(set(rm_keys))
        for keys in rm_keys:
            freqSet.pop(keys)
    freqSet = generateFreqSet(candidateSet)
    freqSet = pruneFreqSet(freqSet)
    k += 1

print("Frequent Itemsets are : ", list(freqSet.keys()))