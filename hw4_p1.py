#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 02:26:19 2019

@author: Simon
"""

import turtle as t


def ngon(n):
    angle=180-(n-2)*180/n       #angle of a normal polygon
    for _ in range (n):
        t.fd(float(100*5/n))        #make sure the size is not too big
        t.right(angle)
    t.done()
    
#ngon(3)