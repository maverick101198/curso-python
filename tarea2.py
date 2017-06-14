lista=[]
for i in range(4):
        print("Digite el numero", str(i + 1) + ":", end="")
        Digito = input()
        lista += [Digito]
print ("La lista creada es: ", lista)
print ("Primer numero de lista: ", lista[0])
print ("Ultimo numero de lista: ", lista[3])