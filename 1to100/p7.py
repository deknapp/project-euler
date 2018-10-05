# What is the 10 001st prime number?

import math

def basicSieve(n):
  """Given a positive integer n, generate the primes < n."""
  lst = []
  s = [1]*n
  for p in xrange(2, 1+int(math.sqrt(n-1))):
    if s[p]:
      a = p*p 
      s[a::p] = [0] * -((a-n)//p)
  for p in xrange(2, n): 
    if s[p]:
      lst.append(p) 
  return lst

start_val = 100000000

print basicSieve(start_val)[10000] 
