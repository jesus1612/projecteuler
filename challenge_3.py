# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# Find the prime factors
num = 13195
counter = 0
for i in range(num + 1, 2, -1):
  if num % i == 0:
    counter = 1
    for j in range (int(i/2) +1,2,-1 ):
      if i % j == 0:
        counter = 0
    if counter == 1:
      print(i)
      break
