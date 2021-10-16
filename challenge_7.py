# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

primeNumbers = []
currentNumber = 2

while len(primeNumbers) < 10001:
  cont = 0
  for i in range(1, currentNumber):
    if currentNumber % i == 0:
      cont += 1
      if cont == 2 : break

  if cont < 2:
    primeNumbers.append(currentNumber)

  currentNumber += 1

print(primeNumbers[-1])