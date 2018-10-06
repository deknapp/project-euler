#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc. 

for c in xrange(1, 1000):
  for b in xrange(1, 1000-c):
    a = 1000-b-c
    if a*a + b*b == c*c:
      print a*b*c
      exit()
