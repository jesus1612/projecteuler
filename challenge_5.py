# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# iniciamos en un numero considerable para acelerar el calculo
number = 232791050

while True:
  # valida si el numero actual cumple los requerimientos
  divisible = 1
  # Itera por los primeros 20 numeros
  for i in range(1,21):
    if number % i != 0:
      divisible = 0
      break
  # si no los cumple, agrega uno al contador
  if divisible == 0:
    number += 1
  else:
    print(number)
    break