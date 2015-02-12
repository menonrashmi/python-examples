
def is_multiple(n,m):
   try: 
       if (int(n) % int(m) == 0):
           print "n is a multiple of m"
           return True
       print "n is not a multiple of m "
       return False 
   except ValueError:     
       print ("Must be integer number")
           
is_multiple(50, "dfs")
is_multiple(50, 3)
is_multiple(50, 5)