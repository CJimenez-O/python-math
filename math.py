import numpy as np
# ////////////////////////
# function interates while loop until x = 0 
# ex. 5 -> 16 -> 8 -> 4 -> 2 -> 0

def Seq(a):
 x0 = a
 x = x0
 counter = 0
 while(x != 1 and x != 0):
  if x%2 == 0:
    x /= 2
  else:
   x = 3*x + 1
  counter += 1
 return np.zeros(counter,dtype=int)
 
#  /////////////////////////
# arange array/list in accending order
arr = np.arange(4)
storage_vector = []
for i in arr:
    storage_vector.append(Seq(i))
print(storage_vector)
