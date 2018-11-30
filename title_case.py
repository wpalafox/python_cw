#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 18:48:47 2018

@author: williampalafox
"""

#A string is considered to be in title case if each word in the string is either
#(a) capitalised (that is, only the first letter of the word is in upper case) 
#or (b) considered to be an exception and put entirely into lower case unless 
#it is the first word, which is always capitalised.

#Write a function that will convert a string into title case, given an optional 
#list of exceptions (minor words). The list of minor words will be given as a 
#string with each word separated by a space. Your function should ignore the 
#case of the minor words string -- it should behave in the same way even if the 
#case of the minor word string is changed.

###Arguments (Haskell)

#First argument: space-delimited list of minor words that must always be 
#lowercase except for the first word in the string.
#Second argument: the original string to be converted.
###Arguments (Other languages)

#First argument (required): the original string to be converted.
#Second argument (optional): space-delimited list of minor words that must 
#always be lowercase except for the first word in the string. 
#The JavaScript/CoffeeScript tests will pass undefined when this argument
#is unused.



def title_case(title):
  
    
  #1. Lowercase the string  
  string = title.lower()
 #2. Split the string into an array of strings 
  split_string = string.split() 

  #3. Map over the array 
  def helper_function(string):
      return string[0].upper()+string[1:]
  
  result = map(helper_function, split_string)
  
  
  
  #converting map object to list, then join by space
  
  listTitle = list(result)
  joinTitle =" ".join(listTitle)
  
  return joinTitle
   

print(title_case('heelllooo thisissss issss aaaa  test'))


