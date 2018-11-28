#Given an array of integers, return a new array with each value doubled.

#For example:

#[1, 2, 3] --> [2, 4, 6]

#For the beginner, try to use the map method - 
#it comes in very handy quite a lot so is a good one to know.

#In my own words: Map() is a function that consists of two parts: a function 
#and an iterable.  The function is applied to each item in the iterable, 
#and return from there.   


def maps(a):
    iterable = a
    
    def double(n):
        return n*2
    
    result = map(double, iterable)
    print(result)
    
    #converting map object to list 
    numbersDouble = list(result)
    
    return numbersDouble


print(maps((1,2,3,4,5)))