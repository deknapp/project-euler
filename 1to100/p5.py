#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from operator import mul

def isEvenlyDivisible(number, divisor_list):
  for divisor in divisor_list:
    if number%divisor != 0:
      return False
  return True  		


divisor_list = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
prime_product = 2*3*5*7*11*13*17*19
candidate = prime_product
 
while not isEvenlyDivisible(candidate, divisor_list):	
  candidate += prime_product

print candidate 
