sumSquare = 0
squareSum = 0

# sum of the squares of the first 100 numbers
for i in range(1, 101):
  sumSquare += (i * i)

# square of the sum ot the first 100 numbers
for i in range(1, 101):
  squareSum += i
squareSum = squareSum * squareSum

print(squareSum - sumSquare)