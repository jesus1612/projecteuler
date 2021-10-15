#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# contain the parcial largest palindrome
palindrome = 0

for i in range(1000, 100, -1):
  for j in range(1000,100, -1):
    word = str(j*i)
    if word == word[::-1]:
      if int(palindrome) < int(word):
        palindrome = word
print(palindrome)
