# Find the largest palindrome made from the product of two 3-digit numbers

def isPalindrome(number):
  return (int(str(number)) == int(str(number)[::-1]))

mx = 0
for a in range(999, 99, -1):
  for b in range(900):
    product = a*(a-b)
    if product > mx: 
      if isPalindrome(product):
        mx = product  

print mx
