# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#1, 2, 3, 5, 8

sm = 2
previous_fib = 1
fib = 2 

while True:
  if fib > 4*pow(10,6):
    break
  next_fib = fib + previous_fib
  if next_fib%2 == 0:
    sm += next_fib
  previous_fib = fib
  fib = next_fib

print sm 
