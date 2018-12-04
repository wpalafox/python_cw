#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 05:04:22 2018

@author: williampalafox
"""
def rps(p1, p2):
    #your code here
    #helper function translates object to value 
    def object_to_number(object):
        if object == 'scissors':
            return 0
        elif object == 'paper':
            return 1
        elif object == 'rock':
            return 2
        else: 
            return "error" 
        
    
    p1_number=object_to_number(p1)
    p2_number=object_to_number(p2)
    
    #print(p1_number)
    #print(p2_number)
    
    difference = p1_number - p2_number 
    mod = difference%3 
    
    if mod == 2:
        return "Player 1 won!"
    elif mod == 1:
        return "Player 2 won!"
    elif mod == 0:
        return "Draw!" 
    
print(rps('rock', 'rock'))

