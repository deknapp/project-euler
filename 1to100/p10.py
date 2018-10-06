import math

def basicSieveSum(n):
  """Given a positive integer n, generate the primes < n."""
  s = [1]*n
  for p in xrange(2, 1+int(math.sqrt(n-1))):
    if s[p]:
      a = p*p 
      s[a::p] = [0] * -((a-n)//p)
  sm = 0
  for p in xrange(2, n): 
    if s[p]:
      sm += p
  return sm
 
print basicSieveSum(2*pow(10,6))

