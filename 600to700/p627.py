#Find F(30,10001) mod 1000000007.

# Let's say it was only F(4, 10001)
# Then, we can ignore 1 (1 to any power is 1
# We get 10,001 combos from 3
# We get 10,001 combos from 2
# We do not get 10,001 combos from 4 because every multiple of 4 that is <= 2^10000 is a repeat

def combos_from_prime(prime, max_multiples, max_integer):
  print 'prime is', prime
  combos = max_multiples
  number = prime
  number *= prime
  while number <= 30:
    combos += max_multiples - max_multiples/number 
    print number
    print max_multiples - max_multiples/number
    number *= prime
  return combos 

m = 30
n = 10001
primes = [2,3,5,7,11,13,17,19,23,29]

combos = 1
for prime in primes:
  combos *= combos_from_prime(prime, n, m)

print combos % (pow(10, 9) + 7)    
