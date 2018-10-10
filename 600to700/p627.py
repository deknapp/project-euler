# unique products using n positive integers not exceeding m

import itertools

def findsubsets(S,m):
  return set(itertools.combinations(S, m)) 

def product(lst):
  product = 1
  for item in lst:
    product *= item
  return product

def unique_products(m, n):
  super_set = []
  for i in range(1, m+1):
    super_set.append([i]*n)
  flat_set = [item for subset in super_set for item in subset] 
  subsets = list(findsubsets(flat_set,n))
  products = [product(subset) for subset in subsets]
  return len(list(set(products))) 
 
print unique_products(9,2) 
print unique_products(30,2)


