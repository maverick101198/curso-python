#crear 20 numeros aleatorio entre el 0 y el 100
#imprimir una lista de los numeros generados 
#ordenados ascendentemente, primeros los pares y luego los impares

#ejemplo: si los num generados sin [4,3,5,6,2]
#el resulatdo sera: [2,4,6,3,5]

import random
lista_aleatorio = []
lista_par = []
lista_impar = []

for i in range (20):
  
    lista_aleatorio.append(random.randint(0, 100))
    
print (lista_aleatorio)

print (lista_aleatorio)
lista_aleatorio.sort()
print('Orden ascendente')
print (lista_aleatorio)

while len(lista_aleatorio) > 0:
    num = lista_aleatorio.pop()
    if (num%2 == 0):
      lista_par.append(num)
      
    else:
      lista_impar.append(num)
      
print ("Numeros pares: ")
print (lista_par)
lista_par.sort()
print (lista_par, "Manera ascendente")
print ("Numeros impares")
print (lista_impar)
lista_impar.sort()
print (lista_impar, "Manera ascendente")