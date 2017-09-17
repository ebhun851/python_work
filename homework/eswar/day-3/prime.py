'''
Created on Sep 15, 2017

@author: NIS1526-mbp
'''
#!/usr/bin/python 
for num in range(10,20):  #to iterate between 10 to 20    
    for i in range(2,num): #to iterate on the factors of the number    
        if num%i == 0:      #to determine the first factor          
            break #to move to the next number, the #first FOR    
        else:                  # else part of the loop      
            print num, 'is a prime number'
            break