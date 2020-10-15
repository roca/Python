from utils import *

a = [-1,3,-4,5,1,-6,2,1]

b = [2, 2, 2, 2, 2, 3, 4, 4, 4, 6]
c = [50]

print(equilibrium(a))
print(occurrences(a))

print(leader(b))
print(leader(c))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))