#Dado el texto 'esto es una prueba' imprimir una cadena formateada de la sig. manera

#'esto es una prueba <nombre>'
#-imprimir cuantas letras 'e' tiene la cadena 
#-capitalizar cadena
#-imprimir longitud de cadena 
#-reemplazar en la cadena de la latra 'o' por 0

dato = (input ("Ingrese el texto: "))
texto = dato
cuenta = 0
for carac in texto:
    if carac == 'e':
        cuenta += 1
print ( "El", dato, "tiene ", cuenta, "letra e")
print ( "Capitalización: ", texto.upper())
print ( "La longitud de la cadena es de: ", len(dato))
print ( texto.replace('o','0'), 'Reeplazamos la letra o por el numero 0')