# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# Find the prime factors
num = 13195

for i in range(int(num/2) + 1, 0, -1):
  if num % i == 0:
    print(i)
    break