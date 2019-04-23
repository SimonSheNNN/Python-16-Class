#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 19:25:01 2019

@author: Simon
"""
from math import exp , sin , cos

def solve(x,ini,tol=0.0001): 
    #this is the previous value xn, and convert it to float so that can do calculations on it
    last=float(ini)     
    #while the error is bigger than tolerance, keeps going
    while( abs(x(last)[0])>tol):  
        #get the next value using the formula
        approx = last- (float(x(last)[0])/float(x(last)[1]))
        #set xn to xn-1
        last=approx
        print last
    return last


"""
test cases:
    
    
1. f(x) = x**2 − 1, f′(x) = 2x, x0 = 3
function output: 1.0000305180437934
my output: 1


2. f(x) = x**2 − 1, f′(x) = 2x, x0 = −1
function output: -1.0
my output: -1


3. f(x) = exp(x) − 1, f′(x) = exp(x), x0 = 1 
function output: 1.5641107898984284e-06
my output: 0



4. f(x) = sin(x), f′(x) = cos(x), x0 = 0.5.
function output: 3.311802132639069e-05
my output: 0
"""

'''
Bonus:
solve(lambda x: [x**2-1, 2*x], 3, 0.0001)
solve(lambda x: [x**2-1, 2*x], 3, 0.00001)
solve(lambda x: [x**2-1, 2*x], 3, 0.000001)
since we are finding functions with powers or exponetionals, as the iterations increase
it will satisfy tolerance more and more easily. 
so for 1E-3, the first function needs 4 iterations, 1E-4 needs 5, and this fifth iteration 
can satisfy all the way until toleration of 1E-10
'''