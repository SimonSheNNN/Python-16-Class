 # -*- coding: utf-8 -*-
"""
Simeng Shen 404826665
"""
#1
def largerIndex(c):
    k=list()  #empty list
    for i in range(len(c)):     #in the length of the list
        if c[i]>i:      #do the following comparisons
            k.append(1)
        elif c[i]<i:
            k.append(-1)
        else:
            k.append(0)
    return k


#largerIndex([1,4,6,7,9])


#2
def squareUpTo(n):
    l=list()        #empty list
     #in the range of n, in case of squareUpTo(1), use range(n+1) for safety
    for i in range(n+1):  
        # n**2 is always bigger than n, so must in range
        if i**2 <= n:
            l.append (i)
        #break when bigger to save time
        else:
            break
    return l

#squareUpTo(1)
    

#3
#use random module
import random as rand
def flip1in3():
    #only success when got Head Head,ignore Head Tail, fail otherwise
    while True:
        x=rand.randint(0,1) #first coin
        y=rand.randint(0,1) #second coin
        if x ==0:
            if y==0:
                return True
            elif y==1:
                continue
        elif x==1:
            return False
    #this gives a 1/3 success


"""
count=0
for i in range(1000):
    if flip1in3():
        count+=1
count
"""


#4
def duplicates(c):
    l=list()
    for i in range(len(c)): #first loop that looks for duplicate for all element
        k=i+1   #element after that first element
        for j in range(k,len(c)):
            if c[i] == c[j] and c[i] not in l:      #if duplicate and not already in list
                l.append(c[i])
            
    return l
            
#duplicates([1,2,3,1,1,1,1,1,1,1,1,4,3,2,4])
 
#5
def longestpath(d):
    countAll=0      #the longest of all paths
    for i in d:     #for every scenario
        count=1     #first key to value is already set
        v=d[i]      #starting value
        x=d.copy()  #create a duplicate so dont destroy the original
        del x[i]    #delete key to ensure doesnt loop back
        
        dup=True
        while dup:
            dup=False#if no dup found, exit loop
            
            #look for duplicate, when found, set next key to current value, and delete current key
            for j in x:
                if j==v and j!=i:
                    count =count +1
                    v=x[j]
                    del x[j]
                    dup=True
                    break
                
        #get the longest
        if count>countAll:
                countAll=count
    return countAll
    
'''
d= { "a": "b", "b": "c", "c": "d", "d": "e", "e": "f" }
longestpath(d)
'''
    
    
    
    
    