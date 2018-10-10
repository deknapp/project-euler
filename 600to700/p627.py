# unique products using n positive integers not exceeding m

primes_under_30 = [2,3,5,7,11,13,17,19,23,29]
primes_under_9 = [2,3,5,7]

def additional_products(primes, m, n):
  counter = 0
  for i in range(m):
    counter += n - 1  
  return counter
  
def F(m, n, primes_under_m):
  counter = 0
  for i in range(len(primes_under_m)):
    counter += additional_products(primes_under_m[:i+1], m, n) 
  return counter 

print F(30,2, primes_under_30)
print F(9,2,primes_under_9)
