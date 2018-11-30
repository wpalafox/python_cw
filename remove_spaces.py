#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 04:47:58 2018

@author: williampalafox
"""

def no_space(x):
  l = list(x)
  i=0  
  while i < len(l):
    if l[i] == " ":
        l[i] = ""
        i += 1 
    else:
        i += 1
  result = "".join(l)
  return result 


print(no_space("asdfASd  fas fd d d d d dd d d ")) 
        
        
        
