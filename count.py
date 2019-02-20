#The main idea is to count all the occuring characters(UTF-8) in string. 
#If you have string like this aba then the result should be { 'a': 2, 'b': 1 }
#What if the string is empty ? Then the result should be empty object literal { }


#Passes Sample Tets but fails attempt 

def count(string):
    # The function code should be here
    array={}
    
    
    for letter in string: 
        if letter not in array:   
            count = 1
            array[letter] = count
        elif letter in array: 
            count += 1
            array[letter] = count
    return array

print(count("aba"))