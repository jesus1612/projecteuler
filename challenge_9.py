b = 1
c= 0
NotResult = True

# Ciclo principal que hará iterar el número mayor
while NotResult:
  # Ciclo menos que itera dentro del rango del número mayor
  for a in range(1, b):
    # Obtenemos c con pitagoras
    c = (a**2 + b**2) ** 0.5
    # verificamos que la suma de nuestras variables tenga el resultado esperado
    if (a + b + c) == 1000:
      print(a*b*c)
      NotResult = False
  # Agregamos uno en b para ampliar los parametros y así encontrar la suma adecuada
  b+=1
