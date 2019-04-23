#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 02:53:25 2019

@author: Simon
"""
def network_plot_circle(N):
    n=len(N)
    x=[np.cos(2*np.pi*i/n) for i in range(n)]
    y=[np.sin(2*np.pi*i/n) for i in range(n)]
    for i in range(n):
        for j in range(i):
            if N[i][j]==1:
                plt.plot([x[i],x[j]],[y[i],y[j]],'b')
            if N[i][j]==2:
                plt.plot([x[i],x[j]],[y[i],y[j]],'g')
            if N[i][j]==3:
                plt.plot([x[i],x[j]],[y[i],y[j]],'y')
    plt.plot(x,y,'ro')
    plt.show()

phd = open("phd.txt").read()
pairs = [s.split(' ') for s in phd.splitlines()]
pairs = [[int(i) for i in j]for j in pairs]
n = max(max(j for j in pairs))
adjMatrix = [[0]*n for _ in range(n)]


for p in pairs:
    if  p[0]<400:
        adjMatrix[p[0]-1][p[1]-1]=2
        adjMatrix[p[1]-1][p[0]-1]=2
    elif p[0]>700:
        adjMatrix[p[0]-1][p[1]-1]=3
        adjMatrix[p[1]-1][p[0]-1]=3
    else:
        adjMatrix[p[0]-1][p[1]-1]=1
        adjMatrix[p[1]-1][p[0]-1]=1
    

network_plot_circle(adjMatrix)