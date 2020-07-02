import pandas as pd 
from collections import Counter 
  
pd = input ("Enter a string : ")
res = Counter(pd) 

print ("Count of all characters in " + pd + " is :\n\n " +  str(res)) 
