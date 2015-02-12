"""
Python function that takes a positive integer n and returns 
the sum of the squares of all the odd positive integers smaller than n
"""
def sum_of_sqrs(n):
    if n > 0:            
        print sum([pow(x,2) for x in range(1,n,2)])
    else :
       print "Enter positive number"     
    
sum_of_sqrs(2)
sum_of_sqrs(-3)