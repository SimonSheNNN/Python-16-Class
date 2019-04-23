#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 01:55:13 2019

@author: Simon
"""
import re


#1
def mytype(v):
    myv=str(v)
    if re.match("\[\w+(,\w+)+",myv):
        return 'str'
    elif re.match('\[',myv):   #search for [ which is always at the start of lists
        return 'list'
    elif re.match('^\d+\.\d+$',myv):     #search for . after numbers
        return "float"
    elif re.search('^\d+$',myv):                       #else is integer
        return "int"
    else:
        return "str"
    

    
#2
def findpdfs(L):
    myL= ', '.join(L)           #join the list and separate with ", "
     #find all that is after ", " and before .pdf and has numbers or letters in between
    return re.findall('\w+(?:\.\w+)*(?=.pdf)',myL)   

"""
L=['sadad.pdf', 'sadasdasdasdas.pdf', '123sd.pdf', '123dsad.sdf']
findpdfs(L)

"""

#3
import urllib2
def findemail(url):
    page=urllib2.urlopen(url).read()
    return re.findall(r'[a-zA-Z0-9!#$%&*+-/=?^_`{|}~]+(?:@| AT | at |\[at]|\[AT])[-a-zA-z0-9]+(?:(?:\.| DOT | dot |\[dot]|\[DOT])[-a-zA-z0-9]+)+',page)
    
    
"""

findemail("https://www.math.ucla.edu/~hangjie/teaching/Winter2019PIC16/regexTest")

"""


#4
def happiness(text):
    happy=0     
    count=0    
    mytext=text.lower()
    #findall the text using regular expressions based on only words
    x= re.findall('\w+',mytext)  
    for i in x:     #got a list, for all elements in list 
        if i in happiness_dictionary:       #if element is in the dict
            happy=happy+happiness_dictionary[i]     #retrieve happiness, and count+1
            count+=1
    return happy/count    #average