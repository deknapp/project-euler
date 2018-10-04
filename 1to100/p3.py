import math

#What is the largest prime factor of the number 600851475143 ?

# From an answer here: https://stackoverflow.com/questions/2897297/speed-up-bitstring-bit-operations-in-python 
def basicSieve(n):
  """Given a positive integer n, generate the primes < n."""
  s = [1]*n
  for p in xrange(2, 1+int(math.sqrt(n-1))):
    if s[p]:
      a = p*p
      s[a::p] = [0] * -((a-n)//p)
  for p in xrange(2, n):
    if s[p]:
      yield p 

number = 600851475143
max_prime_factor = 0
for prime in basicSieve(int(math.sqrt(number))):
  if number%prime == 0 and prime > max_prime_factor:
    max_prime_factor = prime

print max_prime_factor
