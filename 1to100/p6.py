#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

print [pow(i,2) for i in range(1,101)]
sum_squares = sum([pow(i,2) for i in range(1,101)]) 
square_sum = pow(sum(range(1,101)), 2)

print sum_squares - square_sum
